# HTML-First Patterns

Use this reference to choose an interaction primitive and define its enhancement boundary. Verify version-sensitive behavior against the linked primary documentation at execution time.

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

Do not choose a primitive solely because it is new. The semantic task, baseline behavior, and project browser policy decide.

## Progressive enhancement contract

Define three layers explicitly:

1. **Semantic baseline:** complete the task with links, forms, server responses, and understandable document structure.
2. **Native enhancement:** add browser features whose absence leaves the baseline intact.
3. **Scripted enhancement:** add the smallest event handling needed for orchestration, partial updates, or presentation.

Avoid maintaining the same domain state independently in HTML, JavaScript, and the server. Prefer the server response and URL as shared truth.

## Server-driven updates

- Return meaningful full pages or clearly scoped fragments according to the framework's established conventions.
- Preserve validation messages, focus, loading feedback, and error recovery.
- Decide whether an update creates, replaces, or preserves a history entry.
- Make polling and streaming lifecycle-aware; stop work when the containing UI is removed or the terminal state is reached.
- Ensure an unavailable enhancement library degrades to navigation or form submission rather than a dead control.

## Validation matrix

- Keyboard-only completion, including predictable focus after open, close, validation, and replacement
- Accessible names, landmarks, headings, labels, descriptions, and error associations
- Screen-reader state changes only where native announcements are insufficient
- No-JavaScript or failed-script completion of the primary task
- Back, forward, refresh, copied URLs, modified link clicks, and duplicate form submission
- Reduced motion, zoom/reflow, touch targets, and narrow viewports
- Supported-browser behavior verified from current primary documentation
- Server errors, timeouts, stale partial responses, and interrupted network requests
