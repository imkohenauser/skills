# Repository Instructions for AI Agents

This repository contains reusable skills for AI coding agents. Follow these
instructions whenever you create, update, move, or review a skill.

## Repository layout

- Store each skill in `skills/<skill-name>/`.
- Every skill directory must contain a `SKILL.md` file.
- Keep supporting material next to the skill that uses it:
  - `references/` for detailed documentation and examples
  - `scripts/` for reusable automation and validation
  - `assets/` for templates and other static files
- Do not add a support directory unless the skill needs it.

## Naming

- Use lowercase kebab-case for skill names: letters, numbers, and hyphens only.
- Limit skill names to 64 characters.
- The directory name and the `name` field in `SKILL.md` must match exactly.

Example:

```text
skills/example-skill/SKILL.md
```

```yaml
name: example-skill
```

## `SKILL.md`

Begin each `SKILL.md` with YAML frontmatter:

```yaml
---
name: example-skill
description: Use when an agent needs to ...
license: MIT
---
```

### Frontmatter

- `name` is required and must follow the naming rules above.
- `description` is required, must be no more than 1,024 characters, and must
  explain both what the skill does and when it should be used.
- Write descriptions in the third person. Prefer `Use when ...` over
  `You can use this when ...`.
- Include concrete trigger terms that help an agent select the skill.
- `license` is optional. Use it only when the skill or its bundled material has
  an applicable license.

### Instructions

- Write concise, imperative, task-oriented instructions.
- Document decisions, workflows, pitfalls, verification, and cleanup that are
  specific to the skill.
- Do not duplicate general product or library documentation. Link to an
  authoritative source when background material is sufficient.
- Keep `SKILL.md` focused and preferably under 500 lines. Move lengthy details
  into `references/` and link to the exact files an agent should read.
- Prefer existing scripts, templates, and assets over duplicating their content
  in `SKILL.md`.
- Make referenced paths relative to the skill directory and verify that every
  link and command is valid.

## Change workflow

When adding or updating a skill:

1. Inspect the repository and the affected skill before editing.
2. Make the smallest change that fully addresses the request.
3. Preserve unrelated files and user changes.
4. Verify the directory name, frontmatter, paths, examples, and commands.
5. Run any relevant validation or tests provided by the repository or skill.
6. If `README.md` contains a skill index or structure overview, update the
   affected sections so they remain accurate.

## References

- [Agent Skills specification](https://agentskills.io/specification.md)
- [skills CLI](https://github.com/vercel-labs/skills)
