# Django 6 Upgrade Reference

Use this checklist after inspecting the target repository. Verify every version-sensitive statement at execution time.

## Primary sources

- [Django 6.0 release notes](https://docs.djangoproject.com/en/6.0/releases/6.0/)
- [Django 5.2 release notes](https://docs.djangoproject.com/en/5.2/releases/5.2/)
- [How to upgrade Django](https://docs.djangoproject.com/en/6.0/howto/upgrade-version/)
- [Deprecation timeline](https://docs.djangoproject.com/en/6.0/internals/deprecation/)
- [Deployment checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)
- [Supported versions](https://www.djangoproject.com/download/#supported-versions)
- Package maintainers' release notes and compatibility classifiers for each direct dependency

Use the documentation for the current patch release. Do not use only the initial major-release page. Check security advisories separately.

## Baseline inventory

Capture:

- Python and Django limits in project metadata and lockfiles
- Runtime and CI Python versions, base images, buildpacks, and deployment platform
- Installed direct dependencies and Django integration packages
- Databases, drivers, routers, caches, storage backends, email, authentication, and middleware
- Settings variants and environment-dependent code paths
- Migrations, custom fields, custom backends, template engines, management commands, and admin customizations
- ASGI/WSGI servers, background workers, scheduled work, and health checks
- Current test, lint, type-check, system-check, and release commands

## Staged upgrade

### Stabilize on Django 5.2

- Move to the latest compatible 5.2 patch according to current official documentation.
- Run `manage.py check`, `manage.py makemigrations --check --dry-run`, the full tests, and production-representative commands.
- Run tests with Python warnings enabled, commonly `python -Wa manage.py test` or the repository's equivalent.
- Fix project-owned deprecations. Track dependency-owned warnings by package and compatible release.

### Confirm compatibility

- Verify the Django 6 Python requirement against local, CI, and production runtimes.
- Check every Django-facing direct dependency from its maintainer's current documentation.
- Review database backend support and database-version requirements.
- Read all applicable Django 6 backwards-incompatible changes and removed deprecations.
- Decide whether the upgrade requires dependency replacement or removal. Do not add compatibility shims.

### Upgrade and review

- Update dependency limits through the repository's package manager. Inspect the resolved dependency changes.
- Run checks before creating migrations. Any new migration must correspond to an intentional model-state change.
- Inspect settings defaults, request/response behavior, URL routing, forms, templates, authentication, storage, serialization, admin, and localization used by the application.
- Exercise database-specific behavior and all deployed process types.

## Validation and rollout

- Run the full CI-equivalent suite on the supported Python/database matrix.
- Test migration forward behavior on a production-like copy or representative fixture.
- Perform basic staging tests for critical user tasks, admin operations, static and media handling, background work, and deployment startup.
- Compare logs, error rate, latency, database queries, task failures, and resource use with the baseline.
- Document the code rollback procedure. Document the schema rollback or forward-fix procedure. Record the deployment order and the point after which rollback is not safe.

## Django 6 features

Treat feature adoption as a separate follow-up. Confirm the upgrade first, then evaluate features such as the Tasks framework against current official documentation and project operations. Do not imply that Django supplies an external worker or production execution backend unless current documentation explicitly says so.
