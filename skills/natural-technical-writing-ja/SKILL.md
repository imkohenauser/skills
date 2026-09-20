---
name: natural-technical-writing-ja
description: Write, translate, revise, or review technical material in natural, precise Japanese. Use when explicitly invoked as `$natural-technical-writing-ja` or `/natural-technical-writing-ja`. Use for Japanese documentation, explanations, articles, and reports when terminology, literal translation, mixed English and Japanese, or formulaic LLM prose needs attention.
license: MIT
disable-model-invocation: true
---

# Natural Japanese Technical Writing

Produce technical prose that reads as if it was written in Japanese, not converted from English. Preserve technical meaning, qualifications, and identifiers. Removing English is not the goal.

Follow the requested action. A review request calls for findings; it does not authorize a full rewrite. When revising supplied text, do not introduce facts, claims, or opinions absent from the source unless the user asks for substantive additions.

## Set the standard

Adapt terminology and explanation to the stated audience, domain, and publication. When these are not stated, assume technically literate Japanese readers who may not know project-specific jargon.

Use this priority order when criteria conflict:

1. Preserve the intended technical meaning, including agency, causality, conditions, constraints, modality, and degree of certainty.
2. Preserve exact names and code-level identifiers where recognition or interoperability depends on them.
3. Make the prose idiomatic and independently understandable in Japanese.
4. Keep terminology consistent within the document.

Do not simplify away a distinction merely to make a sentence smoother. If natural Japanese would be materially ambiguous, retain the precise source term and explain it as needed.

## Choose technical terms

Decide by concept and usage, not by replacing words one at a time.

1. **Established Japanese term:** Use the term current in the relevant field, normally without repeating the English.
   - `distributed system` → `分散システム`
   - `reinforcement learning` → `強化学習`
   - `dependency injection` → `依存性注入`
2. **Established English, abbreviation, or loanword:** Keep the form Japanese practitioners normally encounter when it is clearer than a translation.
   - `API`, `RAG`, `トークン`, `埋め込み`, `ファインチューニング`
3. **Unsettled term with an explainable concept:** Express the meaning in Japanese. If the source term aids identification or search, add it in parentheses on first occurrence only.
   - `モデルに与える文脈を設計する手法（context engineering）`
4. **Exact identity matters:** Preserve official product, service, API, library, protocol, standard, class, function, variable, CLI command, configuration key, and code identifier names.

Do not invent an authoritative-sounding Japanese term for a new concept. Do not assume a literal katakana transcription is established usage. If usage is uncertain and the distinction matters, retain the original term, explain it, or verify terminology when the task permits research.

Respect a glossary, style guide, official localization, or user-selected spelling when supplied. On first mention, a long explanation may introduce a shorter form for consistent later use.

## Rebuild the sentence in Japanese

Recover the proposition first, then express it using Japanese information structure. Reorder clauses, split overloaded sentences, turn abstract nouns into verbs, and choose a natural subject where useful. Do not preserve English syntax for its own sake.

In particular:

- avoid long chains of prenominal modifiers;
- avoid stacked abstract nouns and unnecessary nominalization;
- do not mechanically retain an inanimate subject;
- translate `enable`, `provide`, `support`, and `leverage` according to their function in context, not with a fixed equivalent;
- prefer a direct construction over `〜することを可能にする` when the meaning is simply `〜できる`;
- rewrite the whole clause when isolated word substitution would leave mixed-language syntax.

For example:

```text
Avoid: この機能は、ユーザーが効率的に設定を管理することを可能にします。
Prefer: この機能を使うと、設定を効率よく管理できます。

Avoid: agentic workflow の context を管理する。
Prefer: 自律的に処理を進めるワークフローで、モデルに渡す文脈を管理する。

Avoid: オーケストレーションによってタスクエグゼキューションをハンドリングする。
Prefer: 複数の処理を調整し、タスクの実行を管理する。
```

Keep a loanword when it is genuinely conventional for the audience. For example, `エージェント` or `ワークフロー` may be preferable to a forced paraphrase in a field that routinely uses those terms.

## Remove translation and LLM residue

Revise wording that adds no meaning or makes the English source structure visible. Common signals include repeated `〜することができます`, `〜を提供します`, `〜を実現します`, `〜を活用します`, `〜が重要となります`, and filler such as `〜という点で` or `〜の観点から`.

Treat fashionable adjectives and loanwords such as `シームレス`, `堅牢`, `革新的`, `包括的`, or `柔軟かつスケーラブル` as claims, not decoration. Keep them only when the source supports the specific meaning and the term suits the audience. Vary repetitive endings only when doing so improves the prose without changing emphasis.

Do not apply a blacklist mechanically. A flagged expression may be correct in a specification, quotation, established product language, or context that requires its exact nuance.

## Protect exact text

Unless asked to localize it, do not translate or normalize text whose exact form matters:

- code, commands, paths, URLs, keys, values, error messages, and syntax;
- official feature names and UI labels;
- quoted text and defined terms;
- normative keywords such as `MUST` or `SHOULD` when their formal force matters.

Format and explain exact text in natural Japanese around it. Preserve Markdown links, code fences, placeholders, and document structure unless the requested action includes changing them.

## Working method

1. Identify the claim of each passage rather than mapping its words.
2. Fix the form of recurring terms using the hierarchy above.
3. Draft or revise at sentence and paragraph level in natural Japanese.
4. Compare the result with the source for lost or added meaning.
5. Remove unjustified English, coined katakana, literal syntax, vague modifiers, repetition, and formulaic filler.

For a long or terminology-heavy document, maintain a small working glossary. Distinguish deliberate first-use patterns such as `日本語の説明（English term）` from accidental variation.

## Final check

Before returning the result, confirm that:

- every remaining English term has a reason to remain;
- the Japanese text is understandable without relying on the source sentence structure;
- no unsettled term is presented as an established translation without evidence;
- technical meaning and qualifications remain intact;
- the same concept uses the same form unless the variation is deliberate;
- the result reads as Japanese technical prose rather than as a translation exercise.
