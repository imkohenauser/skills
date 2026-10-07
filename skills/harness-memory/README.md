# Harness Memory

A lightweight framework for sharing project memory with coding agents.
Agree on what to remember, keep it in readable Markdown, and carry it into future work.

- **Agree**: before saving, the agent shows the exact text and the rows it changes, so you can check that no background, condition, or meaning is lost.
- **Keep**: entries are saved as readable Markdown in `memory/harness/`, outside `AGENTS.md`, `CLAUDE.md`, and skills.
- **Carry**: in later work, the agent reads the index and only the files the task needs, in interactive sessions and automations alike.

The agent changes the memory only on explicit instruction from an administrator or an approved automation, and reports, informs, and consults rather than acting alone. Confidential information never goes into the memory.

## Files

```text
memory/harness/
├── index.md         # one link and one line per file
├── guardrails.md    # circumstances and cautions that guide judgment, with background
├── scaffolding.md   # procedures, tools, environment, and references
└── notes.md         # other lasting project information
```

What to record, and where, follows the project's circumstances and your intent. The memory is guidance, not rules, and enforces nothing; keep rules that must always apply in `AGENTS.md` or CI.

## Usage

Ask in plain words, or invoke `$harness-memory` in Codex or `/harness-memory` in Cursor and Claude Code.

| Request | Result |
| --- | --- |
| Remember: December is the client's peak season, and a large release then once overloaded their support. | Shows the row for `guardrails.md` with that background, then saves it once you agree. |
| Change the scaffolding entry on new pages to `app/(site)/`. | Edits that row only; the request already gives the exact content. |
| Forget the note on date handling. | Shows the row and any related duplicates, then deletes them once you agree. |
| Shorten the scaffolding entries on local setup. | Shows the shortened rows and any background or conditions they drop, then saves once you agree. |
| What does the harness memory say about releases? | Reads the index and the relevant file, then cites the rows. |

The first request might be saved as:

```markdown
| Item | Detail |
| --- | --- |
| December releases | December is the client's peak season, and a large release then once overloaded their support, so weigh release size and timing. |
```

Commit and review the files like code, or keep them local with `.gitignore`. The skill does not commit or push without permission.

## Routing

Installing the skill does not make agents read the memory. Add these lines to `AGENTS.md`:

```markdown
## Harness memory

- Before starting work, read `memory/harness/index.md`, then only the files relevant to the task.
- Change `memory/harness/` only on explicit instruction from an administrator or an approved automation, following the `harness-memory` skill.
- Keep project memory there, not in a client's built-in memory, and never store confidential information in it.
```

For `CLAUDE.md`, add the same lines, or import `AGENTS.md` with a line containing `@AGENTS.md`. If a client cannot load skills, replace the skill name with the path to the installed `SKILL.md`, which varies by client and install method.
