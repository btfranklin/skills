# HTML-First Patterns

Use this reference to choose an interaction element and define the limits of its enhancement. Verify version-sensitive behavior in the linked primary documentation when you do the work.

## Source hierarchy

1. [WHATWG HTML Living Standard](https://html.spec.whatwg.org/)
2. [MDN HTML reference](https://developer.mozilla.org/en-US/docs/Web/HTML)
3. [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) when native HTML cannot supply the needed semantics
4. Official documentation for the repository's server or partial-update framework

Use native semantics before ARIA. Treat compatibility tables and framework APIs as time-sensitive.

## Primitive selection

| Need | Baseline | Optional enhancement | Validate |
| --- | --- | --- | --- |
| Navigate | Link with a meaningful URL | Prefetch or transition | Destination, history, modified clicks |
| Submit or mutate | Form with server validation | Partial replacement or optimistic presentation | CSRF, errors, duplicate submission, disabled states |
| Reveal adjacent content | `details` and `summary` | Animation | Keyboard operation, announced state |
| Modal task | Dedicated page or in-flow form | `dialog` | Initial focus, focus return, Escape, background behavior |
| Non-modal transient UI | Visible/in-flow controls | Popover | Dismissal, focus order, anchor behavior |
| Choose one value | Radio buttons or `select` | Styled picker | Labels, selected state, form submission |
| Update authoritative state | Full server response | Server-rendered fragment | Direct endpoint behavior, stale responses, history |

Do not choose an element only because it is new. Use the semantic task, baseline behavior, and project browser policy to make the decision.

## Progressive enhancement contract

Define three layers explicitly:

1. **Semantic baseline:** Complete the task with links, forms, server responses, and an understandable document structure.
2. **Native enhancement:** Add browser features only when the baseline continues to work without them.
3. **Scripted enhancement:** Add the minimum event handling for coordination, partial updates, or presentation.

Do not keep separate copies of the same domain state in HTML, JavaScript, and the server. Use the server response and URL as the authoritative state.

## Server-driven updates

- Return meaningful full pages or clearly limited fragments. Follow the established framework conventions.
- Preserve validation messages, focus, loading feedback, and error recovery.
- Decide whether an update creates, replaces, or preserves a history entry.
- Stop polling or streaming after removal of the containing interface.
- Also stop after the process reaches its final state.
- If an enhancement library is unavailable, use navigation or form submission. Do not leave a control that does not work.

## Validation matrix

- Keyboard-only completion, including predictable focus after open, close, validation, and replacement
- Accessible names, landmarks, headings, labels, descriptions, and error associations
- Screen-reader state changes only where native announcements are insufficient
- No-JavaScript or failed-script completion of the primary task
- Back, forward, refresh, copied URLs, modified link clicks, and duplicate form submission
- Reduced motion, zoom/reflow, touch targets, and narrow viewports
- Supported-browser behavior verified from current primary documentation
- Server errors, timeouts, stale partial responses, and interrupted network requests
