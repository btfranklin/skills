# Skill Icon Asset Contract

## Files and metadata

- Store `assets/<skill-name>.svg` as the editable small icon.
- Store `assets/<skill-name>.png` as a 100x100 large icon derived from the SVG.
- Resolve `agents/openai.yaml` icon paths from the skill directory:

```yaml
interface:
  icon_small: "./assets/<skill-name>.svg"
  icon_large: "./assets/<skill-name>.png"
```

Confirm current path and metadata conventions in the official skill-authoring guidance before changing them.

## Design

- Use a square SVG view box. Use `0 0 512 512` unless the existing design requires a different square view box.
- Extend intentional backgrounds to every edge to avoid an accidental inset tile.
- Keep the focal shape readable at 16–32 pixels.
- Use transparency only when it is part of the design.
- Treat the SVG as the authoritative source. Regenerate the PNG after you change the SVG.

## Export

Use an available SVG renderer that preserves gradients and alpha. On macOS, Quick Look can produce a preview. Verify the result before you accept the conversion:

```bash
qlmanage -t -s 100 -o /tmp assets/<skill-name>.svg
```

Move the generated preview into `assets/<skill-name>.png` only after you check its format and dimensions. You can use another renderer when it meets the same requirements.

## Deterministic validation

1. Parse the SVG as XML.
2. Confirm the SVG view box and full-bleed geometry when a background is expected.
3. Identify the PNG by file contents and confirm it is exactly 100x100.
4. Parse `agents/openai.yaml` and resolve both paths from the skill directory.
5. Render or open both files. Inspect contrast, cropping, gradients, transparency, and legibility at a small size.

## Troubleshooting

- **Gray or flat PNG:** use a renderer with gradient support and regenerate from the SVG.
- **Inset border:** extend the background to the full view box before re-exporting.
- **Soft or cropped subject:** simplify the design or increase the clear area around the subject. Then inspect the result at its actual display size.
- **Missing icon:** correct the skill-relative YAML path and confirm exact filename casing.
