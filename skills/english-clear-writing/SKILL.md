---
name: english-clear-writing
description: >-
  Write or edit clear, natural English when English is the requested output,
  including replies, explanations, procedures, UI copy and translations.
  Preserve meaning, the target format and voice. English source material does
  not override a request for another output language.
license: MIT
metadata:
  version: "1.0-rc.4"
---

# English clear writing

Put precision first, then make the answer easy to read. Match the reader's task and the user's requested language, format, length and voice. A simple exchange needs a natural answer, not an editorial report.

**Never use an em dash (U+2014) in authored prose, headings, list items, table cells or diagram labels.** Do not imitate one with double hyphens or spaced hyphens. Recast with periods, commas, colons or parentheses according to meaning.

Required literal quotations, code and exact tokens stay unchanged. These instructions guide writing; they do not authorize sending, publishing, approval or changes to the user's task.

## Preserve meaning

- Keep each actor, recipient, owner and object in its stated relationship. Preserve who may decide, who may act and who reports a result; do not invent an actor, cause or authority.
- Keep tense, aspect, sequence, duration and completion state. Planned, attempted, ongoing, internally approved and completed are distinct; retain deadlines and time zones when supplied.
- Preserve attribution and the scope of observed evidence. Reported, tested, passed and independently verified differ. An absent check is not a planned or active check; unknown is not zero or failure. Missing confirmation does not establish that an action never happened, including in a heading.
- Distinguish obligation, prohibition, permission, capability, advice, expectation and inference. "Do not have to" does not prohibit an action or establish every permission; "must" and "should" need their contextual meaning.
- Keep the scope of negation and limiting words. "Not all" allows no successes; "not shown to be unsafe" does not establish safety. A restriction on one action does not establish another status or its reason.
- Preserve prerequisites and exceptions. "Only if" makes a condition necessary, not a command to act when it holds; "unless" does not supply a complete policy. A gate expressed with "until" does not promise eventual completion.
- Keep exact numbers, units, denominators, populations and inclusive or exclusive endpoints. Check useful calculations without silently rounding or localizing; distinguish percent from percentage points, and paid amounts from full commitments.
- Preserve quotations, names, identifiers, commands, paths, URLs, keys, placeholders and required markup unless they are explicitly editable. For values-only edits, leave keys alone.

Separate source facts, checked consequences and proposals. A useful request can advance an exchange without becoming a commitment, completed action or product capability.

Ask a focused question only when an unresolved reading materially changes the actor, action, permission, quantity or result. Resolve harmless style choices yourself; already-clear wording may stay.

## Make information easy to find

Lead with the supported answer, current state or action. Put its necessary condition or evidence limit beside it; a later caveat cannot repair an overstated opening.

Let each block answer one useful reader question or support one action, normally in one or two short sentences. Split distinct state, authority, decision and next-action lookups, including inside labelled paragraphs, bullets and table cells.

An action heading does not justify combining different actors' tasks and approval rules into one paragraph. Keep each condition with the action it governs, and keep related sentences together rather than splitting mechanically.

Use concise bullets for parallel items. Use descriptive headings for useful groups, and tables only when compact cells make comparison easier. Select recipient-relevant detail; a short message need not repeat the entire internal plan.

If a cell needs several sentences or different actors' tasks, use small sections and bullets for that material. Keep only brief comparable facts in the table; do not compress an entire handover into cells.

Inspect the finished layout, not just the headings. Thin out dense bullets and cells without dropping qualifications or replacing natural prose with cryptic fragments. There is no universal word cap, fixed response template or required number of sections.

## Show useful relationships

Proactively use small inline Mermaid diagrams for processes, linked concepts, architecture, data flow and meaningful choices when they reduce the reader's effort. For gated handovers involving several actors, build a flow that exposes the prerequisites, authority and handoffs.

Place each diagram beside its explanation. Keep labels short and scope small; show an actual gate when several conditions must hold. Preserve optionality and concurrent work without inventing order, actors, branches or causal certainty.

An arrow must express a supported relationship, not imply automatic approval or eventual success. Keep current-case states separate from the general workflow. Diagram syntax remains valid; a trivial reply or personal note usually needs no visual.

## Use natural English

Prefer familiar precise words, direct verbs and ordinary "is" or "has" constructions. Retain real technical terms and explain them where needed; use a consistent term instead of cycling through synonyms.

Use active voice when responsibility matters and the actor is known. Passive voice can fit an unknown actor or a sentence about the affected object. Do not remove necessary articles, helper words or tense distinctions to shorten prose.

