#!/usr/bin/env python3
"""Read the bundled editorial reference; never rewrite text or infer missing rules."""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
DATA={'rules':('rules.json','rules'),'lexicon':('lexicon.json','entries')}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('kind',choices=DATA)
    p.add_argument('query',nargs='?',help='Case-insensitive literal search; no stemming or synonym inference.')
    p.add_argument('--id',dest='entry_id',help='Find an exact stable ID, case-insensitively.')
    p.add_argument('--exact',action='store_true',help='Match a whole term/title; requires a query.')
    p.add_argument('--profile',choices=['core','grammar','profile','ui','evaluation'],help='Rules only.')
    p.add_argument('--related',action='store_true',help='Lexicon only: include the directly linked entries for returned matches.')
    p.add_argument('--limit',type=int,default=6,help='Maximum primary results (1-100); default 6.')
    args=p.parse_args()
    if not 1<=args.limit<=100:p.error('--limit must be between 1 and 100')
    if args.exact and not args.query:p.error('--exact requires a query')
    if args.profile and args.kind!='rules':p.error('--profile is for rules only')
    if args.related and args.kind!='lexicon':p.error('--related is for lexicon only')
    try:
        filename,key=DATA[args.kind]
        rows=json.loads((ROOT/'references'/filename).read_text(encoding='utf-8'))[key]
    except (OSError,ValueError,KeyError) as exc:
        print(json.dumps({'error':str(exc)}),file=sys.stderr);return 2
    selected=[]
    for row in rows:
        if args.entry_id and row['id'].casefold()!=args.entry_id.casefold():continue
        if args.profile and row.get('profile')!=args.profile:continue
        if args.query:
            query=args.query.casefold()
            if args.exact:
                text=row.get('term',row.get('title','')).casefold()
                if query!=text:continue
            elif query not in json.dumps(row,ensure_ascii=False).casefold():continue
        selected.append(row)
    returned=selected[:args.limit]
    result={'kind':args.kind,'query':args.query,'id':args.entry_id,
            'total_matches':len(selected),'returned':len(returned),
            'truncated':len(selected)>len(returned),'entries':returned,
            'scope':'Contextual editorial guidance, not a closed vocabulary or automatic replacement rule.'}
    if args.related:
        primary_ids={x['id'] for x in returned}
        related={item_id for x in returned for item_id in x.get('related',[])}-primary_ids
        result['related_entries']=[x for x in rows if x['id'] in related]
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0

if __name__=='__main__':sys.exit(main())
