# Meaning and English grammar

Use this guide for a substantive edit, ambiguous sentence or meaning-sensitive translation. For a particular output type, read the relevant part of [modes and examples](modes-and-examples.md).

Find a specific term or rule in the bundled [lexicon and checks](lexicon-and-checks.md). These references support the task; their headings and review notes do not belong in the reader's requested text.

## A meaning-preserving workflow

### Read the task before the sentence

Identify the requested output and its reader: a reply, revision, translation, explanation, procedure, interface string or creative piece. Determine which parts are editable.

A values-only JSON edit leaves the keys unchanged. If a quotation must stay exact, edit the surrounding prose instead.

Resolve ordinary stylistic choices from context. Ask one focused question when an unresolved reading would materially change an actor, permission, quantity, time or result.

### Keep a private meaning record for substantial edits

| Invariant | What to identify |
| --- | --- |
| Participants | Actor, recipient, owner, affected group and each stated role |
| Action and state | Planned, attempted, ongoing or completed action |
| Modality | Requirement, prohibition, permission, capability, advice or inference |
| Negation | The exact claim, action or quantity being negated |
| Time | Moment, duration, sequence, deadline and supplied time zone |
| Quantity | Number, unit, denominator, population and endpoints |
| Conditions | Prerequisites, exceptions and unknown conditions |
| Evidence | Who reports the result and what was actually checked |
| Output contract | Target language, format, voice, length and protected strings |

The record is an editing aid, not a required section in the answer. Show it only when the user asks for an audit or a material unresolved issue needs explaining.

### Rewrite, then compare

1. Identify the reader's immediate need. Put the supported answer, request or current state where the reader will look first.
2. Keep a necessary condition, exception or evidence limit beside its claim. Review headings, subject lines and labels as well as body text.
3. Remove a real obstacle: ambiguity, poor order, unnecessary complexity or incorrect grammar. Keep wording that is already clear and accurate.
4. Compare against the source, including diagram labels and arrows. Try a boundary case that separates the meanings: exactly 10 files, no completed jobs, two possible owners or a check that never finishes.
5. Check structure and protected tokens separately from meaning. Inspect small blocks, bullets and table cells for independently useful information that has been bundled together.

A later caveat cannot repair an overstated headline. A shorter sentence that changes a permission is a failed edit; a longer sentence may be needed to keep an exception.

One meaning record can support several deliverables. Compare each email, summary and UI string with the source again because compression can drop attribution or turn uncertainty into reassurance.

## English grammar that affects meaning

### Actors, voice and ownership

Active voice often makes responsibility visible: "Noor approved the refund." Passive voice can fit an unknown actor or a sentence about the affected object: "The folder was renamed yesterday."

Do not rewrite the second sentence as "You renamed the folder yesterday" unless the actor is known. A form of "be" is not automatically passive: "The folder is empty" states a condition.

Keep each actor attached to the stated action. Delivering an item does not establish who supplied, paid for or owns it.

"Mira delivered the boxes, not Leo" contrasts the delivery actors. It does not establish who supplied the boxes or why Leo did not deliver them.

"Maya sent Noor her draft" can leave the owner unclear. Ask whose draft it was before replacing "her" with Maya's or Noor's name if ownership affects the task.

Preserve stated pronouns and intentional personal voice. Singular "they," conversational phrasal verbs and a chosen English variety are not errors merely because another style is more formal.

### Articles and countability

Articles help identify the referent. "Open a draft" allows an unspecified draft; "open the draft" points to an identifiable one.

The reader may identify "the draft" from the situation even on its first mention. Do not apply a mechanical rule that "a" always means first mention and "the" always means second mention.

"We received an update" introduces an update. "We received the update" can refer to an expected or identifiable update; removing the article to save a word may lose that distinction.

Check a noun's intended sense before changing countability. Ordinary "information" takes forms such as "some information" or "a piece of information," rather than "informations."

An exact identifier named `informations` remains unchanged. A button such as "Open draft" can use a compact interface convention without making the same fragment suitable for a prose paragraph.

### Agreement and parallel structure

Find the grammatical subject after restructuring. In "Each of the files is ready," "each" controls the singular verb, not the nearby plural "files."

