---
name: integrate-daisyui-into-django
description: >-
  Use when integrating or refactoring Tailwind CSS and DaisyUI in a Django application. Covers the asset pipeline, template and component boundaries, theme tokens, optional theme switching, migration, and verification. Excludes isolated template edits, non-Django work, visual direction, and backend-only tasks. Produces repo-specific code or a plan that preserves existing conventions and identifies ownership and checks.
---

# Integrate DaisyUI into Django

## Workflow

1. Inspect the repository's Django version, package managers, template layout, static-file pipeline, deployment build, CSS and JavaScript entrypoints, component conventions, CSP, and existing Tailwind or DaisyUI configuration.
2. Verify current installation and configuration guidance in official Tailwind CSS and DaisyUI documentation. Follow the project's existing toolchain when it is viable; do not introduce a second asset pipeline casually.
3. Choose one CSS entrypoint and one deterministic build command. Ensure template files are included in content detection and generated assets flow through Django's established static-file handling.
4. Define ownership: Django templates hold semantics and server data, the CSS entrypoint holds framework imports and intentional overrides, reusable template components hold repeated markup, and scripts hold behavior that native HTML cannot provide.
5. Define semantic theme tokens before component-specific styling. Add theme switching only when requested, with an explicit default, persistence policy, and no-script behavior.
6. Migrate incrementally, removing superseded assets and configuration outright. Validate development, CI, production build, collected assets, accessibility, and representative rendered pages.

## Decisions

- Preserve established repository conventions and supported versions unless the task explicitly includes changing them.
- Prefer Django template inclusion or the project's existing component system. Do not add a component package solely to wrap every DaisyUI class combination.
- Keep business rules and authorization in Django, not in CSS classes or browser scripts.
- Use native HTML first. If the repository already uses HTMX or Hyperscript, integrate through its existing request and event conventions; do not introduce Alpine or another enhancement library by default.
- Keep generated CSS out of hand-edited source and avoid broad global overrides that fight DaisyUI component contracts.

## Freshness

Tailwind CSS and DaisyUI installation, plugin syntax, content detection, theme configuration, and supported package versions are time-sensitive. Verify them from current official documentation and inspect the resolved packages before editing. Record checked sources, versions, and date in plans or audit reports.

## Resource

Read [references/django-daisyui-patterns.md](references/django-daisyui-patterns.md) when choosing the build pipeline, component boundary, theme model, migration sequence, or validation matrix. Load it only when those details affect the task.

## Output

Return a repo-specific patch or plan covering the chosen pipeline, source/generated file ownership, template component convention, theme behavior, migration sequence, and executed or proposed checks. Ask only when a material product or deployment choice remains undiscoverable.
