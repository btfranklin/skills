# Public Skills

This repository contains reusable skills for AI agents. Each skill is in
`skills/<skill-name>/`.

## Install a skill

Replace `<skill-name>` with a name from the catalog:

```bash
npx skills add btfranklin/skills --skill <skill-name> -g
```

Omit `-g` to install the skill only in the current project.

## Skill catalog

The `description` field in each `SKILL.md` is the source of truth for the
skill's trigger, scope, exclusions, and output.

| Skill |
| --- |
| [`deep-code-elegance-and-beauty-review`](skills/deep-code-elegance-and-beauty-review/SKILL.md) |
| [`deep-codebase-review`](skills/deep-codebase-review/SKILL.md) |
| [`design-html-first-web-uis`](skills/design-html-first-web-uis/SKILL.md) |
| [`design-ui-style-guide`](skills/design-ui-style-guide/SKILL.md) |
| [`django-6-upgrade-guide`](skills/django-6-upgrade-guide/SKILL.md) |
| [`django-pytest-performance-suite`](skills/django-pytest-performance-suite/SKILL.md) |
| [`integrate-daisyui-into-django`](skills/integrate-daisyui-into-django/SKILL.md) |
| [`llms-txt-authoring`](skills/llms-txt-authoring/SKILL.md) |
| [`make-repo-agent-legible`](skills/make-repo-agent-legible/SKILL.md) |
| [`openai-django-webhooks`](skills/openai-django-webhooks/SKILL.md) |
| [`publish-npm-package`](skills/publish-npm-package/SKILL.md) |
| [`publish-python-package-pypi`](skills/publish-python-package-pypi/SKILL.md) |
| [`review-agent-production-readiness`](skills/review-agent-production-readiness/SKILL.md) |
| [`skill-icon-workflow`](skills/skill-icon-workflow/SKILL.md) |
| [`structured-llm-output`](skills/structured-llm-output/SKILL.md) |

## Repository workflow

Use these files for each skill:

- `SKILL.md` is required. Its frontmatter name must match the skill directory.
  Its description is the authoritative trigger and scope.
- `agents/openai.yaml` is required in this repository. It contains the display
  name, short description, default prompt, and icon paths.
- `assets/` must contain the SVG and PNG files named in `agents/openai.yaml`.
- `LICENSE.txt` is required so that the skill directory can be distributed by
  itself.
- `references/`, `examples/`, and `templates/` are optional. Add them only when
  the skill needs progressive disclosure or reusable material.
- `evals/evals.json` is optional for a simple skill. Add it when trigger
  boundaries, approval gates, fallbacks, or failure behavior need regression
  coverage.

Keep detailed behavior in one authoritative file. Link to that file instead of
copying its content into the README or another skill file.

Before you publish a change, run:

```bash
python3 scripts/validate_repository.py
```

The validator checks repository structure, frontmatter, metadata, icon paths,
local Markdown links, eval JSON, and the README catalog. It validates the eval
file structure, but it does not execute behavioral evals. Run behavioral evals
in the agent harness that will use the skill.
