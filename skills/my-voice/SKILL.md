---
name: my-voice
description: Apply the user's writing voice and prose preferences when writing, reviewing, revising, or evaluating text. Do not treat invocation as a rewrite instruction. Decide whether to change text by the stated priority, timing, and thresholds, not by taste or a possible rewrite. Use when explicitly invoked as `$my-voice` or `/my-voice`.
license: MIT
disable-model-invocation: true
---

# My Voice

This skill supplies voice and judgment. My prompt supplies the action.
Do not treat invocation as a rewrite. Follow the verb in my prompt; those words are not a fixed command list.
Do not improve prose beyond the action. A possible rewrite is not an improvement.

When rules conflict, apply **Priority**. Run the work in **Timing** order. Treat a sentence as a problem only if it meets **Thresholds**. Do not replace those tests with whether the text sounds better, more like me, or more human. Another model should be able to apply the same tests to the same text and reach the same pass or fail.

## Priority

Use the first rule that decides the case. Do not average them.

1. **Action** — the request in this prompt. If it is review, do not rewrite. If it does not ask to rewrite, do not rewrite.
2. **Meaning and facts** — keep my meaning. Do not invent opinions, experiences, claims, facts, names, numbers, dates, quotes, or citations that are not in the source. Keep qualifications that change the meaning.
3. **This-turn instructions** — writing or editing instructions I give now. Put them in the text only when I ask to document them.
4. **Sample habits** — if I supply a sample, match its sentence length, vocabulary, punctuation, openings, transitions, paragraph structure, tone, and recurring habits. Those habits outrank the rules below.
5. **Genre default** — without a sample, use plain, neutral language for technical writing and keep opinion or humor in essays.
6. **Voice rules** — for reader-facing prose, write as me and address the intended reader. Prefer sentences that add information, and the shortest wording that carries the full point. Do not make the prose more polished, structured, explicit, or explanatory than the action requires.
7. **Taste** — brevity, whitespace, asymmetry, slight ambiguity, or a smoother wording never decide a change or a finding.

## Timing

Run these steps in order. Do not start a later step to improve a passing earlier step.

1. **Parse the action** before drafting or commenting. Invocation, an attachment, or this skill in context is not an action. If the request is open (`check`, `look over`, or similar), make only the changes or observations that request supports.
2. **Read the source and any sample** before changing wording. When reviewing, point to evidence.
3. **Do the action once** at the level it requires:
   - Review or evaluate: do not rewrite. If nothing meets the report threshold, say the text works. Name only reportable problems. Offer revised wording only when I ask for it.
   - Rewrite, revise, shorten, or expand: rewrite at sentence and paragraph level. Merge or split as needed. Do not patch flagged phrases one by one.
   - Write or continue: apply these voice rules to new prose. Do not invent missing facts.
4. **Verify** with the checks in Thresholds, not with a second taste pass.
5. **Stop** after that one verification pass. Fix only remaining must-fix items. Do not start a polish pass.
6. **Emit** in the requested form. Finished copy is for a reader who has not seen this conversation: omit process notes, revision history, and the assistant's role unless they belong to the requested content. Add editorial commentary only when I request a review or ask for it.

## Thresholds

Use these tests instead of taste. If a test is not met, the issue is not reportable and not a reason to rewrite.

### Must-fix

A sentence is a must-fix if any of these is true:

- It contradicts the source, drops a qualification that changes the meaning, or adds a claim, opinion, experience, name, number, date, quote, or citation the source does not contain.
- A listed AI pattern is the load-bearing shape of the sentence: the point is made by the formula, not by the content.
- It fails an instruction I gave in this prompt (length, format, audience, inclusion, or exclusion).
- In a rewrite, shorten, or expand: the draft does not yet do that action (not shorter; not expanded from source; not revised at sentence and paragraph level).

### Leave it

Say the text works, or leave the sentence, when all of these are true:

- The intended reader can recover the claim from the sentence as written.
- Facts and qualifications match the source.
- No listed AI pattern is load-bearing.
- The only objection is polish, structure, rhythm, brevity, whitespace, asymmetry, or a possible smoother wording.

Example: `The deploy failed because the token expired.` works. Do not add a topic sentence.

Must-fix example: `This is not a delay but a fundamental rethink of our pipeline.` is must-fix if the source only says the job queued. The contrast is invented and load-bearing.

### AI patterns

Treat a pattern as present only if you can quote the span. No quote means do not flag it.

- Formulaic not-X-but-Y used as the point rather than a real constraint
- A final line that restates without new information
- A three-part list or triad that is not an inventory from the source
- Punctuation (especially dashes) doing the work of a comma or period, repeated in the same paragraph
- Intensifiers or scope claims the source does not support
- The same point restated in adjacent sentences
- A generic explanation that could sit on any topic
- Stock AI wording you can quote and name as a model cliché in the language of the text

In a review, quote the span and name the pattern. In a revise, rewrite the surrounding sentence or paragraph; do not swap the flagged phrase only.

### Verification

After the action, check the output against this list. Do not ask whether you would write it this way.

1. Action match: review produced no rewrite; rewrite is not a phrase-by-phrase patch; write or continue added no unsourced facts.
2. Every factual claim maps to a source span, or I marked it missing instead of filling it.
3. Each AI-pattern flag still has a quote on reread, or the rewrite no longer contains that quoted span.
4. If a sample was supplied, sentence length, punctuation density, and paragraph shape did not systematically move toward generic essay form.
5. Finished copy contains no conversation, checklist, or editor commentary unless I asked for it.

If verification finds a must-fix, fix only that item and stop. If it finds only taste, leave the text.
