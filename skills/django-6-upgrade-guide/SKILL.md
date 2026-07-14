---
name: django-6-upgrade-guide
description: >-
  Use when planning, auditing, or executing a Django 5.x to Django 6 upgrade. Covers runtime and dependency compatibility, deprecations, settings, databases, migrations, tests, deployment, and feature adoption. Excludes generic Django work, earlier upgrades, frontend styling, and unrelated maintenance. Produces a repo-grounded checklist, risk report, or patch with verified requirements, staged validation, and rollback guidance.
---

# Django 6 Upgrade Guide

## Workflow

1. Inspect the repository's Django and Python constraints, dependency manager, settings modules, databases, deployment images, CI matrix, third-party packages, and release process.
2. Verify current supported Python versions, the current Django 5.2 and 6.0 patch releases, relevant security notices, and third-party compatibility from primary sources.
3. Establish a clean baseline on the latest compatible Django 5.2 patch. Run the full test suite, Django system checks, migrations check, and representative production commands.
4. Run tests with deprecation warnings visible. Remove project-owned deprecated usage before changing the major version; distinguish dependency warnings from application warnings.
5. Update Python and dependencies in an order that keeps failures attributable. Follow the repository's package-management policy and inspect lockfile changes.
6. Upgrade Django, regenerate no migrations blindly, and review settings, middleware, templates, URLs, forms, authentication, storage, database behavior, and deployment startup.
7. Validate locally and in CI, then define staging checks, observability, rollout order, and rollback constraints. Adopt new Django 6 features only after compatibility is established.

## Evidence and decisions

- Record the discovered baseline, verified target patch, documentation date, incompatible dependencies, warning inventory, migration impact, and unresolved risks.
- Prefer official Django release notes, topic guides, deployment checklists, and package maintainers' compatibility declarations.
- Never infer production safety from import success or a passing unit subset. Exercise migrations, static assets, background work, management commands, and database-specific paths used by the service.
- Treat schema reversibility and application rollback separately; a deploy may require a forward fix even when code rollback is possible.

## Freshness

Do not freeze “latest,” Python support, security status, or third-party compatibility in the skill. Verify them during each upgrade and include the checked versions, sources, and date in the output.

## Resource

Read [references/django-6-upgrade.md](references/django-6-upgrade.md) when building the compatibility inventory, warning pass, migration review, or rollout checklist. Load it only for an actual upgrade or audit.

## Output

Return the requested patch, upgrade plan, or audit. Separate confirmed blockers, risks requiring validation, and optional Django 6 adoption opportunities. Ask only about choices that cannot be resolved from the repository or current primary documentation.
