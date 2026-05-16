---
name: skill-icon-workflow
description: >-
  Use when creating, updating, validating, or wiring Codex skill icon assets, especially `icon_small` SVG and `icon_large` 100x100 PNG entries in `agents/openai.yaml`, or when icon generation is part of skill creation/maintenance. Do not use for general app icons, favicons, README badges, non-skill artwork, or broader skill authoring without an icon task; pair with `skill-creator` when the skill itself also needs changes. Output correctly placed assets, relative YAML paths, render/size checks, and narrowly scoped metadata changes.
---

# Skill Icon Workflow

Use this skill for the icon-specific part of Codex skill creation or maintenance. If the task also involves creating or updating the skill itself, use this alongside `skill-creator`.

## Workflow

1. Read [references/icon-workflow.md](references/icon-workflow.md) before creating or wiring icon assets.
2. Keep the design source and `icon_small` as SVG.
3. Export `icon_large` as a 100x100 PNG derived from the SVG.
4. Save both files under the target skill's `assets/` directory and wire them in `agents/openai.yaml`.
5. If the user needs new icon artwork rather than a file conversion, also use `imagegen` for concept generation, then produce the final SVG and PNG pair using the conventions in the reference.
6. If `agents/openai.yaml` already exists, limit changes to the icon fields unless the broader task requires more metadata updates.

## Guardrails

- Use a full-bleed background so the icon does not render with an inset border.
- Prefer simple, legible shapes over fine detail that will disappear at small sizes.
- Keep paths in `agents/openai.yaml` relative to that file.
- If the large icon renders as a gray box or loses gradients, check the troubleshooting notes in `references/icon-workflow.md`.

## Reference

- [references/icon-workflow.md](references/icon-workflow.md) for sizing, export, YAML wiring, and troubleshooting.
