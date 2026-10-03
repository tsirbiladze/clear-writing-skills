#!/usr/bin/env python3
"""Read-only Georgian sense/rule lookup. Python 3.10+, standard library only.

Exact headword, explicit example form, ID, or literal substring search.
No morphology, automatic replacement, external access, or file writes.
"""
import argparse
import json
from pathlib import Path
import re
import unicodedata


def normalize(value):
    return unicodedata.normalize('NFC', value).casefold().strip()


def positive_limit(value):
    try:
        n = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError('limit must be an integer') from exc
    if not 1 <= n <= 400:
        raise argparse.ArgumentTypeError('limit must be between 1 and 400')
    return n


def select_records(kind, records, query='', record_id=None, profile=None,
                   exact=False, form=False, include_deprecated=False):
    query = normalize(query)
    selected = []
    for item in records:
        if record_id and item['id'].upper() != record_id.strip().upper():
            continue
        if (kind == 'lexicon' and item.get('status', '').startswith('deprecated')
                and not (include_deprecated or record_id)):
            continue
        if profile:
            if kind == 'lexicon' and profile not in item['profiles']:
                continue
            if kind == 'rules' and item['id'][0] not in ('C', 'G', profile):
                continue
        if query:
            if form:
                hit = bool(item.get('representative_form')) and normalize(item['representative_form']) == query
            elif exact:
                hit = normalize(item['term'] if kind == 'lexicon' else item['title']) == query
            else:
                fields = ('term', 'sense_id', 'meaning', 'example', 'representative_form', 'usage_note') if kind == 'lexicon' else ('title', 'body_markdown')
                hit = any(query in normalize(item.get(f, '')) for f in fields)
            if not hit:
                continue
        selected.append(item)
    return selected


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=('lexicon', 'rules'))
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--id', dest='record_id', help='Exact Lnnn or C/G/T/A/Unn code')
    parser.add_argument('--profile', type=str.upper, choices=('T', 'A', 'U'))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--exact', action='store_true', help='Exact headword/title, not inflection search')
    mode.add_argument('--form', action='store_true', help='Exact explicitly listed representative form; lexicon only')
    parser.add_argument('--related', action='store_true', help='Include related/replacement lexicon records separately')
    parser.add_argument('--include-deprecated', action='store_true')
    parser.add_argument('--limit', type=positive_limit, default=8)
    args = parser.parse_args(argv)
    if (args.exact or args.form) and not args.query.strip():
        parser.error('--exact and --form require a text query')
    if args.record_id and args.query.strip():
        parser.error('use an ID or a text query, not both')
    if args.kind == 'rules' and (args.form or args.related or args.include_deprecated):
        parser.error('--form, --related and --include-deprecated apply only to lexicon')
    if args.record_id and not re.fullmatch(r'L\d{3}' if args.kind == 'lexicon' else r'[CGTAU]\d{2}', args.record_id.strip().upper()):
        parser.error('ID does not match the selected kind')
    root = Path(__file__).resolve().parents[1]
    source = root / 'references' / f'{args.kind}.json'
    try:
        data = json.loads(source.read_text(encoding='utf-8'))
        version = data['version']
        records = data['entries' if args.kind == 'lexicon' else 'rules']
        matches = select_records(args.kind, records, args.query, args.record_id,
                                 args.profile, args.exact, args.form, args.include_deprecated)
        shown = matches[:args.limit]
        related_ids = {id for item in shown for id in item.get('related_ids', []) + item.get('replacement_ids', [])}
        related = [item for item in records if item['id'] in related_ids and item['id'] not in {x['id'] for x in shown}] if args.related else []
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(1, f'Cannot read bundled {args.kind} data: {exc}\n')
    result = {
        'kind': args.kind, 'version': version, 'query': args.query or None,
        'id': args.record_id, 'profile': args.profile,
        'match_mode': 'id' if args.record_id else ('explicit_form' if args.form else ('exact_title' if args.exact else 'literal_substring')),
        'total_matches': len(matches), 'returned': len(shown), 'truncated': len(matches) > args.limit,
        'results': shown, 'related_results': related,
        'warnings': ['Selected record is archived; use its replacement IDs.'] if any(x.get('status', '').startswith('deprecated') for x in shown) else [],
        'scope': 'Editorial proposals. No-match is not a prohibited-word decision. Explicit forms are examples, not a morphology model. Choose a sense from sentence context; no automatic replacement.'
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
