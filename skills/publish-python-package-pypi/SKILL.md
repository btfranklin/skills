---
name: publish-python-package-pypi
description: >-
  Use when configuring or troubleshooting PyPI publishing for PDM packages with GitHub Actions and Trusted Publishing, including release events, OIDC permissions, builds, and repository/PyPI settings. Do not use for applications, non-Python projects, generic CI, containers, or token uploads unless requested. Return scoped workflow changes, required settings, validation results, and external steps.
---

# Publish Python Packages to PyPI

Build a release path that is minimal, inspectable, and consistent with the package's existing conventions.

## Workflow

1. Confirm that the repository produces a distributable Python package and uses PDM.
2. Inspect `pyproject.toml`, supported Python versions, existing workflows, release conventions, and repository instructions before proposing changes.
3. Run `pdm build`; inspect the wheel and source distribution when package contents are material to the request.
4. Configure publishing around PyPI Trusted Publishing:
   - trigger publication from the repository's approved release event;
   - grant `id-token: write` only to the publishing job;
   - keep ordinary repository permissions read-only;
   - align the workflow filename, GitHub environment, and PyPI publisher mapping exactly.
5. Keep CI, release-note generation, and package publication separate. Add optional release-note automation only when requested or already established by the repository.
6. Validate YAML, package builds, permissions, event semantics, and all manual GitHub/PyPI configuration. Do not claim that external settings or a live publication were verified when they were not.

## Freshness

Before changing action references, Python matrices, PDM setup, or Trusted Publishing configuration, check the current primary documentation and upstream releases. Follow repository pinning or SHA policies when present. Otherwise use a current supported action reference verified during the task; never describe a frozen reference as “latest.” Record the relevant versions or verification date in the result when they affect the change.

## Guardrails

- Use PDM for environments, dependency installation, builds, and project commands.
- Do not introduce a long-lived PyPI token unless the user explicitly requires token-based publishing.
- Do not create or push tags, publish releases, alter repository settings, or perform a live upload without explicit authorization.
- Match the project's supported Python versions instead of imposing a global matrix.
- Preserve existing workflow names and conventions unless changing them is necessary to fix the release path.

## Resources

- Read [references/workflow-templates.md](references/workflow-templates.md) when creating or substantially restructuring GitHub Actions workflows. Adapt the patterns after verifying current action references.

## Output

Report:

1. Existing release coverage and gaps.
2. Workflow changes and why each permission or event is required.
3. Manual GitHub and PyPI settings.
4. Local validation results and anything that remains externally unverifiable.
5. Authorized next steps, clearly separating configuration from live release actions.
