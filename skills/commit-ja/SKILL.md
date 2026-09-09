---
name: commit-ja
description: Propose a Japanese Conventional Commit message from staged Git changes when explicitly invoked as `$commit-ja` or `/commit-ja`. Also apply the Compose rules when a repository rule such as AGENTS.md names this skill as the commit convention.
license: MIT
# Cursor/Claude Code extension; not in the Agent Skills spec.
disable-model-invocation: true
---

# Japanese Commit Message

Compose always applies.

Inspect and Propose apply only when this skill is explicitly invoked as `$commit-ja` or `/commit-ja`.

Apply applies when a repository rule such as AGENTS.md names this skill as the commit convention and the current task is to create a commit.

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

Prefer one commit per concern.

## Inspect

When explicitly invoked, read Git state only; do not edit files, change the index, or create a commit.

Run these commands in parallel and do not inspect anything else unless the staged diff is insufficient:

- `git status --short`
- `git diff --cached --stat`
- `git diff --cached`
- `git log -8 --format='%s'`

Use only the staged diff as the source of truth. Ignore unstaged and untracked changes. Use recent commit subjects only to match the repository's established message style; do not search for additional commit conventions.

If there are no staged changes, follow Propose for the empty-state output and stop.

If paths and diff hunks do not provide enough context for an accurate message, read at most one relevant file.

## Propose

When explicitly invoked, do not create a commit. Output only the proposed message text inside a single fenced code block labeled `text` for clipboard copying. Do not add an introduction, explanation, conclusion, or reasoning outside the fence.

If there are no staged changes, output only `ステージ済みの変更はありません` inside that same fence and stop.

If the staged diff clearly combines independently committable concerns with different types, output one message for each proposed commit. Keep them in the same fence and separate them with `---`.

Example:

```text
feat(auth): OAuth2ログインエンドポイントの追加

リフレッシュトークンを使ったセッション継続に対応。
```

## Apply

When used as the commit convention, write the commit message as plain text. Do not wrap it in a code fence, and do not emit a proposal instead of committing.

If the staged diff combines independently committable concerns with different types, create separate commits. Do not join messages with `---`.
