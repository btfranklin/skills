# Style Guide Contract

Use this reference only after concept approval. Treat the approved image, user-supplied content, brand assets, and repository constraints as the source of truth. Produce maintainable HTML/CSS rather than a screenshot recreation.

Read [visual-quality-and-ai-tells.md](visual-quality-and-ai-tells.md) again during extraction and final review.

## Output

Create `ui-style-guide/` in the current project or workspace with:

- `style-guide.html`: documented visual system and component examples
- `style-guide.css`: shared tokens, base styles, components, states, and responsive rules
- `demo.html`: one representative screen using the shared CSS
- `assets/selected-concept.*`: the approved image when project-bound

Use plain HTML and CSS by default. Add a small script only when the demo needs an interaction that native HTML cannot express.

## Extraction

Document:

- Visual thesis: composition, material character, typography, and energy
- Color: backgrounds, surfaces, text, borders, accents, semantic colors, and contrast notes
- Typography: families and fallbacks, scale, weights, line heights, tracking, labels, numeric treatment, and control text
- Spacing and layout: page grid, gutters, section rhythm, container widths, panel density, and content-driven breakpoints
- Surfaces and geometry: cards, panels, bands, rails, lists, tables, borders, radii, shadows, texture, and material effects
- Navigation and controls: global and local navigation, buttons, links, inputs, selects, toggles, disclosure, search, and filters
- Data and feedback: tables, charts, timelines, meters, maps, logs, loading, empty, success, warning, and error states when relevant
- Imagery and icons: source, framing, crop, masks, icon family, stroke/fill treatment, optical size, spacing, and decorative limits
- Motion and interaction: purpose, hover, focus, pressed, selected, expanded, disabled, and reduced-motion behavior
- Accessibility adaptations: contrast, target sizes, focus visibility, semantic elements, keyboard behavior, and readable fallbacks

Resolve ambiguity from the approved concept with the smallest coherent rule. If a critical area is unreadable or cropped, generate a focused detail concept in the same visual system rather than freely inventing it.

## HTML

`style-guide.html` must include:

- A concise title and source-concept reference
- Token samples for color, typography, spacing, and surfaces
- A component gallery covering the approved concept's component families
- Interactive and feedback state examples
- Responsive and accessibility guidance
- A link to `demo.html`

`demo.html` must include:

- One realistic representative screen for the product idea
- Semantic elements such as `header`, `nav`, `main`, `section`, `form`, `table`, `dialog`, or `aside` where appropriate
- Shared components and tokens, not one-off page-specific styling
- Purposeful labels and clearly identified sample data instead of filler text or unsupported claims

Keep real UI text, controls, and state in HTML. Do not place a generated screenshot behind the page or crop the concept into production UI.

## CSS

`style-guide.css` must include:

- `:root` custom properties for color, typography, spacing, radii, borders, shadows, transitions, and layout widths
- Base document styles and accessible defaults
- Reusable component classes with explicit variants
- Native pseudo-class or state-class styling for focus, hover, active, selected, disabled, loading, empty, success, warning, and error states as relevant
- Responsive rules based on content and interaction needs
- `prefers-reduced-motion` handling when motion is used

Keep the CSS readable and cohesive. Use inline styles only for genuine one-off data values such as a progress percentage.

## Fidelity

- Preserve the approved concept's hierarchy, density, palette, typography character, spacing, geometry, imagery, and interaction grammar.
- Preserve the container model. Do not replace open layouts, lists, tables, rails, bands, canvases, or full-bleed regions with generic cards.
- Keep repeated elements consistent through shared tokens and classes; express legitimate differences as variants.
- Do not add decorative labels, badges, pills, glows, overlays, or explanatory copy absent from the concept or brief.
- Replace impossible, fragile, inaccessible, or raster-only effects with implementable equivalents and report material changes.
- Do not shift color temperature, surface tone, media treatment, or icon style merely because another default feels familiar.

## Verification

Before handoff:

1. Parse or otherwise validate the HTML and CSS with available project tooling.
2. Confirm that both HTML files load `style-guide.css` and share tokens and components.
3. Open the guide and demo in a browser or the project's normal development environment.
4. Check the representative screen at desktop and narrow/mobile widths for fit, overflow, hierarchy, and interaction clarity.
5. Verify keyboard navigation, visible focus, accessible names, contrast, control states, and reduced-motion behavior where applicable.
6. Compare the rendered demo directly with the approved concept. Inspect at least composition, typography, palette, spacing, component geometry, and imagery/icon treatment.
7. Run the anti-tell and copy audit. Remove ungrounded filler, repeated layout formulas, decorative metadata, and unnecessary UI chrome.
8. Record intentional deviations and why they improve feasibility or accessibility.

Do not claim fidelity from code inspection or build success alone. Visual comparison is required when the environment supports screenshots or rendered inspection.
