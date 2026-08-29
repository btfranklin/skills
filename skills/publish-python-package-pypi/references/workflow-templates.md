# PyPI Workflow Patterns

Use these examples as structural patterns. Do not copy their version references without verification. Before implementation, verify current action references in the official repositories. Apply the target repository's action-pinning policy.

Primary sources:

- [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/)
- [GitHub OIDC security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [`pdm-project/setup-pdm`](https://github.com/pdm-project/setup-pdm)
- [`pypa/gh-action-pypi-publish`](https://github.com/pypa/gh-action-pypi-publish)

## Publish on an approved release event

Replace every `<verified-...-ref>` after you check the current upstream release and repository policy.

```yaml
name: Upload Python Package

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: release
    permissions:
      id-token: write
    steps:
      - uses: actions/checkout@<verified-checkout-ref>
      - uses: pdm-project/setup-pdm@<verified-setup-pdm-ref>
        with:
          python-version: "<supported-python-version>"
      - run: pdm build
      - uses: pypa/gh-action-pypi-publish@<verified-publish-ref>
```

Keep `id-token: write` at job scope. Add `fetch-depth: 0` only when the build requires repository history.

## Package CI

Derive the Python matrix and commands from `pyproject.toml` and existing scripts.

```yaml
name: Python package

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["<supported-version>"]
    steps:
      - uses: actions/checkout@<verified-checkout-ref>
      - uses: pdm-project/setup-pdm@<verified-setup-pdm-ref>
        with:
          python-version: ${{ matrix.python-version }}
          cache: true
      - run: pdm install --group dev
      - run: pdm run <repository-check-command>
      - run: pdm run <repository-test-command>
```

Do not assume Ruff, pytest, a `src/` layout, or a particular default branch unless the repository establishes them.

## Optional release-note automation

Keep release-note generation separate from publication. If the user requests release-note generation, use the repository's established release tool. Grant only the permissions that the tool requires. Document each required secret. Do not make an AI service credential a prerequisite for Trusted Publishing.

## Adaptation checklist

- Confirm package metadata and `pdm build` output.
- Verify supported Python versions and repository commands.
- Verify current action references from primary upstream sources.
- Confirm the release event and default branch behavior.
- Match the PyPI publisher owner, repository, workflow filename, and environment.
- Validate YAML and inspect effective job permissions.
- Distinguish local validation from live GitHub/PyPI state.
