# Agent Skills

Skills for products and the agents that build them.

## Install

```bash
npx skills add imkohenauser/skills
```

To select an agent:

```bash
npx skills add imkohenauser/skills --agent cursor
```

Use `$skill-name` in Codex or `/skill-name` in Cursor. Cursor also supports `@` attachments and Custom Mode.

## Skills

| Skill | Task | Invocation |
| --- | --- | --- |
| [harness-memory](skills/harness-memory/SKILL.md) | Maintain shared project memory with agents. | Automatic or explicit |
| [web-naming-conventions](skills/web-naming-conventions/SKILL.md) | Choose, review, and rename web-project names. | Automatic or explicit |
| [review-accessibility](skills/review-accessibility/SKILL.md) | Review interface accessibility. | Explicit |
| [commit-ja](skills/commit-ja/SKILL.md) | Write Japanese Conventional Commit messages; commit when requested. | Explicit |
| [natural-technical-writing-ja](skills/natural-technical-writing-ja/SKILL.md) | Write and revise natural, precise Japanese technical prose. | Explicit |

**harness-memory** keeps project memory that outgrows `AGENTS.md` or `CLAUDE.md` in `memory/harness/`. It needs routing lines in either file; see its [README](skills/harness-memory/README.md).

**commit-ja**, invoked on its own, returns a message for staged changes. Ask to create a commit to commit them. To use it as a project convention, add an instruction to `AGENTS.md` to read its `SKILL.md` when committing.

## License

[MIT](LICENSE)
