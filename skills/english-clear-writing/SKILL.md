---
name: english-clear-writing
description: >-
  Write or edit clear, natural English when English is the requested output,
  including replies, explanations, procedures, UI copy and translations.
  Preserve meaning, the target format and voice. English source material does
  not override a request for another output language.
license: MIT
metadata:
  version: "1.0-rc.5"
---

# English clear writing

Put precision first. Match the user's task, target language, format, length and voice. A simple exchange needs a natural answer. This skill does not authorize sending, publishing, approval or changes to the task.

## Shared constraints

- Never use an em dash (U+2014) in authored prose, headings, bullets, table cells or diagram labels. Do not imitate it with double or spaced hyphens. Recast with periods, commas, colons or parentheses; required literal quotations, code and exact tokens stay unchanged.
- Keep actors, recipients, ownership, authority, actions and completion states. Distinguish obligation, prohibition, permission, capability, advice, expectation and inference. Ask only when an unresolved reading materially changes the result.
- Preserve negation, limiting words, necessary conditions and exceptions. "Not all" permits no successes; "only if" does not require action whenever its condition holds. Keep optionality, concurrency and sequence distinct.
- Preserve attribution and evidence limits, including in headings. Unknown is not zero or failure. Not checked is not being checked. Missing confirmation does not establish that an action never happened. An attempt or plan is not completion.
- Keep exact numbers, units, denominators, deadlines and inclusive or exclusive endpoints. Distinguish percent from percentage points and paid amounts from full commitments. Preserve names, identifiers, keys, placeholders and required markup unless explicitly editable.
- Use idiomatic grammar and a consistent precise term. Do not invent an actor to force active voice or delete articles and helper words merely to shorten prose. Preserve pronouns, contractions, chosen English variety and deliberate creative effects.

## Readable structure and diagrams

Lead with the supported answer, state or action, placing its condition beside it. Let each block answer one useful question or support one action, normally in one or two short sentences. Separate distinct status, authority and next-action lookups, including within bullets and table cells.

Use concise bullets for parallel information and numbering for required order. Keep table cells to short comparable facts; use small sections for several sentences or different actors' tasks. There is no universal word cap, fixed template or required number of sections.

Proactively use small inline Mermaid diagrams for useful processes, handovers, architecture, data flow or meaningful choices. Expose gates, permissions and supported relationships without implying automatic approval or success. Preserve optional and concurrent work; distinguish current-case states from a general workflow. A simple personal reply usually needs no visual.

State the point directly. Remove inflated wording, technical-sounding metaphors, canned introductions, empty praise and generic endings. Keep real terminology, necessary uncertainty, warmth and requested creative effects.

## Read the relevant supporting guide

Load only material that helps the current request; do not read every reference or re-read unchanged material already in context.

- For substantive edits, grammatical ambiguity, modality, negation, conditions or numeric boundaries: [Meaning and grammar](references/meaning-and-grammar.md).
- For explanations, procedures, handovers, UI copy, localization, letters or creative writing: the relevant section of [Modes and examples](references/modes-and-examples.md).
- For substantive cleanup of inflated or awkward prose: [Editorial cleanup](references/editorial-cleanup.md).
- For lexical distinctions or exact JSON/token edits: [Lexicon and checks](references/lexicon-and-checks.md), then the relevant record in [lexicon.json](references/lexicon.json) or [rules.json](references/rules.json).

Worked edits and rule examples illustrate choices; they do not impose a response template. Use the sentence's context to choose a sense. An unlisted word is not forbidden.

## Optional local helpers

The bundled lookup and contract checker use Python 3.10+ and no external packages. Resolve paths relative to this skill folder.

```bash
python3 scripts/lookup.py lexicon 'must not' --exact --related
python3 scripts/lookup.py rules --id C05
python3 scripts/check_contract.py before.json after.json --json --simple-placeholders
```

The checker compares declared JSON structure, exact literal counts and simple `{identifier}` placeholders. It rejects unsupported placeholder syntax in that mode. It does not verify meaning, grammar, formatter behavior or accessibility; keep the source comparison.

## Final private check

Compare every requested item with the source and output contract, including subject lines, headings, labels, diagram nodes and arrows. Recheck boundaries and unknown states, exact tokens, grammar, authored punctuation and dense bullets or cells.

For a rewrite, translation or drafted message, return the requested text. For a public description, explain purpose and use. Add editorial process, test caveats, invocation mechanics, origin stories, implementation advice or maintainer notes only when asked; internal checks must not invent another assignment or product behavior.
