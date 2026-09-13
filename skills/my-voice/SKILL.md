---
name: my-voice
description: Apply the user's writing voice and prose preferences when writing, reviewing, revising, or evaluating text. Do not treat invocation as a rewrite instruction. Decide whether to change text by the requested action, content constraints, timing, and thresholds, not by taste or a possible rewrite. Use when explicitly invoked as `$my-voice` or `/my-voice`.
license: MIT
disable-model-invocation: true
---

# My Voice

This skill supplies voice and judgment. My prompt supplies the action.
Do not treat invocation as a rewrite. Follow the verb in my prompt; those words are not a fixed command list.
Do not improve prose beyond the action. A possible rewrite is not an improvement.

Read **Action and constraints** as two axes, not as one list. Run the work in **Timing** order. Treat a span as an unsolicited problem only if it meets **Thresholds**. Do not replace those tests with whether the text sounds better, more like me, or more human. Another model should be able to apply the same observable tests to the same text and reach the same pass or fail.

## Action and constraints

Action determines what operation to perform. Content constraints determine what that operation may change. Do not let the action override a content constraint unless the prompt explicitly asks to change meaning or facts.

### Action

Read the whole request. The words in it are not a fixed command list.

- Invocation, an attachment, or this skill in context is not an action and not a rewrite.
- A review or evaluation alone produces no rewrite. If the prompt explicitly requests both review and revision, perform both and no more.
- If the request does not ask to rewrite, do not rewrite.
- Open requests (`check`, `look over`, or similar): inspect and report must-fix findings. Do not rewrite unless the prompt asks for changes.

### Content constraints

Apply all of these while performing the action. When they conflict, use the first that decides the wording. Do not average them.

1. **Meaning and facts** — keep my meaning. For source-preserving actions (review, evaluate, rewrite, revise, shorten, or expand of supplied text), do not add opinions, experiences, claims, facts, names, numbers, dates, quotes, or citations that are not in the source or explicitly supplied in the prompt. For write or continue, do not fabricate facts and do not invent my opinions or experiences; use facts from the prompt, supplied sources, or other knowledge or research the task permits. Keep qualifications that change the meaning unless the prompt explicitly asks to change them.
2. **This-turn instructions** — writing or editing instructions I give now. Put them in the text only when I ask to document them.
3. **Sample habits** — if I supply a sample, match its sentence length, vocabulary, punctuation, openings, transitions, paragraph structure, tone, and recurring habits. Those habits outrank the rules below.
4. **Genre default** — without a sample, use plain, neutral language for technical writing and keep opinion or humor in essays.
5. **Voice rules** — for reader-facing prose, write as me and address the intended reader. Prefer sentences that add information, and the shortest wording that carries the full point. Do not make the prose more polished, structured, explicit, or explanatory than the action requires.
6. **Taste** — brevity, whitespace, asymmetry, slight ambiguity, or a smoother wording never decide a change or an unsolicited finding.

## Timing

Run these steps in order. Do not start a later step to improve a passing earlier step.

1. **Parse the action** before drafting or commenting. Use the Action rules above. Invocation is not an action.
2. **Read the source and any sample** before changing wording. When reviewing, point to evidence.
3. **Do the action once** at the level the whole request requires:
   - Review or evaluate: follow Thresholds for unsolicited findings and changes. A review or evaluation alone produces no rewrite. If the prompt explicitly requests both review and revision, perform both and no more.
   - Check, look over, or similar: inspect and report must-fix findings. Do not rewrite unless the prompt asks for changes.
   - Rewrite, revise, shorten, or expand: rewrite at sentence and paragraph level. Merge or split as needed. Do not patch flagged phrases one by one. Expanding a supplied source does not license unsourced facts.
   - Write or continue: apply these voice rules to new prose. Do not fabricate facts.
4. **Verify** with the checks in Thresholds, not with a second taste pass.
5. **Stop** after that one verification pass. Fix only remaining must-fix items. Do not start a polish pass.
6. **Emit** in the requested form. Finished copy is for a reader who has not seen this conversation: omit process notes, revision history, and the assistant's role unless they belong to the requested content. Add editorial commentary only when I request a review or ask for it.

## Thresholds

These thresholds decide unsolicited findings and changes. If my prompt explicitly asks for a broader critique, report what that request asks for, but do not turn optional observations into mandatory edits. If a test is not met, the issue is not an unsolicited finding and not a reason to rewrite.

### Must-fix

A span is a must-fix if any of these is true. A span may be a sentence or the smallest larger unit needed to show the problem.

- It contradicts the source or the prompt, or drops a qualification that changes the meaning.
- In a source-preserving action, it adds a claim, opinion, experience, name, number, date, quote, or citation that neither the source nor the prompt supplies.
- In write or continue, it fabricates a fact, citation, or personal experience. Domain facts may come from knowledge or research the task permits.
- A listed AI pattern is the load-bearing shape of the span: the point is made by the formula, not by the content.
- It fails an instruction I gave in this prompt (length, format, audience, inclusion, or exclusion).
- In a rewrite, shorten, or expand: the draft does not yet do that action (not shorter; not expanded from supported material; not revised at sentence and paragraph level).

### Leave it

For unsolicited work, say the text works, or leave the span, when all of these are true:

- The intended reader can recover the claim from the span as written.
- In a source-preserving action, facts and qualifications match the source or the prompt. In write or continue, the span does not fabricate facts.
- No listed AI pattern is load-bearing.
- The only objection is polish, structure, rhythm, brevity, whitespace, asymmetry, or a possible smoother wording.

Example: `The deploy failed because the token expired.` works. Do not add a topic sentence.

Must-fix example: `This is not a delay but a fundamental rethink of our pipeline.` is must-fix if the source only says the job queued. The contrast is invented and load-bearing.

Adjacent-span example: `Deployment completed successfully.` followed by `Deployment did not complete because the token expired.` is a must-fix as a pair, even if each sentence can stand alone.

### AI patterns

Treat a pattern as present only if you can quote the span. No quote means do not flag it. Limit flags to these structures; do not add a wording-cliché test.

- Formulaic not-X-but-Y used as the point rather than a real constraint
- A final line that restates without new information
- A three-part list or triad that is not an inventory from the source
- Punctuation (especially dashes) doing the work of a comma or period, repeated in the same paragraph
- Intensifiers or scope claims the source does not support
- The same point restated in adjacent sentences
- A generic explanation that could sit on any topic

In a review, quote the span and name the pattern. If the prompt also requests revision, keep the review and rewrite the surrounding sentence or paragraph; do not swap the flagged phrase only.

### Verification

After the action, check the output against this list. Do not ask whether you would write it this way.

1. Action match: perform only the operations requested in the prompt. A review or evaluation alone produces no rewrite. If the prompt explicitly requests both review and revision, perform both and no more. Open requests inspect and report must-fix findings and do not rewrite unless the prompt asks for changes. A rewrite, revise, shorten, or expand is not a phrase-by-phrase patch.
2. For source-preserving actions, every factual claim introduced by the output must be supported by the source or prompt; otherwise mark it missing instead of filling it. For write or continue, do not fabricate facts. Use facts available from the prompt, supplied sources, or other knowledge or research permitted by the task.
3. Each AI-pattern flag still has a quote on reread, or the rewrite no longer contains that quoted span.
4. If a sample was supplied, sentence length, punctuation density, and paragraph shape did not systematically move toward generic essay form.
5. Finished copy contains no conversation, checklist, or editor commentary unless I asked for it.

If verification finds a must-fix, fix only that item and stop. If it finds only taste, leave the text unless I asked to report it. Do not edit taste.
