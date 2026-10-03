#!/usr/bin/env python3
"""Compare declared editing invariants. Reads UTF-8 files; does not edit them."""
import argparse
from collections import Counter
from decimal import Decimal
import json
from pathlib import Path
import re
import sys

SIMPLE=re.compile(r'\{[A-Za-z_][A-Za-z0-9_]*\}')

def unique_object(pairs):
    result={}
    for key,value in pairs:
        if key in result:raise ValueError('Duplicate JSON key: '+key)
        result[key]=value
    return result

def invalid_constant(value):
    raise ValueError('Nonstandard JSON constant: '+value)

def structure(a,b,path='$'):
    issues=[]
    if type(a) is not type(b):return [{'kind':'json_type_changed','path':path}]
    if isinstance(a,dict):
        if a.keys()!=b.keys():issues.append({'kind':'json_keys_changed','path':path,'before':sorted(a),'after':sorted(b)})
        for key in sorted(a.keys() & b.keys()):issues+=structure(a[key],b[key],path+'['+json.dumps(key)+']')
    elif isinstance(a,list):
        if len(a)!=len(b):issues.append({'kind':'json_array_length_changed','path':path,'before':len(a),'after':len(b)})
        for i,(x,y) in enumerate(zip(a,b)):issues+=structure(x,y,f'{path}[{i}]')
    elif not isinstance(a,str) and a!=b:issues.append({'kind':'nontext_value_changed','path':path,'before':a,'after':b})
    return issues

def strings(node,path='$'):
    if isinstance(node,str):return {path:node}
    if isinstance(node,dict):
        return {p:s for k,v in node.items() for p,s in strings(v,path+'['+json.dumps(k)+']').items()}
    if isinstance(node,list):return {p:s for i,v in enumerate(node) for p,s in strings(v,f'{path}[{i}]').items()}
    return {}

def supported_simple(text):
    # Refuse common unsupported formats instead of returning a false clean bill.
    # This does not attempt to identify or parse every templating language.
    if '{{' in text or '}}' in text or '${' in text or re.search(r'\{[^{}]*,\s*(?:plural|select|selectordinal)\b',text):return False
    rest=SIMPLE.sub('',text)
    return '{' not in rest and '}' not in rest

def main():
    p=argparse.ArgumentParser(description=__doc__,epilog=(
        'Exit 0: declared checks pass; 1: a mismatch; 2: invalid input or unsupported placeholder syntax. '
        'No semantic, grammar, readability or accessibility validation. '
        '--simple-placeholders supports only {identifier}; it rejects ICU, mustache and ${...}. '
        'For other formats, omit that flag and supply exact --literal values, or use the actual formatter. '
        'Decimal JSON numbers are compared exactly and displayed as strings in issue reports.'))
    p.add_argument('before',type=Path);p.add_argument('after',type=Path)
    p.add_argument('--json',action='store_true',dest='is_json',help='Allow string-value edits while preserving recursive keys, array lengths, types and non-string values.')
    p.add_argument('--simple-placeholders',action='store_true',help='Compare {identifier} counts separately in each JSON string, or across a plain text file.')
    p.add_argument('--literal',action='append',default=[],help='An exact raw string whose occurrence count must stay unchanged; repeatable. Must occur in before.')
    args=p.parse_args()
    if not (args.is_json or args.simple_placeholders or args.literal):p.error('Choose at least one declared check')
    if any(not s for s in args.literal):p.error('--literal must not be empty')
    try:
        before=args.before.read_text(encoding='utf-8');after=args.after.read_text(encoding='utf-8')
        issues=[];unsupported=[];checks=[]
        if args.is_json:
            a=json.loads(before,object_pairs_hook=unique_object,parse_float=Decimal,parse_constant=invalid_constant)
            b=json.loads(after,object_pairs_hook=unique_object,parse_float=Decimal,parse_constant=invalid_constant)
            issues+=structure(a,b);checks.append('json_structure_and_nontext_values');astr=strings(a);bstr=strings(b)
        else:astr={'$':before};bstr={'$':after}
        for literal in args.literal:
            n=before.count(literal)
            if n==0:raise ValueError('Declared literal does not occur in before: '+literal)
            m=after.count(literal);checks.append('literal_occurrence_count')
            if n!=m:issues.append({'kind':'literal_count_changed','literal':literal,'before':n,'after':m})
        if args.simple_placeholders:
            checks.append('simple_placeholders_per_string')
            for path in sorted(astr.keys() | bstr.keys()):
                x=astr.get(path,'');y=bstr.get(path,'')
                if not supported_simple(x) or not supported_simple(y):
                    unsupported.append({'path':path,'reason':'Only {identifier} placeholders are supported by this mode.'});continue
                cx=Counter(SIMPLE.findall(x));cy=Counter(SIMPLE.findall(y))
                if cx!=cy:issues.append({'kind':'placeholder_counts_changed','path':path,'before':dict(cx),'after':dict(cy)})
        status='unsupported' if unsupported else ('mismatch' if issues else 'declared_checks_pass')
        result={'status':status,'checks':checks,'issues':issues,'unsupported':unsupported,
                'limitations':['Only explicitly selected mechanical properties were checked.','Passing does not establish semantic equivalence, appropriate target language, good writing or formatter validity.','Literal occurrence counts do not verify where a literal is used.']}
        print(json.dumps(result,ensure_ascii=False,indent=2,default=str))
        return 2 if unsupported else (1 if issues else 0)
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({'status':'input_error','error':str(exc)},ensure_ascii=False),file=sys.stderr);return 2

if __name__=='__main__':sys.exit(main())
