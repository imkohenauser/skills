# Agent Skills

Skills for products and the agents that build them.

## Install

```bash
npx skills add imkohenauser/skills
```

## Update

```bash
npx skills update review-accessibility
npx skills update web-naming-conventions
```

### 日本語のスキル

```bash
npx skills update commit-ja
npx skills update perspective-audit-ja
npx skills update review-terms-ja
```

## Skills

| Skill | Task | Invocation |
| --- | --- | --- |
| [review-accessibility](skills/review-accessibility/SKILL.md) | Review interface accessibility. | Automatic or explicit |
| [web-naming-conventions](skills/web-naming-conventions/SKILL.md) | Choose, review, and rename web-project names. | Automatic or explicit |

### 日本語のスキル

| スキル | 用途 | 起動 |
| --- | --- | --- |
| [commit-ja](skills/commit-ja/SKILL.md) | 日本語の Conventional Commit メッセージを作成。依頼時はコミットも実行 | 自動または明示 |
| [perspective-audit-ja](skills/perspective-audit-ja/SKILL.md) | LLM生成文書やAgent向け指示の視座・文脈・責務の混同を監査 | 明示 |
| [review-terms-ja](skills/review-terms-ja/SKILL.md) | 日本語の用語・訳語を見直し、必要に応じて意味と用例を調査 | 自動または明示 |

## License

[MIT](LICENSE)
