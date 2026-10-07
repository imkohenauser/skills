# Harness Memory

Keeps rules and facts that outgrow `AGENTS.md` in `memory/harness/index.md`, a file you commit and review like code. Agents read it before work and change it only when an administrator asks.

When the memory grows too long to read every session, the agent suggests splitting it. Guardrails stay in `index.md`, other sections move to sibling files such as `memory/harness/misc.md`, and `index.md` remains the entry point, so the routing lines do not change.

## Sections

Harness here means the guidance agents follow in the project. The runtime that runs the skill, APIs, and tools are out of scope.

```text
Item ──▶ Misc
  │        │
  ▼        ▼
Scaffolding
  │
  ▼
Guardrails
```

An item that describes structure to follow goes to Scaffolding, and one that must never be broken goes on to Guardrails; other notes go to Misc. Rows firm up along the same arrows. The three sections stay fixed by default.

## Usage

Ask in plain words, or invoke `$harness-memory` in Codex or `/harness-memory` in Cursor and Claude Code.

| Request | Result |
| --- | --- |
| Remember: never write to the production database. | Adds a row to Guardrails. |
| Change the scaffolding note on new pages to `app/(site)/`. | Updates the matching row. |
| Forget the Misc entry on date handling. | Deletes the row. |
| What does the harness memory say about deployment? | Cites the matching rows. |

```markdown
## Guardrails

| Item | Note |
| --- | --- |
| Production database | Never write to it (prevents a repeat incident). |
```

Review changes to `memory/harness/` in pull requests like any other change.

## Routing

Installing the skill does not make agents read the memory. Add these lines to `AGENTS.md`, or to `CLAUDE.md` if that is what your clients read, and adjust the path to where the skill is installed:

```markdown
## Harness memory

- Read `memory/harness/index.md` before starting work.
- Change `memory/harness/` only on an administrator's explicit instruction, following `.agents/skills/harness-memory/SKILL.md`.
- Keep project memory there, not in a client's built-in memory.
- Report entries that contradict the current state instead of changing them.
```
