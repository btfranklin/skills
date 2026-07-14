---
name: publish-python-package-pypi
description: >-
  Use when configuring, auditing, migrating, or troubleshooting PyPI publishing for Python package repositories that use PDM and GitHub Actions, especially Trusted Publishing/OIDC, release-triggered publish workflows, draft release notes, and tag-to-release delivery. Do not use for application/service repos that are not published to PyPI, non-Python packages, container deployments, manual Twine token setup unless explicitly requested, or generic CI unrelated to release publishing. Output exact workflow patches plus PyPI/GitHub settings, local build validation, event sanity checks, and any release-path steps that cannot be verified locally.
---

# Publish Python Package Pypi

## Overview

Implement a consistent release pipeline for Python packages: CI on push/PR, draft release notes on version tags, and PyPI publish on release publication. Follow the workflow patterns captured in `references/workflow-templates.md`.

## Baseline Pattern

For package repos, maintain these workflow files:
- `.github/workflows/python-package.yml`
- `.github/workflows/create-draft-release.yml`
- `.github/workflows/python-publish.yml`

Use `references/workflow-templates.md` for canonical templates and version-pinned actions.

## Workflow

1. Identify repository type.
- If repo is an app/service (not a PyPI package), do not add `python-publish.yml` by default.
- If repo is a package/library, continue.

2. Inspect package metadata before workflow changes.
- Confirm `pyproject.toml` has package metadata suitable for publishing.
- Confirm build works locally: `pdm build`.

3. Configure PyPI Trusted Publisher requirements.
- In PyPI project settings, add a Trusted Publisher for this GitHub repository/workflow.
- Use environment `release` in workflow and repository environment settings.
- Do not introduce long-lived PyPI API tokens unless explicitly requested.

4. Add or update `.github/workflows/python-publish.yml`.
- Trigger: `on: release: types: [published]`.
- Permissions: `contents: read` and job-level `id-token: write`.
- Steps: checkout (full history), setup python, install pdm, `pdm build`, `pypa/gh-action-pypi-publish`.
- Keep publish job minimal and deterministic.

5. Ensure CI and draft-release workflows exist.
- `python-package.yml` should test/lint on push and PR.
- `create-draft-release.yml` should trigger on `v*.*.*` tag pushes.
- Keep action versions aligned with repo standards.

6. Validate end-to-end.
- Validate workflow files: `gh workflow list`.
- Validate package build: `pdm build`.
- Validate release path:
  - Push tag `vX.Y.Z` to trigger release notes draft.
  - Publish GitHub release to trigger PyPI publish workflow.
- Check Actions run logs and PyPI project page.

## Required GitHub/PyPI Configuration

1. GitHub Actions secrets:
- Add repository (or org-level) secret `OPENAI_API_KEY` when using `create-draft-release.yml`.
- `GITHUB_TOKEN` is provided automatically by Actions and does not need manual creation.

2. GitHub environment:
- Create/configure environment `release` if using environment protections.
- Ensure the publish job can run in `release` (reviewers/rules must allow it).

3. PyPI Trusted Publisher:
- In PyPI project settings, register the GitHub repository/workflow/environment used by `python-publish.yml`.
- Do not add `PYPI_API_TOKEN` for trusted publishing unless explicitly requested.

## Repo Conventions

- Use `actions/checkout@v6.0.1`, `actions/setup-python@v6.1.0`, and `pypa/gh-action-pypi-publish@v1.13.0` unless a user asks to change versions.
- Install tooling with:
  - `python -m pip install --upgrade pip`
  - `python -m pip install pdm`
- Match the publish workflow Python version to project support policy. This can vary (`3.10`, `3.11`, `3.12`, `3.14`), so do not hardcode one global value.

## Troubleshooting

1. `Trusted publishing exchange failure`:
- Confirm `id-token: write` exists at job level.
- Confirm PyPI trusted publisher repository/workflow/environment names match exactly.
- Confirm workflow ran from the expected repository and branch/release context.

2. Workflow did not run:
- Confirm event type (`release.published`) and that release is published, not draft only.
- Confirm workflow file exists on default branch.

3. Build artifact problems:
- Run `pdm build` locally and inspect `dist/`.
- Confirm package metadata and included files are correct.

### references/
- `references/workflow-templates.md`: canonical workflow templates and adaptation notes for package repositories.

## Output Expectations

When applying this skill, produce:
1. A short summary of current workflow coverage and gaps.
2. Exact workflow file patches.
3. Any required PyPI/GitHub settings that must be configured manually.
4. Validation results (`pdm build`, workflow/event sanity, and what was not verifiable locally).
5. A checklist of required GitHub/PyPI settings (`OPENAI_API_KEY`, `release` environment, trusted publisher mapping).
