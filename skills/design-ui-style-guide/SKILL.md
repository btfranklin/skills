---
name: design-ui-style-guide
description: >-
  Preferred first-step workflow for creating a UI from whole cloth. Use when asked to create, design, build, prototype, mock up, or redesign a website, web app, dashboard, landing page, product screen, internal tool, or application UI without an approved visual direction. Generates exactly three image concepts, stops for selection or iteration, then converts the approved direction into a reusable HTML/CSS style guide and representative demo. Use before frontend implementation unless the user supplies an existing design, requests a narrow edit, or explicitly skips visual exploration.
---

# Design UI Style Guide

Turn a UI idea into an approved visual direction and a reusable HTML-centric source of truth. Keep two explicit checkpoints: concept selection, then style-guide delivery.

Own the concept and style-guide artifact contract. Do not expand into full product implementation unless the user separately asks for it after the guide exists.

## Required Capabilities

- Resolve image generation in this order:
  1. In Codex, use `$imagegen` when it is available and follow that skill's generation and image-editing workflow.
  2. In another agent or harness, use its native image-generation skill or tool when one is available.
  3. If no image-generation capability exists, use the text-only fallback below.
- Do not replace available image generation with prose, SVG mockups, or CSS sketches.
- During the artifact phase, use the companion skill `design-html-first-web-uis` when it is installed. It supplies semantic HTML, native browser behavior, progressive enhancement, accessibility, and minimal-JavaScript guidance.

If `design-html-first-web-uis` is missing, offer to install it from the same public package and match the current skill's project or global scope. After the user authorizes a global installation, run:

```bash
npx skills add btfranklin/skills --skill design-html-first-web-uis -g
```

For a project-scoped installation, omit `-g`.

Do not block the workflow if installing it is unsupported or declined; apply the semantic and accessibility requirements in this skill directly.

If image generation is unavailable, state that limitation, provide prompt-ready concept briefs, and ask whether to continue with text-only planning; do not imply that images were generated. Outside Codex, do not require a particular image skill, plugin, model, or vendor.

## Workflow

1. Inspect the brief and any existing repository guidance, content, brand assets, screenshots, and technical constraints.
2. Establish the audience, product purpose, primary screen or workflow, required content, device priority, brand constraints, and forbidden directions. Infer low-risk defaults; ask only when an unresolved choice would materially change the concepts.
3. Write a one-sentence visual thesis for each direction, describing its composition, material character, typography, and energy.
4. Read [references/concept-prompt-patterns.md](references/concept-prompt-patterns.md) and [references/visual-quality-and-ai-tells.md](references/visual-quality-and-ai-tells.md).
5. Generate exactly three concept images using the fixed lanes: Traditional, Futuristic/Advanced, and High-concept/Strange. Give each lane its own prompt and image.
6. Audit the concepts against the visual-quality reference. Regenerate any direction that is generic, repetitive, unreadable, off-brief, incomplete for the requested surface, or impractical to translate into HTML/CSS.
7. Present all three images with the exact prompt and a short rationale for each.
8. Stop at the selection checkpoint. Ask the user to choose one, request another batch, or give targeted iteration guidance.
9. If iterating, preserve the three-lane structure unless the user explicitly requests variants of one direction or a blend.
10. After approval, read [references/style-guide-contract.md](references/style-guide-contract.md). Treat the selected image and user-supplied content as the visual and editorial source of truth.
11. If a critical region is too small, ambiguous, or cropped to extract reliably, generate a focused detail concept in the approved visual system before inventing the missing design.
12. Create the output under `ui-style-guide/` in the current project or workspace:
    - `style-guide.html`
    - `style-guide.css`
    - `demo.html`
    - `assets/selected-concept.*` when the image is project-bound
13. Match the approved direction closely. Replace impossible, brittle, or inaccessible details with maintainable HTML/CSS equivalents and record material compromises.
14. Verify the guide and demo structurally and visually, then report the selected direction, artifact paths, checks performed, and intentional deviations.

## Guardrails

- Do not generate the style guide before the user approves a concept.
- Do not implement the full product in the default workflow. Deliver a style guide plus one representative screen.
- Do not invent product claims, company names, testimonials, metrics, or fake precision. Clearly label sample data when realistic examples are needed.
- Keep visible copy specific, purposeful, and consistent with the product context. Preserve exact supplied copy.
- Keep interactive UI text and controls in HTML. Use generated imagery for visual assets, not as a substitute for working UI.
- Use CSS custom properties for tokens. Make `demo.html` depend on `style-guide.css` so the demo proves the guide is reusable.
- Prefer native HTML controls and accessible state styling. Add JavaScript only for small interactions that cannot be represented declaratively.
- Treat the anti-tell reference as a bias correction, not a substitute for judgment. A discouraged pattern is acceptable when the brief, brand, domain, or approved concept gives it a real purpose.

## Handoff

After concept generation, provide:

- The three images labeled `1. Traditional`, `2. Futuristic/Advanced`, and `3. High-concept/Strange`
- The exact prompt and one-sentence rationale for each
- A direct selection checkpoint

After style-guide delivery, provide:

- The selected concept lane and saved image path when applicable
- Paths for `style-guide.html`, `style-guide.css`, and `demo.html`
- A concise description of the extracted visual system
- Structural and visual verification performed
- Any fidelity compromises or intentionally retained discouraged patterns
