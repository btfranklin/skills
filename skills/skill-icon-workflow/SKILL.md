---
name: skill-icon-workflow
description: >-
  Use when creating, updating, validating, or wiring Codex skill icons, including the small SVG, 100x100 PNG, and `agents/openai.yaml` fields. Covers generation, conversion, repair, metadata wiring, and visual checks. Do not use for app icons, favicons, badges, unrelated artwork, or general skill authoring without an icon task. Return correctly placed assets, skill-relative paths, deterministic checks, and rendered verification.
---

# Skill Icon Workflow

Handle the icon-specific portion of skill creation or maintenance. Pair this with `skill-creator` when the skill instructions or broader metadata also change.

## Workflow

1. Read [references/icon-workflow.md](references/icon-workflow.md) for the asset and validation contract.
2. Inspect the existing skill assets and `agents/openai.yaml`; preserve the established visual identity when repairing or converting icons.
3. Keep the editable design source and `icon_small` as SVG. Export `icon_large` from that source as a 100x100 PNG.
4. Store both assets in the target skill's `assets/` directory and wire paths relative to the skill directory.
5. Validate SVG structure, PNG format and dimensions, YAML syntax, file existence, and rendered appearance at small size.
6. Limit metadata changes to icon fields unless the broader task explicitly includes metadata maintenance.

Use `imagegen` when the request requires new artwork or visual concepts; conversion and wiring alone do not require it.

## Freshness

Before changing Codex metadata conventions, verify the current official skill-authoring guidance available in the environment. Record the convention or source consulted when it changes the implementation; do not treat an older local example as permanently authoritative.

## Guardrails

- Use a full-bleed background unless transparency is intentional.
- Prefer simple silhouettes and strong contrast over detail that disappears at small sizes.
- Preserve gradients and alpha through export.
- Never accept file extension alone as proof of format or dimensions.

## Output

Report the assets created or changed, metadata paths, structural checks, image dimensions, and visual-render result.
