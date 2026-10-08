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

### Web / UI

| Skill | Task | Invocation |
| --- | --- | --- |
| [review-accessibility](skills/review-accessibility/SKILL.md) | Review interface accessibility. | Explicit |
| [web-naming-conventions](skills/web-naming-conventions/SKILL.md) | Choose, review, and rename web-project names. | Automatic or explicit |

### Japanese

| Skill | Task | Invocation |
| --- | --- | --- |
| [commit-ja](skills/commit-ja/SKILL.md) | Write Japanese Conventional Commit messages; commit when requested. | Explicit |
| [natural-technical-writing-ja](skills/natural-technical-writing-ja/SKILL.md) | Write and revise natural, precise Japanese technical prose. | Explicit |

**commit-ja**, invoked on its own, returns a message for staged changes. Ask to create a commit to commit them. To use it as a project convention, add an instruction to `AGENTS.md` to read its `SKILL.md` when committing.

## License

[MIT](LICENSE)
