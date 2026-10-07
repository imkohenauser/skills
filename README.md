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
| [harness-memory](skills/harness-memory/SKILL.md) | Record and look up Git-reviewed project memory. | Automatic or explicit |

Use `$skill-name` in Codex or `/skill-name` in Cursor. Cursor also supports `@` attachments and Custom Mode.

Invoke `commit-ja` on its own to get a message for staged changes. Ask to create a commit to commit them. To use it as a project convention, add an instruction to `AGENTS.md` to read its `SKILL.md` when committing.

`harness-memory` keeps rules and facts that outgrow `AGENTS.md` in `memory/harness.md`, a file you commit and review. Agents change it only when an administrator asks. Installing the skill does not make agents read the file; add these lines to `AGENTS.md`, adjusting the path to where the skill is installed:

```markdown
## Harness memory

- Read `memory/harness.md` before starting work.
- Change it only on an administrator's explicit instruction, following `.agents/skills/harness-memory/SKILL.md`.
- Keep project memory there, not in a client's built-in memory.
- Report entries that contradict the current state instead of changing them.
```

## Development

Install `skills-ref`, then run:

```bash
python3 scripts/validate-skills.py
```

See [AGENTS.md](AGENTS.md) for repository conventions, [Agent Skills](https://agentskills.io/specification.md) for the format, and [skills CLI](https://github.com/vercel-labs/skills) for installation options.

## License

[MIT](LICENSE)
