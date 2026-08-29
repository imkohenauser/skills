#!/usr/bin/env python3
"""Validate skills against the Agent Skills spec, plus documented vendor fields.

Strict `skills-ref` / `agentskills validate` rejects `disable-model-invocation`
because that key is a Cursor and Claude Code extension, not a spec field.
This script strips that documented extension, runs skills-ref spec checks on
the remaining frontmatter, then checks the vendor field and Codex sidecar.
"""

from __future__ import annotations

import sys
from pathlib import Path

VENDOR_FIELDS = frozenset({"disable-model-invocation"})
REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"


def _is_yaml_true(value: object) -> bool:
    return value is True or str(value).strip().lower() == "true"


def _is_yaml_false(value: object) -> bool:
    return value is False or str(value).strip().lower() == "false"


def _read_allow_implicit_invocation(path: Path) -> bool | None:
    if not path.is_file():
        return None

    import strictyaml
    from skills_ref.errors import ParseError

    try:
        data = strictyaml.load(path.read_text(encoding="utf-8")).data
    except strictyaml.YAMLError as exc:
        raise ParseError(f"Invalid YAML in {path}: {exc}") from exc

    if not isinstance(data, dict):
        return None
    policy = data.get("policy")
    if not isinstance(policy, dict) or "allow_implicit_invocation" not in policy:
        return None
    value = policy["allow_implicit_invocation"]
    if _is_yaml_true(value):
        return True
    if _is_yaml_false(value):
        return False
    raise ParseError(
        f"{path}: policy.allow_implicit_invocation must be true or false, got {value!r}"
    )


def validate_skill(skill_dir: Path) -> list[str]:
    from skills_ref.errors import ParseError
    from skills_ref.parser import find_skill_md, parse_frontmatter
    from skills_ref.validator import validate_metadata

    errors: list[str] = []
    skill_md = find_skill_md(skill_dir)
    if skill_md is None:
        return ["Missing required file: SKILL.md"]

    try:
        metadata, _body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    except ParseError as exc:
        return [str(exc)]

    vendor = {key: metadata[key] for key in VENDOR_FIELDS if key in metadata}
    spec_metadata = {key: value for key, value in metadata.items() if key not in VENDOR_FIELDS}
    errors.extend(validate_metadata(spec_metadata, skill_dir))

    disable_model_invocation = False
    if "disable-model-invocation" in vendor:
        value = vendor["disable-model-invocation"]
        if not _is_yaml_true(value):
            errors.append(
                "Vendor field 'disable-model-invocation' must be true; "
                "omit the field to allow auto-invocation"
            )
        else:
            disable_model_invocation = True

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    try:
        allow_implicit = _read_allow_implicit_invocation(openai_yaml)
    except ParseError as exc:
        errors.append(str(exc))
        return errors

    if disable_model_invocation and allow_implicit is not False:
        errors.append(
            "disable-model-invocation is true, but agents/openai.yaml does not "
            "set policy.allow_implicit_invocation: false"
        )
    if allow_implicit is False and not disable_model_invocation:
        errors.append(
            "agents/openai.yaml sets allow_implicit_invocation: false, but "
            "SKILL.md is missing disable-model-invocation: true"
        )

    return errors


def main() -> int:
    try:
        import skills_ref  # noqa: F401
    except ImportError:
        print("Install skills-ref first: pip install skills-ref", file=sys.stderr)
        return 2

    if not SKILLS_DIR.is_dir():
        print(f"Skills directory not found: {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(
        path for path in SKILLS_DIR.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    if not skill_dirs:
        print(f"No skill directories found in {SKILLS_DIR}", file=sys.stderr)
        return 1

    failed = False
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failed = True
            print(f"{skill_dir.name}:")
            for error in errors:
                print(f"  - {error}")
            continue

        skill_md = skill_dir / "SKILL.md"
        permitted = []
        if skill_md.is_file() and "disable-model-invocation:" in skill_md.read_text(
            encoding="utf-8"
        ):
            permitted.append("disable-model-invocation")
        suffix = f" (permitted vendor field: {', '.join(permitted)})" if permitted else ""
        print(f"{skill_dir.name}: ok{suffix}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
