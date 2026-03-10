# Workflow Templates

Derived from repeatable package-repository workflow patterns.

## Contents
1. `python-publish.yml` (PyPI publish on release)
2. `python-package.yml` (CI for package repos)
3. `draft-release-notes.yml` (tag-triggered release draft)
4. Adaptation checklist

## 1) python-publish.yml

```yaml
name: Upload Python Package

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: release
    permissions:
      id-token: write

    steps:
      - uses: actions/checkout@v6.0.1
        with:
          fetch-depth: 0
      - name: Set up Python
        uses: actions/setup-python@v6.1.0
        with:
          python-version: "3.14"
      - name: Install PDM
        run: |
          python -m pip install --upgrade pip
          python -m pip install pdm
      - name: Build package
        run: pdm build
      - name: Publish package
        uses: pypa/gh-action-pypi-publish@v1.13.0
```

Notes:
- `environment: release` is used consistently in package repos.
- `id-token: write` is required for Trusted Publishing.
- Keep `fetch-depth: 0` to ensure full history context.

## 2) python-package.yml

```yaml
name: Python package

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.12", "3.13", "3.14"]

    steps:
      - uses: actions/checkout@v6.0.1
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v6.1.0
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install PDM
        run: |
          python -m pip install --upgrade pip
          python -m pip install pdm
      - name: Install dependencies
        run: pdm install --group dev
      - name: Lint with ruff
        run: pdm run ruff check src tests --statistics
      - name: Test with pytest
        run: pdm run pytest
```

Notes:
- Python matrix varies per repo; align with supported versions in `pyproject.toml`.
- Some repos call `pdm run lint`/`pdm run test` instead of direct ruff/pytest.

## 3) draft-release-notes.yml

```yaml
name: Draft Release Notes

on:
  push:
    tags:
      - "v*.*.*"

permissions:
  contents: write

jobs:
  draft-release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6.0.1
        with:
          fetch-depth: 0
      - name: Generate release notes
        uses: btfranklin/release-notes-scribe@v0
        with:
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          include_github_generated_notes: "true"
```

Notes:
- This workflow is optional for publish itself but common in package repos here.
- Requires `OPENAI_API_KEY` repository or organization secret.
- `GITHUB_TOKEN` is built in to GitHub Actions and requires no manual secret.

## 4) Adaptation Checklist

1. Confirm repo is package/library before adding `python-publish.yml`.
2. Set publish Python version to a supported project version.
3. Verify `pyproject.toml` builds with `pdm build`.
4. Configure PyPI Trusted Publisher:
- Owner/repo
- Workflow file name
- Environment name (`release`)
5. Configure GitHub secrets:
- `OPENAI_API_KEY` for `draft-release-notes.yml` (if used)
6. Confirm GitHub environment `release` exists if approvals/policies are used.
7. Test flow:
- Push `vX.Y.Z` tag (release-notes workflow).
- Publish GitHub release (PyPI publish workflow).
