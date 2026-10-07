# Harness Memory

Keeps project-specific memory for coding agents in `memory/harness/`, outside `AGENTS.md`, `CLAUDE.md`, and skills. Agents read only what the task needs, change the memory only on explicit instruction from an administrator or an approved automation, and report, inform, and consult rather than act alone. Confidential information never goes into the memory. The same files serve interactive sessions and non-interactive automations.

## Files

```text
memory/harness/
├── index.md         # one link and one line per file
├── guardrails.md    # constraints to keep, with their background
├── scaffolding.md   # procedures, tools, environment, and references
└── notes.md         # other lasting project information
```

Files are chosen by use, and an entry moves only when its role changes. The memory is guidance and enforces nothing; keep rules that must always apply in `AGENTS.md` or CI. When the memory grows, compress it before adding files.

## Usage

Ask in plain words, or invoke `$harness-memory` in Codex or `/harness-memory` in Cursor and Claude Code.

| Request | Result |
| --- | --- |
| Remember: never write to the production database. | Adds a row to `guardrails.md`. |
| Change the scaffolding entry on new pages to `app/(site)/`. | Edits that row only. |
| Forget the note on date handling. | Deletes the row and checks for duplicates. |
| Compress the harness memory. | Merges duplicates and shortens rows without adding anything. |
| What does the harness memory say about deployment? | Reads the index and the relevant file, then cites the rows. |

The files are plain Markdown. Commit and review them like code, or keep them local with `.gitignore`. The skill does not commit or push without permission.

## Routing

Installing the skill does not make agents read the memory. Add these lines to `AGENTS.md`:

```markdown
## Harness memory

- Before starting work, read `memory/harness/index.md`, then only the files relevant to the task.
- Change `memory/harness/` only on explicit instruction from an administrator or an approved automation, following the `harness-memory` skill.
- Keep project memory there, not in a client's built-in memory, and never store confidential information in it.
```

For `CLAUDE.md`, add the same lines, or import `AGENTS.md` with a line containing `@AGENTS.md`. If a client cannot load skills, replace the skill name with the path to the installed `SKILL.md`, which varies by client and install method.
