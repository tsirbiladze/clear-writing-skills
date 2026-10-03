# Lexicon and protected-text checks

Use a lookup when a word or phrase can change the intended meaning. Use a contract check when a rewrite must preserve structured values, simple placeholders or exact strings.

The [lexicon](lexicon.json) contains 32 contextual entries. The [rules](rules.json) contain 32 editing rules with boundaries and examples; neither file is a closed vocabulary or an automatic replacement list.

For whole-sentence decisions, read [meaning and grammar](meaning-and-grammar.md). For UI text, translation and other output types, read the relevant section of [modes and examples](modes-and-examples.md).

## Contextual lookup

Run the bundled [lookup helper](../scripts/lookup.py) from the skill directory. Replace the example query with the relevant term or use a stable rule ID.

```bash
python3 scripts/lookup.py lexicon "only if" --exact --related
python3 scripts/lookup.py lexicon --id L15
python3 scripts/lookup.py rules --id C07
python3 scripts/lookup.py rules --profile grammar --limit 6
```

Search is case-insensitive and literal. It does not stem words, infer synonyms, rewrite text or decide the intended meaning.

- `--id` selects a stable ID, ignoring case.
- `--exact` matches a whole term or rule title and requires a query.
- `--related` includes directly linked lexical entries.
- `--profile` filters rules; it does not filter lexical entries.
- `--limit` caps primary results. Check `total_matches` and `truncated` before assuming every match is shown.

Read the entry's warning and example in context. Related words express useful distinctions, not interchangeable synonyms.

Useful groups include:

| Question | Terms to inspect |
| --- | --- |
| Requirement or permission? | must, must not, do not have to, should, may, can |
| What condition applies? | only if, unless, until, or |
| What quantity is allowed? | not all, none, at most, fewer than, at least |
| What was established? | verify, validate, unknown, tested |
| What state or action is real? | queued, sent, delivered, delete, remove, archive, reset |

The entries for "percentage point," "the," "since," "while," "log in" and "its / it's" address specific numeric or grammatical distinctions. Do not load the entire lexicon for a simple reply.

## Compare the declared contract

The [contract checker](../scripts/check_contract.py) reads two UTF-8 files and does not modify them. Select the checks that actually apply to the requested edit.

```bash
python3 scripts/check_contract.py before.json after.json --json --simple-placeholders
python3 scripts/check_contract.py before.txt after.txt --literal "{file_name}"
python3 scripts/check_contract.py before.txt after.txt --literal "DELETE" --literal "/reports/current"
```

`--json` permits string-value edits while checking recursive keys, array lengths, value types and non-string values. JSON object key order is not protected; duplicate keys and nonstandard JSON constants are rejected.

`--simple-placeholders` compares occurrence counts of `{identifier}` placeholders separately in each JSON string. For plain text, it compares counts across the whole file.

This placeholder mode rejects common unsupported formats such as ICU plural/select messages, mustache and `${...}`. It does not parse every template language; use the actual formatter for complex messages.

For other formats, omit that flag and declare exact `--literal` values when useful. Each declared literal must occur in the original file, and the checker compares its raw occurrence count.

A literal-count match does not verify where the literal is used. Manually check that a key's placeholder, command, name or path still belongs to the correct instruction or message.

| Exit code | Result |
| --- | --- |
| 0 | Selected mechanical checks passed |
| 1 | A selected property changed |
| 2 | Invalid input or unsupported selected syntax |

An unsupported result is not a clean check. Correct the input or use a checker suited to that format; do not ignore the result and claim the contract was preserved.

## Finish with a meaning check

These tools do not check semantic equivalence, target language, grammar, readable layout or runtime formatting. A mechanically valid rewrite can still change who may act, omit a condition or confuse a total-attempt limit with a retry count.

Compare the final text with the source and the requested format. Keep the tool output and routine review private unless the user requests a technical report.
