---
name: integrate-daisyui-into-django
description: >-
  Use when integrating or refactoring Tailwind CSS and DaisyUI in a Django application. Covers the asset pipeline, template and component boundaries, theme tokens, optional theme switching, migration, and verification. Excludes isolated template edits, non-Django work, visual direction, and backend-only tasks. Produces repo-specific code or a plan that preserves existing conventions and identifies ownership and checks.
---

# Integrate DaisyUI into Django

## Workflow

1. Inspect the Django version, package managers, template layout, and component conventions. Inspect the static-file pipeline, deployment build, CSS and JavaScript entrypoints, CSP, and existing Tailwind or DaisyUI configuration.
2. Verify current installation and configuration guidance in the official Tailwind CSS and DaisyUI documentation.
3. Use the existing asset pipeline when it supports the required Tailwind CSS and DaisyUI configuration. If it does not support the required configuration, identify the exact limitation before you replace it. Do not add a second asset pipeline.
4. Choose one CSS entrypoint and one deterministic build command. Include all template sources in content detection. Send generated assets through Django's established static-file handling.
5. Define file ownership. Django templates hold semantics and server data. The CSS entrypoint holds framework imports and intentional overrides. Reusable template components hold repeated markup. Scripts hold only behavior that native HTML cannot provide.
6. Define semantic theme tokens before component-specific styles. Add theme switching only when the user requests it. Define the default theme, persistence policy, and no-script behavior.
7. Migrate one representative page before broad migration. Verify the new pipeline and component convention. Then migrate the remaining pages. Remove superseded assets and configuration only after their replacements pass the required checks.
8. Validate the development build, CI build, production build, and collected assets. Check accessibility and representative rendered pages.

## Decisions

- Preserve established repository conventions and supported versions unless the task explicitly includes changing them.
- Prefer Django template inclusion or the project's existing component system. Do not add a component package solely to wrap every DaisyUI class combination.
- Keep business rules and authorization in Django, not in CSS classes or browser scripts.
- Use native HTML first. If the repository already uses HTMX or Hyperscript, integrate through its existing request and event conventions; do not introduce Alpine or another enhancement library by default.
- Keep generated CSS out of hand-edited source and avoid broad global overrides that fight DaisyUI component contracts.

## Freshness

Tailwind CSS and DaisyUI installation, plugin syntax, content detection, theme configuration, and supported package versions are time-sensitive. Verify this information in current official documentation. Inspect the resolved packages before you edit the configuration. Record the checked sources, versions, and date in the plan or audit report.

## Resource

Read [references/django-daisyui-patterns.md](references/django-daisyui-patterns.md) when choosing the build pipeline, component boundary, theme model, migration sequence, or validation matrix. Load it only when those details affect the task.

## Output

Return a repo-specific patch or plan covering the chosen pipeline, source/generated file ownership, template component convention, theme behavior, migration sequence, and executed or proposed checks. Ask only when a material product or deployment choice remains undiscoverable.
