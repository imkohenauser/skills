# Agent Skills

Skills for products and the agents that build them.

## Install

```bash
npx skills add imkohenauser/skills
```

## Skills

| Skill | Task | Invocation |
| --- | --- | --- |
| [review-accessibility](skills/review-accessibility/SKILL.md) | Review interface accessibility. | Explicit |
| [web-naming-conventions](skills/web-naming-conventions/SKILL.md) | Choose, review, and rename web-project names. | Automatic or explicit |

### 日本のスキル

| スキル | 用途 | 起動 |
| --- | --- | --- |
| [commit-ja](skills/commit-ja/SKILL.md) | 日本語の Conventional Commit メッセージを作成。依頼時はコミットも実行 | 明示 |
| [review-terms-ja](skills/review-terms-ja/SKILL.md) | 日本語の用語・訳語を見直し、必要に応じて意味と用例を調査 | 自動・明示 |

**commit-ja** は単独起動でステージ済み変更のメッセージを返す。コミット作成を依頼すると実行する。プロジェクトの慣習にする場合は、コミット時にその `SKILL.md` を読む指示を `AGENTS.md` に追加する。

## License

[MIT](LICENSE)
