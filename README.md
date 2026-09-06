# Personal Agent Skills

Reusable skills for AI coding agents, distributed as an [Agent Skills](https://agentskills.io/) repository.

## Skills

| Skill | Description | Invocation |
| --- | --- | --- |
| [`web-naming-conventions`](skills/web-naming-conventions/) | Choose, review, and safely rename web-project identifiers and public contracts. | Automatic or `$web-naming-conventions` |
| [`review-accessibility`](skills/review-accessibility/) | Review interface code or rendered flows for evidence-backed accessibility barriers. | Explicit: `$review-accessibility` |
| [`commit-ja`](skills/commit-ja/) | Propose Japanese Conventional Commit messages from staged changes without modifying Git state. | Explicit: `$commit-ja` |

## Install

```bash
npx skills add imkohenauser/skills
```

Use the [skills CLI](https://github.com/vercel-labs/skills) to install into Cursor, Codex, Claude Code, Copilot, Antigravity, and [more agents](https://github.com/vercel-labs/skills#supported-agents).

The CLI auto-detects the installed agent. To target one explicitly (for example, Antigravity), pass `--agent`:

```bash
npx skills add imkohenauser/skills --agent antigravity
```

## License

[MIT](LICENSE)