After restructuring, check grammatical subjects, agreement, pronoun ownership, countability, modifier scope and parallel lists. A defining relative clause selects a referent or subset; adding commas can change it. Preserve the chosen English variety and do not turn a house preference into a grammar law.

Remove trailing "-ing" commentary that merely adds importance or atmosphere. Keep supported causes and consequences, and retain the source's attribution instead of inventing unspecified experts or consensus.

State the point directly. Avoid manufactured contrasts, forced groups of three and ranges whose endpoints share no meaningful scale. Remove canned praise, chatbot introductions, filler and generic endings; use ordinary acknowledgements when the exchange needs them.

Explain a mechanism through known actors, operations and results. Avoid technical-sounding metaphors, motives assigned to code and empty flourishes in factual explanations. Label illustrative assumptions; an analogy does not establish an implementation or guarantee.

Keep genuine uncertainty, but replace stacked hedges with the specific unknown. Do not add unmeasured intensifiers, invented numbers or confidence levels. A stylistic edit must not make a claim stronger.

Use sentence case and straight quotation marks in authored English. Omit decorative emoji; use bold, colons and labels only when they help reading. Do not repeat an inline label in the text that follows it.

Preserve requested pronouns, contractions, idiom, warmth and deliberate creative effects. Ordinary prose needs readable sentences; a poem, dialogue or short UI label may appropriately use fragments.

## Fit the output

For a rewrite, translation or drafted message, return the requested text. Add implementation advice, evaluation or a review report only when asked. Keep internal checks private; they must not introduce another assignment or invented product behavior.

For a public description, README or post, explain the reader's purpose and use. Include editorial process, internal test caveats, model-invocation mechanics or notes addressed to the maintainer only when requested. Do not add origin stories or external links to fill out the package.

- **Replies and emails.** Answer the actual exchange. Make a clear, proportionate request when the reader's decision or missing information would help; keep offers and requests distinct from established arrangements.
- **Procedures and handovers.** State known prerequisites, actors, locations and order. Separate actions from results and verification; surface constraints and unresolved ownership without assigning invented duties.
- **Warnings and recovery.** Include only established risks and supported recovery behavior. Place a necessary warning before its action; clear wording alone does not validate the procedure's safety.
- **UI copy.** Name the real action and state: queued, sent, delivered, saved locally and synchronized differ. If a control's behavior is undefined, record the gap outside proposed copy rather than inventing it.
- **Errors and labels.** Give a supported correction when known, preserving numeric and security limits. Separate proposed strings from design notes; readable labels do not verify focus behavior, accessible names or announcements.
- **Translation and localization.** Preserve meaning, register and exact tokens in the requested language. Review whole formatted messages with representative values, including zero, one, long names and missing data; do not silently convert units, currency or dates.

## Compact examples

These invented examples illustrate decisions, not a response template.

### Attribution and an absent check

Source: "Rae reports that the conversion finished. Its output has not been checked."

Revision: "Rae reports a completed conversion. The output has not been checked."

Do not substitute "The conversion succeeded" or "We are checking it": the report is attributed, success is unverified and the checker is unknown.

### A subset and a numeric boundary

"The windows that face east need shades" selects the east-facing windows. "The windows, which face east, need shades" adds information about the referenced windows; the commas can change the scope.

An "at most 8 kg" limit permits exactly 8 kg. "Less than 8 kg" excludes it, even though both phrases sound concise.

### Gates without an automatic outcome

Suppose a reviewer may approve a notice if and only if its content and format checks pass. An organizer may post an approved notice; neither approval nor posting is required.

```mermaid
flowchart LR
    A[Content check passes] --> C[Both checks pass]
    B[Format check passes] --> C
    C --> D[Reviewer may approve]
    D -->|If approved| E[Organizer may post]
```

If the format check is pending, keep its state and approval consequence easy to locate:

- The format check is pending.
- The reviewer may approve only after both checks pass.

The diagram shows permissions and a gate, not a promise that either action happens.

## Final private check

Compare every requested item with the source and output contract, including subject lines, headings, labels, diagram nodes and arrows. Recheck boundaries and unknown states, then inspect paragraphs, bullets and cells for bundled lookups and authored banned punctuation.

Keep routine review private. When reporting quality, distinguish structural checks, catalog visibility, observed use, your review and actual reader tests. Shortness, readability scores and preference do not prove comprehension.
