---
name: design-html-first-web-uis
description: >-
  Use when the user wants to design or implement a modern web UI with semantic HTML, native browser features, progressive enhancement, server-rendered or server-driven partial updates, and minimal JavaScript. Especially use when replacing SPA-style widgets with dialogs, popovers, forms, details/summary, view transitions, URL-backed state, or lightweight enhancement libraries. Do not use for visual redesign from whole cloth, heavy React/Vue/Svelte app architecture, canvas/WebGL games, Django+DaisyUI integration, or browser-only debugging after a UI already exists. Output an implementation plan or patch that names the native patterns used, accessibility behavior, graceful degradation, testing implications, and any necessary JavaScript.
---

- Read references/modern-web-uis-without-frameworks-advanced-html-first-patterns-for-2026_20260110_070702.md first; treat it as the authoritative source of truth for all technical details, tradeoffs, and recommendations.
- Identify the users requested UI capability and map it to the most relevant reference section(s): HTML-First Development in 2026 (html-first-2026), Modern HTML Features for UI Composition (native-features), Interaction Patterns with Minimal JavaScript (interaction-patterns), Server-Driven UI and Partial Updates (server-driven), Quality, Performance, and Maintainability Considerations (quality).
- Prefer semantic HTML and native browser behavior; add JavaScript only where the reference indicates it is necessary, and describe any progressive enhancement and graceful degradation behavior explicitly.
- Provide implementation guidance as HTML-first patterns (forms, links, dialogs/popovers, attribute-driven state, URL-driven state), and use server-driven partial updates where applicable; cite or quote the relevant reference sections by exact title/ID in the response.
- Validate the proposed solution against accessibility, performance, and maintainability constraints using Quality, Performance, and Maintainability Considerations (quality); call out keyboard/screen reader behavior, payload size implications, and testing considerations as supported by the reference.
- If information is missing or ambiguous, ask targeted clarifying questions and then re-check the reference file before finalizing the design or code.
