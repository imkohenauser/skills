# Agent Skills

Skills for coding agents.

## Install

```bash
npx skills add imkohenauser/skills
```

To select an agent:

```bash
npx skills add imkohenauser/skills --agent cursor
```

## Skills

| Skill | Task | Invocation |
| --- | --- | --- |
| [commit-ja](skills/commit-ja/SKILL.md) | Write Japanese Conventional Commit messages; commit when requested. | Explicit |
| [web-naming-conventions](skills/web-naming-conventions/SKILL.md) | Choose, review, and rename web-project names. | Automatic or explicit |
| [review-accessibility](skills/review-accessibility/SKILL.md) | Review interface accessibility. | Explicit |

Use `$skill-name` in Codex or `/skill-name` in Cursor. Cursor also supports `@` attachments and Custom Mode.

Invoke `commit-ja` on its own to get a message for staged changes. Ask to create a commit to commit them. To use it as a project convention, add an instruction to `AGENTS.md` to read its `SKILL.md` when committing.

## Development

Install `skills-ref`, then run:

```bash
python3 scripts/validate-skills.py
```

See [AGENTS.md](AGENTS.md) for repository conventions, [Agent Skills](https://agentskills.io/specification.md) for the format, and [skills CLI](https://github.com/vercel-labs/skills) for installation options.

## License

[MIT](LICENSE)
