---
name: integrate-daisyui-into-django
description: >-
  Use when starting or refactoring a Django app to use Tailwind and DaisyUI in a maintainable way: asset build pipeline, template/style/script separation, reusable component patterns, custom themes, optional theme switching, and long-term UI checks. Do not use for non-Django frontend work, pure HTML-first design without Tailwind/DaisyUI, one-off template tweaks, product/visual redesign from scratch, or backend-only Django tasks. Output a repo-specific integration plan or patch covering pipeline choice, file ownership, component conventions, theme tokens, accessibility/lint/visual checks, and migration steps.
---

- Consult references/django-daisyui-maintainable-integration-separation-of-concerns-and-custom-theming_20260117_224519.md before answering; treat it as the authoritative source of truth for all domain details.
- Map the user request to the reference sections by using the exact Section index titles/IDs: Architecture & Separation of Concerns (architecture_concerns), Build Pipeline & Asset Management (build_pipeline), Componentization Patterns in Django Templates (component_patterns), Theming with DaisyUI: Custom Themes & Multi-Theme Support (daisyui_theming), Maintainability, Testing, and Governance (maintainability_governance).
- Extract and apply the recommended patterns from the relevant sections; quote or cite the section titles/IDs in the response to ground guidance in the reference.
- Produce a maintainable implementation plan that keeps templates, styles, and scripts separated, chooses an asset pipeline approach, defines reusable template component patterns, and specifies theming/theme-switching behaviors, all aligned to the cited sections.
- Identify missing requirements (deployment constraints, theming needs, component scope, team conventions) and ask targeted clarifying questions, then revise the plan using the same cited reference sections.
