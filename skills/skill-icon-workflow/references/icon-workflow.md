# Icon Workflow

Use this workflow when a skill needs `icon_small` and `icon_large` in `agents/openai.yaml`.

## Constraints

- Keep `icon_small` as SVG.
- Use PNG for `icon_large` because the UI may not render gradient SVGs correctly for the large icon.
- Use a full-bleed background to avoid inset borders in the UI.

## SVG design checklist

- Canvas: 512x512.
- Background: full-bleed rect, for example `<rect x="0" y="0" width="512" height="512" rx="64" ... />`.
- Gradients are allowed. SVG is the source of truth for the design.
- Save to `assets/<skill-name>.svg`.

## PNG export for `icon_large`

Export a 100x100 PNG from the SVG and save it as `assets/<skill-name>.png`.

Example on macOS with Quick Look:

```bash
qlmanage -t -s 100 -o /tmp assets/<skill-name>.svg
mv /tmp/<skill-name>.svg.png assets/<skill-name>.png
```

## `openai.yaml` wiring

```yaml
interface:
  icon_small: "./assets/<skill-name>.svg"
  icon_large: "./assets/<skill-name>.png"
```

## Troubleshooting

- Gray box for the large icon: ensure `icon_large` points to the PNG, not the SVG.
- Inset or white border: ensure the SVG background is full-bleed with no margins.
