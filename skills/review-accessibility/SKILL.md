---
name: review-accessibility
description: Review interface code, diffs, or rendered pages for accessibility barriers, and fix them when asked. Use when accessibility is requested or required by project rules, such as a11y reviews and audits, WCAG conformance, keyboard and focus behavior, screen reader support, ARIA, color contrast, or target size. Not for ordinary UI work that does not raise accessibility.
license: MIT
---

# Review Accessibility

Review the requested interface or flow against the project's accessibility target, or WCAG 2.2 AA if none is stated. With no target, review the interface changes in the working tree and on the current branch; ask only if there are none. When accessibility is part of another request, such as a code review or a UI change, follow that request's scope and output.

Leave files unchanged unless fixes are requested.

## Review

1. Identify the user tasks, interactive elements, and states in scope.
2. Apply the relevant sections of [review-checks.md](references/review-checks.md).
3. Test the flow in a browser when available, and run the project's accessibility tests or linters, if any.
4. Record each finding's verification: `Observed` in a browser or assistive technology, noting the setup when it matters, or `Source` from code alone, which cannot confirm screen-reader announcements. Mark essential checks you could not run `Not verified`.

## Findings

List findings in this table, ordered by severity. Use `path:line` for code or the flow and element for observed behavior.

| Severity | Location | Finding and evidence | User impact | Suggested fix | Verification |
| --- | --- | --- | --- | --- | --- |

Severity:

- **HIGH**: blocks a task or essential content, traps focus, or makes an essential control inaccessible.
- **MEDIUM**: causes substantial friction or ambiguity.
- **LOW**: causes limited difficulty.

For requirement failures, cite the applicable WCAG criterion and level or project rule. Label other improvements as recommendations. Report concrete barriers rather than convention preferences.

## Fixes

When fixes are requested, prefer native HTML behavior over added ARIA and keep each change within its finding. Re-run the check that found each issue, then report the remaining findings.

## Verdict

End with the reviewed scope, the `Not verified` checks, and one verdict:

- `Block`: a confirmed HIGH finding remains.
- `Inconclusive`: no confirmed HIGH finding, but essential checks are incomplete.
- `Approve`: essential checks are complete and no HIGH finding remains. Include any MEDIUM or LOW findings.

The verdict covers the reviewed scope; automated checks alone do not establish WCAG conformance.
