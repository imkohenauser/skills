---
name: commit-ja
description: Propose a Japanese Conventional Commit message from staged Git changes, or create that commit when the current task authorizes it. Use when invoked as `$commit-ja` or `/commit-ja`, attached with `@`, used as a Custom Mode, or when a repository rule such as AGENTS.md names this skill and the agent reads this SKILL.md.
license: MIT
# Cursor/Claude Code extension; not in the Agent Skills spec.
disable-model-invocation: true
---

# Japanese Commit Message

Compose always applies once these instructions are loaded.

Choose Propose or Apply from the current task, not from how the skill was loaded. `@` attachment and Custom Mode load these instructions; they do not authorize a commit.

- Propose when the task is to draft a commit message, including a standalone `$commit-ja` or `/commit-ja` invocation with no request to create a commit.
- Apply when these instructions are loaded and the current task authorizes creating commits.

## Compose

Use the Conventional Commits form `type(scope)!: subject`:

- Choose one of `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `build`, `ci`, or `revert`.
- Add a scope only when it is clear from the staged paths or diff.
- Add `!` immediately after the type or scope for a breaking change. Add a `BREAKING CHANGE:` footer when the migration impact needs explanation.
- Write the type and scope in English. Write the subject and body in Japanese.
- Describe the result of applying the commit, not the editing process.
- Write the subject as a concise Japanese noun phrase. Do not use `〜しました`.
- Include meaningful domain or behavior terms; do not use only generic words such as `修正` or `更新`, and do not list filenames as the subject.
- Do not end the subject with punctuation. Aim for 50 characters and never exceed 72 characters.
- Keep ticket numbers and URLs out of the subject.
- Add a body only when it clarifies motivation, behavior, or impact. Do not narrate implementation details.

Decide how many messages or commits to produce in Propose or Apply, not here.

## Inspect

When proposing a message, read Git state only; do not edit files, change the index, or create a commit.

Run these commands in parallel and do not inspect anything else unless the staged diff is insufficient:

- `git status --short`
- `git diff --cached --stat`
- `git diff --cached`
- `git log -8 --format='%s'`

Use only the staged diff as the source of truth. Ignore unstaged and untracked changes. Use recent commit subjects only to match the repository's established message style; do not search for additional commit conventions.

If there are no staged changes, follow Propose for the empty-state output and stop.

If paths and diff hunks do not provide enough context for an accurate message, read only the additional context needed to resolve the uncertainty. Keep the message grounded in the staged changes.

## Propose

When proposing a message, do not create a commit. Output only the proposed message text inside a single fenced code block labeled `text` for clipboard copying. Do not add an introduction, explanation, conclusion, or reasoning outside the fence.

If there are no staged changes, output only `ステージ済みの変更はありません` inside that same fence and stop.

If the staged diff clearly combines concerns that can be applied and reverted independently, output one message for each concern, even when they share a type. Keep them in the same fence and separate them with `---`. Keep a change and its supporting tests or documentation together when they serve the same purpose.

Example:

```text
feat(auth): OAuth2ログインエンドポイントの追加

リフレッシュトークンを使ったセッション継続に対応。
```

## Apply

Use this path when these instructions are loaded and the current task authorizes creating commits. Loading the skill, naming it in a repository rule, attaching it with `@`, or using it as a Custom Mode does not itself authorize a commit. If the task only asks for a commit message, follow Inspect and Propose.

1. Before changing the index, inspect `git status --short`, `git diff --cached --stat`, and `git diff --cached`. Inspect `git diff` when unstaged changes overlap the intended commit or staging is needed. Identify the authorized changes, unrelated changes, and partially staged files.
2. Stage only authorized paths or hunks that the task requires. Preserve unrelated staged changes and unstaged portions of partially staged files; do not use blanket staging or a reset to simplify selection. If the intended changes cannot be isolated safely, stop before committing and explain the unresolved scope or staging issue.
3. Split concerns that can be applied and reverted independently, regardless of type. Keep each change with its supporting tests or documentation. Preserve remaining changes and their staging state between commits.
4. Immediately before each commit, recheck status and the exact staged diff to be committed. Commit only when it is nonempty, contains only the intended changes, has no unresolved conflicts, and required repository checks have passed. If nothing remains to commit, report that and stop; do not create an empty commit. If a precondition is unmet, report it without committing.
5. Compose the message from that diff using Compose and pass it to Git as plain text, without code fences or `---` separators. After each commit, verify the resulting commit and remaining Git state before reporting success. If a commit or hook fails, inspect the resulting state before retrying; do not bypass required hooks or checks.
