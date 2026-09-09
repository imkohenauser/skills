# Agent Skills

Reusable skills for AI coding agents, distributed as an [Agent Skills](https://agentskills.io/) repository. Compatible with Cursor, Codex, and other `SKILL.md` clients.

Explicit invocation control is client-dependent. Cursor and Claude Code honor `disable-model-invocation` in `SKILL.md`; Codex honors `policy.allow_implicit_invocation` in `agents/openai.yaml`. Other clients may ignore both and treat every skill as auto-invocable.

## Skills

| Skill | Description | Invocation |
| --- | --- | --- |
| [`commit-ja`](skills/commit-ja/) | Japanese Conventional Commit messages: propose a message from staged changes, or apply it when the task authorizes creating a commit. | `$commit-ja` / `/commit-ja`. Cursor: also `@` or Custom Mode. AGENTS.md: name it and instruct the agent to read `SKILL.md`. |
| [`web-naming-conventions`](skills/web-naming-conventions/) | Choose, review, and safely rename web-project identifiers and public contracts. | Automatic, or `$web-naming-conventions` / `/web-naming-conventions` |
| [`review-accessibility`](skills/review-accessibility/) | Review interface code or rendered flows for evidence-backed accessibility barriers. | Explicit: `$review-accessibility` / `/review-accessibility` |

Codex uses `$skill-name`. Cursor loads skills with `/skill-name`, `@` attachment, or Custom Mode. See [Skills help](https://cursor.com/help/customization/skills) and [Custom Modes](https://cursor.com/docs/agent/prompting).

Once `commit-ja` instructions are loaded, choose Propose or Apply from the current task. A standalone `$commit-ja` or `/commit-ja` invocation, or a request for a commit message only, uses Inspect and Propose. A request to create a commit uses Apply. `@` attachment and Custom Mode load the skill; they do not authorize a commit.

Projects may name `commit-ja` in `AGENTS.md` as the commit-message convention. Naming it does not load the skill body. Instruct the agent to read this skill's `SKILL.md` and follow Compose and Apply when the task authorizes creating commits. Apply checks Git state and the intended staged changes before committing.

`review-accessibility` distinguishes requirement failures from recommended improvements and reports `Block`, `Inconclusive`, or `Approve` for the inspected scope. `web-naming-conventions` selects names separately from deciding whether an existing contract can be safely migrated.

## Install

```bash
npx skills add imkohenauser/skills
```

Use the [skills CLI](https://github.com/vercel-labs/skills) to install into Cursor, Codex, Claude Code, Copilot, and [more agents](https://github.com/vercel-labs/skills#supported-agents).

The CLI auto-detects the installed agent. To target one explicitly (for example, Cursor), pass `--agent`:

```bash
npx skills add imkohenauser/skills --agent cursor
```

For Cursor Cloud Agents, omit `-g` so the skill is installed into the project (`.agents/skills/`). User-level `~/.cursor/skills/` is available to Cloud Agents when [Sync Skills](https://cursor.com/docs/skills) is on. Unsynced local skills and `~/.agents/skills/` are not copied.

In Cursor Agent chat, load a skill with `/`, `@` attachment, or Custom Mode. Explicit-only skills (`review-accessibility`, `commit-ja`) load only through those paths, not from context. Propose vs Apply for `commit-ja` is described above.

## License

[MIT](LICENSE)