Keep the user's established variety and treatment of collective nouns. Do not present one regional choice as the only grammatical English form.

Parallel actions are easy to follow: "Open the draft, check the totals, and save the file." Preserve an important difference between an action and a state rather than forcing every item into the same grammatical form.

If a list combines responsibilities, keep each actor explicit. "Check the totals" must not replace "The reviewer checks the totals" in a handover addressed to a different person.

### Relative clauses and commas

A defining clause identifies the intended referent or subset. A non-defining clause adds information about an already identified referent and is set off by commas.

| Sentence | Scope |
| --- | --- |
| The accounts that are inactive will be archived. | Selects inactive accounts |
| The accounts, which are inactive, will be archived. | Describes the referenced accounts as inactive |

Adding commas can change which accounts the instruction covers. Resolve the intended set before polishing the punctuation.

Restrictive "which" is possible in English. A preference for restrictive "that" can be a house style; do not label every restrictive "which" a grammar error.

Do not use "that" to introduce a non-defining clause. Preserve the clause's meaning when changing its pronoun or punctuation.

### Tense, aspect and result

| Wording | What it establishes |
| --- | --- |
| We tested the export. | A test occurred |
| We have tested the export. | A test occurred with present relevance |
| We have been testing the export. | Testing activity continued over a period |
| We will test the export. | A future test is stated |
| We plan to test the export. | A plan is stated |

None of these phrases alone establishes that the export passed. Keep a test's criterion and outcome when the source supplies them.

Present-perfect forms connect earlier events or states with a reference time. They do not automatically certify completion or success, and the continuous form does not by itself prove that the activity is still running now.

Present tense can describe general behavior. Future tense matters when it distinguishes a delayed operation: "The file will be archived on the next run" must not become "The file is archived."

Keep "already," "still" and "yet" when they contribute timing or expectation. "The report is not ready yet" does not mean it will be ready by a particular deadline.

### Limiting words, modifiers and noun stacks

"Only Nina can approve refunds" restricts the approver. "Nina can only approve refunds" may restrict Nina's activities instead; put the limiting word where its intended scope is clear.

Do not soften a stated restriction into merely usual behavior. "Only Nina may approve" cannot become "Nina usually approves" without changing authority.

Unpack a noun stack such as "customer account deletion request history" only after identifying the relationships. Is it the history of requests to delete customer accounts, or a history belonging to a particular customer?

Keep helpful words such as "that," "the," "if" and "by" when they make a relationship explicit. A lower word count does not justify obscuring who acts on what.

### Connectors and small grammatical distinctions

"Since" can express a starting time or a reason. "While" can express simultaneous time or contrast; do not choose a causal or temporal rewrite without context.

"The queue grew. The worker restarted" does not establish a cause or order. Adding "therefore" or "then" would add a relationship the source has not supplied.

"Its" is possessive. "It's" can mean "it is" or "it has"; correct prose when needed while preserving exact identifiers and protected quotations.

Use "log in" as a verb phrase when that is the intended action. Keep actual UI labels, commands and identifiers even when their spelling differs from ordinary prose.

## Semantic traps

### Modal verbs are not interchangeable

| Source | Meaning in this context | Unsafe replacement |
| --- | --- | --- |
| You must not restart. | Prohibition | You do not have to restart. |
| You do not have to restart. | No restart requirement | You must not restart. |
| It should finish soon. | Expectation | It will finish soon. |
| Someone must be inside. | Strong inference | Someone is required to be inside. |

Identify the contextual function before paraphrasing. "Must" can express obligation or inference; "should" can express advice or expectation.

"May" can mark permission or possibility. "May not" can express a prohibition or possible non-occurrence, so "The archive may not be ready" must not become "The archive must not be ready."

"Can" can express capability, permission or general possibility. "Editors cannot rename files" does not identify whether a technical limit or an authorization rule prevents the action unless the source explains it.

In a permission-sensitive context, "not required" alone does not establish every permission affecting the action. Do not assign invented probabilities or confidence percentages to "may," "should" or "must."

### Negation and quantifiers

