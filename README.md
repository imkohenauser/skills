# Personal Agent Skills

Reusable skills for AI coding agents, distributed as an [Agent Skills](https://agentskills.io/) repository.

## Skills

| Skill | Description | Invocation |
| --- | --- | --- |
| [`web-naming-conventions`](skills/web-naming-conventions/) | Choose, review, and safely rename web-project identifiers and public contracts. | Automatic or `$web-naming-conventions` |
| [`review-accessibility`](skills/review-accessibility/) | Review interface code or rendered flows for evidence-backed accessibility barriers. | Explicit: `$review-accessibility` |
| [`commit-ja`](skills/commit-ja/) | Propose Japanese Conventional Commit messages from staged changes without modifying Git state. | Explicit: `$commit-ja` |

## Install

List the available skills:

```sh
npx skills add imkohenauser/skills --list
```

Install one skill globally for Codex:

```sh
npx skills add imkohenauser/skills --skill web-naming-conventions -g -a codex
```

Replace the skill name to install another skill, or omit `--skill` to select interactively.

## License

[MIT](LICENSE)
