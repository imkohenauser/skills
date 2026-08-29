# Personal Agent Skills

Reusable skills for AI coding agents, distributed as an [Agent Skills](https://agentskills.io/) repository. Compatible with Cursor, Codex, and other `SKILL.md` clients.

## Skills

| Skill | Description | Invocation |
| --- | --- | --- |
| [`web-naming-conventions`](skills/web-naming-conventions/) | Choose, review, and safely rename web-project identifiers and public contracts. | Automatic, or `$web-naming-conventions` / `/web-naming-conventions` |
| [`review-accessibility`](skills/review-accessibility/) | Review interface code or rendered flows for evidence-backed accessibility barriers. | Explicit: `$review-accessibility` / `/review-accessibility` |
| [`commit-ja`](skills/commit-ja/) | Propose Japanese Conventional Commit messages from staged changes without modifying Git state. | Explicit: `$commit-ja` / `/commit-ja` |

Codex uses `$skill-name`. Cursor uses `/skill-name`.

## Install

List the available skills:

```sh
npx skills add imkohenauser/skills --list
```

Install one skill globally for Cursor and Codex:

```sh
npx skills add imkohenauser/skills --skill web-naming-conventions -g -a cursor -a codex
```

Replace the skill name to install another skill, or omit `--skill` to select interactively.

For Cursor Cloud Agents, omit `-g` so the skill is installed into the project (`.agents/skills/`). User-level `~/.cursor/skills/` is not copied to Cloud Agents.

In Cursor Agent chat, type `/` and search for the skill name. Explicit-only skills (`review-accessibility`, `commit-ja`) load only when invoked this way.

## License

[MIT](LICENSE)
