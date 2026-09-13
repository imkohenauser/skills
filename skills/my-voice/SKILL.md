---
name: my-voice
description: Apply the user's writing voice and prose preferences when writing, reviewing, revising, or evaluating text. Do not treat invocation as a rewrite instruction. Decide changes by the requested action, content constraints, timing, and thresholds, not by taste. Use when explicitly invoked as `$my-voice` or `/my-voice`.
license: MIT
disable-model-invocation: true
---

# My Voice

This skill supplies voice and judgment. My prompt supplies the action.
Do not treat invocation as a rewrite. Follow the verb in my prompt; those words are not a fixed command list.
Do not improve prose beyond the action. A possible rewrite is not an improvement.

Use **Action and constraints**, **Timing**, and **Thresholds**. Another model should reach the same pass or fail on the same observable tests.

## Action and constraints

Action determines what operation to perform. Content constraints determine what that operation may change. Do not let the action override a content constraint unless the prompt explicitly asks to change meaning or facts.

### Action

- Invocation, an attachment, or this skill in context is not an action and not a rewrite.
- A review or evaluation alone produces no rewrite. If the prompt explicitly requests both review and revision, perform both and no more.
- Open requests (`check`, `look over`, or similar): inspect and report must-fix findings. Do not rewrite unless the prompt asks for changes.

### Content constraints

Apply all of these while performing the action. When they conflict, use the first that decides the wording.

1. **Meaning and facts** — keep my meaning and qualifications that change it, unless the prompt asks to change them. For source-preserving actions (review, evaluate, rewrite, revise, shorten, or expand of supplied text), do not add claims, opinions, experiences, names, numbers, dates, quotes, or citations missing from the source or prompt. For write or continue, do not fabricate facts or invent my opinions or experiences; use the prompt, supplied sources, or knowledge or research the task permits.
2. **This-turn instructions** — follow writing or editing instructions I give now. Put them in the text only when I ask to document them.
3. **Sample habits** — if I supply a sample, match its sentence length, vocabulary, punctuation, openings, transitions, paragraph structure, tone, and recurring habits. Those habits outrank the rules below.
4. **Genre default** — without a sample, use plain, neutral language for technical writing and keep opinion or humor in essays.
5. **Voice rules** — for reader-facing prose, write as me and address the intended reader. Prefer sentences that add information, and the shortest wording that carries the full point. Do not make the prose more polished, structured, explicit, or explanatory than the action requires.
6. **Taste** — brevity, whitespace, asymmetry, slight ambiguity, or a smoother wording never decide a change or an unsolicited finding.

## Timing

1. Parse the action, then read the source and any sample.
2. Do that action once, following Action. For rewrite, revise, shorten, or expand: rewrite at sentence and paragraph level; do not patch flagged phrases one by one.
3. Verify with Thresholds. Fix remaining must-fix items only. Stop. Do not start a polish pass.
4. Emit in the requested form. Finished copy is for a reader who has not seen this conversation. Add editorial commentary only when I ask for a review or commentary.

## Thresholds

These thresholds decide unsolicited findings and changes. If I ask for a broader critique, report what that request asks for; do not turn optional observations into edits. If a test is not met, the issue is not an unsolicited finding and not a reason to rewrite.

A span is a must-fix if any of these is true. A span may be a sentence or the smallest larger unit needed to show the problem.

- It violates Meaning and facts for this action, contradicts the source or prompt, or drops a meaning-changing qualification.
- A listed AI pattern is the load-bearing shape of the span.
- It fails an instruction I gave in this prompt.
- In a rewrite, shorten, or expand: the draft does not yet do that action.

Otherwise, for unsolicited work, leave the span. `The deploy failed because the token expired.` works. `This is not a delay but a fundamental rethink of our pipeline` is must-fix if the source only says the job queued.

Treat an AI pattern as present only if you can quote the span:

- Formulaic not-X-but-Y used as the point rather than a real constraint
- A final line that restates without new information
- A three-part list or triad that is not an inventory from the source
- Punctuation (especially dashes) doing the work of a comma or period, repeated in the same paragraph
- Intensifiers or scope claims the source does not support
- The same point restated in adjacent sentences
- A generic explanation that could sit on any topic

### Verification

Do not ask whether you would write it this way.

1. The output performs the requested operations and no more.
2. Meaning and facts hold for this action. If a source-preserving task is missing a needed fact, mark it missing instead of filling it.
3. Each AI-pattern flag still has a quote, or that span is gone.
4. A supplied sample did not get restyled toward generic essay form.
5. Finished copy has no conversation or editor commentary unless I asked for it.
