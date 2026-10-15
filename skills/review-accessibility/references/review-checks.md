# Accessibility checks

Use the checks relevant to the flow and review target.

## Semantics

- Native links for navigation and buttons for actions; preserve browser link behavior.
- Accessible names for links and controls, including visible labels; roles and states matching behavior.
- Valid `aria-labelledby` and `aria-describedby` references; no focusable content under `aria-hidden="true"`.
- Page title and language, useful landmarks and headings, and a way to bypass repeated content.
- Lists, data tables, and control groups exposed in markup when their structure carries meaning.
- Image alternatives matching purpose: empty for decoration, meaning for information, action or destination for functional images.

## Keyboard and focus

- Complete tasks with the keyboard; check focus order, visibility, and equivalent operation.
- Focused elements not entirely hidden by sticky headers, banners, or other author content.
- Test custom focus indicators, including forced-colors mode where relevant.
- Check actual ordering problems from positive `tabindex`; allow expected roving tabindex in composite widgets.
- For modals, check entry focus, background isolation, focus containment, expected Escape behavior, and restoration.
- Keep hidden and inactive content out of the tab order. Check title and focus after client-side navigation.

## Forms and updates

- Programmatic labels, input types, and autocomplete. No unexpected context change on focus or input.
- Authentication without memory or transcription tests unless an alternative exists, including paste and password-manager support.
- Previously entered information filled in or selectable instead of requested again in the same process.
- Visible, associated, reachable errors and accurate invalid states. Allow users to obtain actionable validation.
- Control-specific descriptions, polite routine status updates, and alerts for urgent updates.
- Stable live regions and enough time to access essential messages and actions.

## Visual and pointer access

- Information conveyed beyond color or motion alone.
- Measured rendered contrast for text, UI components, meaningful graphics, and focus indicators; token names are insufficient evidence.
- Target size under the applicable criterion, including its spacing, inline, equivalent-control, user-agent, and essential exceptions.
- Single-pointer alternatives for dragging and for multipoint or path-based gestures.
- Usable hit areas without obstructing overlays or overlap; hover interactions that also work on touch.
- Hover or focus content that users can dismiss and hover, and that stays visible until no longer needed.
- Text resize, text spacing, zoom, and narrow reflow without loss of content or function. Allow scrolling for two-dimensional content.

## Motion and media

- Controls for autoplaying audio and for moving or auto-updating content, flash limits, and access to time-limited information.
- Reduced-motion behavior that retains necessary state cues. At AA, distinguish recommendations from AAA criterion 2.3.3 or explicit project requirements.
- Captions for video with speech, audio description for prerecorded video, and text alternatives for audio.

## References

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/)
