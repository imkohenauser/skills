# Repository conventions

## Structure

- Store each skill in `skills/<skill-name>/SKILL.md`.
- Use lowercase kebab-case names, at most 64 characters. Match the directory and frontmatter name.
- Add `references/`, `scripts/`, or `assets/` only when needed. Link supporting files relative to the skill directory.
- Keep repository-wide validation in `scripts/`.

## Frontmatter

```yaml
---
name: example-skill
description: Use when choosing names for web-project identifiers.
license: MIT
---
```

Require `name` and `description`. Describe what the skill does and when to use it, with concrete trigger terms, in at most 1,024 characters. Use third-person wording such as `Use when ...`. Include `license` only when applicable.

Other specification fields are `compatibility`, `metadata`, and `allowed-tools`.

For explicit-only invocation, set both client controls:

- `disable-model-invocation: true` in `SKILL.md` for Cursor and Claude Code.
- `policy.allow_implicit_invocation: false` in `agents/openai.yaml` for Codex.

Omit both for automatic invocation. Other clients may ignore these controls. `disable-model-invocation` is a vendor extension; the repository validator permits it before running strict spec checks.

## Changes

Read the affected files before editing. Preserve unrelated changes, update the README index when needed, and check names, frontmatter, links, examples, and commands.

Run `python3 scripts/validate-skills.py` and any relevant script tests. Install its dependency with `pip install skills-ref` if needed.

## References

- [Agent Skills specification](https://agentskills.io/specification.md)
- [Cursor skills](https://cursor.com/docs/skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
