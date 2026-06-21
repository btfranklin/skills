# Public Skills

This repository contains a public set of useful AI agent skills designed to be reused across projects.

The skills live under `skills/` and are intended to be installable from a public GitHub repository via tools such as `npx skills`.

Before publishing skill metadata changes, verify discovery-safe frontmatter lengths:

```bash
python3 scripts/check_skill_frontmatter_lengths.py skills
```

## Skills

- `review-agent-production-readiness`
  Review and harden OpenAI Agents SDK systems for production readiness, including architecture risk, tool safety, eval coverage, tracing, monitoring, rollout, cost/latency, privacy, compliance, and human oversight.

  ```bash
  npx skills add btfranklin/skills --skill review-agent-production-readiness -g
  ```

- `deep-codebase-review`
  Perform a comprehensive structural sub-agent council review of a codebase or substantial PR by default, focused on cruft, duplication, clean code shape, weak boundaries, lifecycle risks, testing gaps, and design drift.

  ```bash
  npx skills add btfranklin/skills --skill deep-codebase-review -g
  ```

- `deep-code-elegance-and-beauty-review`
  Review one code project as an artifact of thought, craft, and maintenance experience, focusing on cognitive clarity, design elegance, developer joy, naming, locality, and what should be protected.

  ```bash
  npx skills add btfranklin/skills --skill deep-code-elegance-and-beauty-review -g
  ```

- `design-html-first-web-uis`
  Design modern interactive web interfaces with HTML-first patterns, native browser features, progressive enhancement, and minimal JavaScript.

  ```bash
  npx skills add btfranklin/skills --skill design-html-first-web-uis -g
  ```

- `django-6-upgrade-guide`
  Plan and execute Django 6 upgrades, including breaking changes, compatibility checks, and migration checklists from Django 5.

  ```bash
  npx skills add btfranklin/skills --skill django-6-upgrade-guide -g
  ```

- `django-pytest-performance-suite`
  Build Postgres-backed Django performance regression suites with pytest, pytest-django, RequestFactory, timing budgets, query caps, and reproducible artifact reports.

  ```bash
  npx skills add btfranklin/skills --skill django-pytest-performance-suite -g
  ```

- `integrate-daisyui-into-django`
  Build and maintain a Django + Tailwind/DaisyUI setup with clear separation of concerns, reusable template patterns, and sustainable theming decisions.

  ```bash
  npx skills add btfranklin/skills --skill integrate-daisyui-into-django -g
  ```

- `llms-txt-authoring`
  Create or review `llms.txt` files for a site root, including structure, content, and recommended conventions.

  ```bash
  npx skills add btfranklin/skills --skill llms-txt-authoring -g
  ```

- `make-repo-agent-legible`
  Improve a repository's legibility for coding agents by moving implicit knowledge into discoverable in-repo artifacts, tightening `AGENTS.md`, and making constraints mechanically enforceable.

  ```bash
  npx skills add btfranklin/skills --skill make-repo-agent-legible -g
  ```

- `openai-django-webhooks`
  Implement OpenAI Responses API async workflows in Django, including background jobs, webhook verification, HTMX polling, and metadata fallback handling.

  ```bash
  npx skills add btfranklin/skills --skill openai-django-webhooks -g
  ```

- `publish-python-package-pypi`
  Configure and maintain GitHub Actions workflows for publishing Python packages to PyPI with PDM and Trusted Publishing.

  ```bash
  npx skills add btfranklin/skills --skill publish-python-package-pypi -g
  ```

- `skill-icon-workflow`
  Create or update skill icon assets and wire `icon_small` and `icon_large` correctly in `agents/openai.yaml`, especially when icon generation is part of skill creation.

  ```bash
  npx skills add btfranklin/skills --skill skill-icon-workflow -g
  ```

- `structured-llm-output`
  Design structured LLM output workflows using schema-driven validation patterns with tools such as Pydantic, PydanticAI, and Instructor.

  ```bash
  npx skills add btfranklin/skills --skill structured-llm-output -g
  ```
