# Agent Skills

Reusable skills for AI coding agents, distributed as an [Agent Skills](https://agentskills.io/) repository. Compatible with Cursor, Codex, and other `SKILL.md` clients.

Explicit invocation control is client-dependent. Cursor and Claude Code honor `disable-model-invocation` in `SKILL.md`; Codex honors `policy.allow_implicit_invocation` in `agents/openai.yaml`. Other clients may ignore both and treat every skill as auto-invocable.

## Skills


| Skill                                                      | Description                                                                                    | Invocation                                                          |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `[web-naming-conventions](skills/web-naming-conventions/)` | Choose, review, and safely rename web-project identifiers and public contracts.                | Automatic, or `$web-naming-conventions` / `/web-naming-conventions` |
| `[review-accessibility](skills/review-accessibility/)`     | Review interface code or rendered flows for evidence-backed accessibility barriers.            | Explicit: `$review-accessibility` / `/review-accessibility`         |
| `[commit-ja](skills/commit-ja/)`                           | Propose Japanese Conventional Commit messages from staged changes without modifying Git state. | Explicit: `$commit-ja` / `/commit-ja`                               |


Codex uses `$skill-name`. Cursor uses `/skill-name`.

## Install

```bash
npx skills add imkohenauser/skills
```

Use the [skills CLI](https://github.com/vercel-labs/skills) to install into Cursor, Codex, Claude Code, Copilot, and [more agents](https://github.com/vercel-labs/skills#supported-agents).

The CLI auto-detects the installed agent. To target one explicitly (for example, Cursor), pass `--agent`:

```bash
npx skills add imkohenauser/skills --agent cursor
```

For Cursor Cloud Agents, omit `-g` so the skill is installed into the project (`.agents/skills/`). User-level `~/.cursor/skills/` is not copied to Cloud Agents.

In Cursor Agent chat, type `/` and search for the skill name. Explicit-only skills (`review-accessibility`, `commit-ja`) load only when invoked this way.

## License

[MIT](LICENSE)