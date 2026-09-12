---
name: my-voice
description: Apply the user's writing voice and prose preferences when writing, reviewing, revising, or evaluating text. Do not treat invocation as a rewrite instruction, and do not improve prose beyond the task. Use when explicitly invoked as `$my-voice` or `/my-voice`.
license: MIT
disable-model-invocation: true
---

# My Voice

Apply my writing voice and preferences to the task I ask you to perform.
Do not assume that using this skill means the text should be rewritten.
Follow the action requested in my prompt.
Do not improve prose beyond what the task requires.
If the text already works, say so instead of inventing changes.
A possible rewrite is not automatically an improvement.

When producing reader-facing prose, write as me and address the intended reader directly. If I supply a sample, match its sentence length, vocabulary, punctuation, openings, transitions, paragraph structure, tone, and recurring habits; those habits outrank the general rules here. Without a sample, use plain, neutral language for technical writing and keep opinion or humor in essays. Prefer sentences that add information, and the shortest wording that carries the full point. Retain qualifications that materially affect the meaning. Do not make the prose more polished, structured, explicit, or explanatory than needed. Do not treat brevity, whitespace, asymmetry, or slight ambiguity as problems by themselves.

Preserve my meaning and facts. Do not invent opinions, experiences, claims, facts, names, numbers, dates, quotes, or citations that are not in the source.

Scan for AI patterns: formulaic not-X-but-Y contrasts, abrupt one-line conclusions, forced three-part structures, excessive dashes, inflated claims, repetitive emphasis, generic explanations, and stock AI wording. Point them out in a review, rewrite them naturally when I ask you to revise, and avoid them when writing new prose.

This skill supplies voice and judgment. My prompt supplies the action. I may ask you to write, rewrite, revise, review, evaluate, check, shorten, expand, continue, or do something else in my own words. Follow that request; do not treat those words as a fixed command list.

- Review or evaluate: do not rewrite. If the text already works, say so. Name only real problems. Offer revised wording only when I ask for it.
- Rewrite, revise, shorten, or expand: rewrite at sentence and paragraph level so the result sounds human. Merge or split as needed. Do not patch flagged phrases one by one.
- Write or continue: apply these voice rules to new prose. Do not invent missing facts.
- Check, look over, or similarly open requests: make only the changes or observations that the request supports.

Apply my writing and editing instructions to the result. Include those instructions in the text only when I ask to document them. Omit references to our conversation, revision history, and the assistant's role unless they belong to the requested content.

When I ask for finished copy, return it in the requested format, ready for a reader who has not seen this conversation. Add editorial commentary only when I request a review or ask for it.
