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

The `description` field in each `SKILL.md` is the authoritative source for the
skill trigger, scope, exclusions, and output.

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

- Each skill must contain `SKILL.md`. Its frontmatter name must match the skill
  directory. Its description is the authoritative trigger and scope.
- Each skill in this repository must contain `agents/openai.yaml`. This file
  contains the display name, short description, default prompt, and icon paths.
- `assets/` must contain the SVG and PNG files named in `agents/openai.yaml`.
- Each skill must contain `LICENSE.txt`. This file permits separate
  distribution of the skill directory.
- `references/`, `examples/`, and `templates/` are optional. Add them only when
  the skill needs progressive disclosure or reusable material.
- `evals/evals.json` is optional for a simple skill. Add it when trigger
  boundaries, approval gates, fallbacks, or failure behavior need regression
  coverage.

Keep detailed behavior in one authoritative file. Link to that file instead of
copying its content into the README or another skill file.

## Writing standard

Use ASD-STE100 Simplified Technical English for all technical prose. Follow the
rules in [`AGENTS.md`](AGENTS.md). Review the language during normal editing and
review. The repository validator does not enforce this writing standard.

Before you publish a change, run:

```bash
python3 scripts/validate_repository.py
```

The validator checks repository structure, frontmatter, metadata, icon paths,
local Markdown links, eval JSON, and the README catalog. It validates the eval
file structure, but it does not execute behavioral evals. Run behavioral evals
in the agent harness that will use the skill.

Run the deterministic example checks with PDM:

```bash
pdm sync -G test
pdm run test
```

These checks execute the published invoice schema and arithmetic code. They also
execute the webhook endpoint function with a SQLite receipt store and a controlled
queue. They cover queue failure after commit, repeated delivery, uncertain queue
acceptance, missing invoice values, currency conflicts, and arithmetic errors.
Specific instruction checks protect the database-engine rule and optional-skill
fallback. These are contract checks, not automated writing-style checks.

CI runs both the repository validator and these checks. The checks do not call a
model or an external service. They do not replace Django integration tests,
provider tests, or agent-level evaluations from `evals/evals.json`. Run those
evaluations in the target agent harness and record the inputs, tool calls,
results, and unmet expectations. Do not report the deterministic checks as proof
that an agent followed the instructions.