"Not all three uploads finished" allows zero, one or two completed uploads. The plain rewrite "At least one of the three uploads did not finish" preserves that range.

| Wording | Possible completed count out of three |
| --- | --- |
| Not all finished. | 0, 1 or 2 |
| Some finished and some did not. | 1 or 2 |
| None finished. | 0 |
| All finished. | 3 |

Do not change "not all" to "some succeeded" because that excludes zero successes. Keep the relevant group explicit when "none" or "all" might refer to different sets.

"The change has not been shown to be unsafe" does not establish safety. "The test was not run" does not mean that it failed.

Missing confirmation does not establish that the action never happened. "We have no booking confirmation" must not become "Nothing has been booked," including in a heading.

Unknown counts are not zero. An unsupported check, absent observation or unanswered request cannot supply a result through smoother wording.

### Conditions, alternatives and exceptions

"Publish only if the review passes" makes a pass necessary. It does not require publication after every pass or establish other publication permissions.

"Publish if the review passes" supplies a conditional instruction. "You may publish if the review passes" supplies conditional permission; preserve that modal difference.

If a source uses "if and only if," preserve both directions of the stated relationship. Do not add the reverse implication to an ordinary "if" or "only if."

"If" can also introduce an indirect question or polite request. Determine its function in the sentence rather than treating every occurrence as a formal process gate.

"Keep the draft unless the owner requests deletion" supplies an exception to keeping it. The sentence alone does not establish a whole deletion policy or unrelated deletion authority.

Check whether "or" allows both alternatives when the choice affects behavior. If both are confirmed, write "email, SMS, or both"; if exactly one is confirmed, write "either email or SMS, but not both."

Do not infer exclusivity merely from an "either ... or" construction. Use the source's actual rule when exclusivity matters.

### Time and numeric boundaries

"Do not submit until the check finishes" prohibits submission before the event. It neither promises that the check will finish nor requires submission afterward.

"Send it by Friday" may be adequate in ordinary conversation. For an exact cutoff, preserve the supplied time and time zone or ask for them when the distinction matters.

| Expression | Endpoint |
| --- | --- |
| At most 10; no more than 10 | Includes 10 |
| Fewer than 10; less than 10 | Excludes 10 |
| At least 10; no fewer than 10 | Includes 10 |
| More than 10 | Excludes 10 |

Use count and measure wording naturally, but keep the mathematical boundary. "Choose a file that is 10 MB or smaller" must not become "Choose a file smaller than 10 MB."

State what a limit counts. A limit of three total attempts including the first permits two retries; it is not a limit of three retries.

Preserve the numerator, denominator, population and period. "20% of reviewed cases" is not "20% of all cases" unless the reviewed set is the whole set.

A change from 10% to 15% is an increase of 5 percentage points. Relative to 10%, the increase is 50%.

"Twice the original value" means the original multiplied by two. An "increase of 200%" means three times the original value.

Keep paid amounts separate from commitments. If a total commitment is 510 and 170 has been paid, the unpaid part is 340; subtracting only the paid amount from a budget does not establish the budget available after all commitments.

Check calculations and conversions separately from wording. Do not silently round exact numbers or convert units, currencies or ambiguous dates because the surrounding text changes language.

Arithmetic can reveal a supported gap without creating a new policy or commitment. A quote exceeding the remaining budget by 25 does not establish permission to spend another 25.

## Keep evidence and proposals distinct

Preserve who supplied each claim and what the check actually covered. "The vendor reports a fix" remains an attributed report until the source supplies a stronger result.

Use "tested," "verified" and "validated" with their actual scope. A test performed locally does not become a production result; a syntax check does not become a meaning check.

Keep source facts, checked consequences and proposed arrangements distinguishable. A request for a carrier's written confirmation is neither confirmation received nor a booking commitment.

Retain the specific unknown instead of stacking vague hedges. A clean sentence can say "The delivery status is unknown" without inventing a cause, active investigation or reassurance.

## Final comparison

Can the reader identify the intended actor, action, condition and result? Check subject lines, headings, labels, diagram nodes and arrows for the same limits as the body.

Keep the requested language, voice and protected strings. Return the requested text; do not append this private review or a new implementation assignment.
