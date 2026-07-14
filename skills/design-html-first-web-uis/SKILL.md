---
name: design-html-first-web-uis
description: >-
  Use when designing or implementing HTML-first web interfaces with native browser features, progressive enhancement, server-rendered updates, and minimal JavaScript. Covers forms, dialogs, popovers, disclosure, URL state, and replacing SPA-style interactions. Excludes visual direction, framework architecture, games, and browser debugging. Produces repo-specific code or a plan with accessibility, fallbacks, and validation.
---

# Design HTML-First Web UIs

## Workflow

1. Inspect the existing stack, templates, routes, form handling, JavaScript, CSS, browser targets, and repository guidance. Preserve established conventions.
2. Describe the interaction as links, forms, navigation, disclosure, selection, or transient UI before choosing an implementation.
3. Select the smallest native primitive that preserves server authority and meaningful URLs. Use JavaScript only for enhancement that HTML and CSS cannot express adequately.
4. Define the baseline behavior without enhancement, then add optional native APIs, server-driven partial updates, or small scripts.
5. Implement the narrowest complete change. Keep state in URLs, form controls, or server responses when practical; avoid parallel client-side state.
6. Validate keyboard use, focus, accessible names, error handling, history/navigation, no-JavaScript behavior, and relevant browser support.

## Decisions

- Prefer links for navigation and forms for state-changing requests.
- Prefer `details`/`summary`, `dialog`, and popover behavior when their semantics match the interaction; do not force a native primitive onto a mismatched design.
- Use server-rendered pages or fragments for authoritative application state. Keep partial-update endpoints usable and understandable outside the enhancement layer.
- Preserve normal HTTP behavior: validation errors, redirects, CSRF protection, idempotency expectations, and back/forward navigation.
- Treat animations and view transitions as optional presentation. Respect reduced-motion preferences and never make them necessary for task completion.

## Freshness

When browser support, API syntax, accessibility behavior, or framework integration affects the result, verify it against current MDN, WHATWG, and relevant framework documentation. Record the checked source and date in plans or reports; do not present a remembered support table as current.

## Resource

Read [references/html-first-patterns.md](references/html-first-patterns.md) when selecting a native primitive, designing progressive enhancement, or preparing the validation matrix. Load it only when those details are needed.

## Output

Return a repo-specific patch or plan that names the semantic baseline, enhancement layer, required JavaScript, fallback behavior, accessibility decisions, and verification performed. Ask a question only when an unresolved product choice would materially change the implementation.
