# Visual Quality and AI-Tell Guardrails

Use this reference when writing concept prompts, reviewing generated concepts, extracting the style guide, and checking the rendered demo. Its purpose is to counter repetitive model defaults, not to outlaw legitimate design patterns.

## Decision Rule

Start with the brief, audience, product type, content, brand, and approved concept. Discourage a pattern when it appears as unexplained decoration or repeated filler. Keep it when it communicates real meaning, belongs to the brand, or is required by the product.

Prefer one coherent visual thesis over a collection of fashionable devices. Establish one palette, shape language, typography system, icon treatment, surface model, and spacing rhythm; vary them only through an explicit rule.

## Common Default Signatures

Avoid clustering these patterns by default:

- Purple-blue mesh gradients, neon glows, glassmorphism, or bokeh orbs used as generic atmosphere
- A centered headline over an abstract dark background with no product-specific visual idea
- Three equal feature cards, repeated bento tiles, stacked card mosaics, or a card around every region
- The same split image/text section repeated in a zigzag down the page
- Repeated section headers with a large headline on one side and a small floating explainer on the other
- Small uppercase, monospaced, wide-tracked eyebrow labels above every hero or section heading
- Decorative section numbering such as `01 / Capabilities`, image counters users do not need, or step labels that repeat visible sequence
- Hero badges, version stamps, invitation labels, or status claims that are not real product information
- Pills, tags, or pseudo-editorial labels over images; fake archive captions or photo credits for generated or stock imagery
- Decorative status dots, build/version footers, locale/time/weather strips, or scroll instructions without functional value
- Decorative word strips such as `DESIGN / BUILD / SHIP` added only to fill space
- Fake product screenshots assembled from meaningless rectangles, task rows, terminal chrome, or dashboard fragments
- Fake metrics, implausibly round numbers, fabricated precision, generic testimonials, invented social proof, or placeholder brands presented as fact
- Generic marketing language such as “elevate,” “unleash,” “seamless,” “next-generation,” or “revolutionize” where a concrete action or benefit is available

Do not turn this list into a different template. For example, asymmetric layouts, serif type, off-black backgrounds, and photography are options, not mandatory replacements.

## Eyebrows and Micro-Labels

An eyebrow is a small label above a heading, often uppercase, monospaced, or widely tracked. It is useful when it supplies information the heading cannot, such as a real category, state, or navigation cue. It becomes a tell when used as automatic decoration.

- Omit the eyebrow by default; let the heading establish the section.
- Never add section numbers merely to make the page look art-directed.
- Avoid using an eyebrow on adjacent sections. On a long page, treat one per roughly three sections as a ceiling, not a quota.
- Do not combine an eyebrow, badge, status strip, micro-tagline, and supporting paragraph in the same hero.
- Prefer a plain-language label over cryptic metadata when categorization is genuinely needed.

## Composition and Containers

- Start with composition and information hierarchy, not component inventory.
- Give each section one primary job and one dominant visual idea.
- Use cards only when containment, comparison, selection, or elevation communicates structure. Otherwise prefer open layout, bands, lists, tables, rails, dividers, and whitespace.
- Vary long-page rhythm deliberately. Do not repeat one section formula more than twice in succession.
- Avoid equal three-card feature rows unless exactly three peer items must be compared and equal weight is meaningful.
- Keep one coherent container and geometry system. Mixed radii, border weights, shadows, and pill treatments need an explicit semantic rule.
- Make the first viewport fit the available screen with the primary action or task visible. Treat persistent navigation as part of that height budget.
- Keep navigation quiet enough to preserve the primary task. Do not fill headers with ornamental controls or pseudo-status widgets.

## Imagery and Product Representation

- Use imagery when it carries product, brand, place, or narrative meaning. Do not require it for tools where the working surface itself is the subject.
- Keep interactive UI text and controls in code. Generated images may supply photography, illustration, texture, products, environments, or other visual assets.
- Do not use a generated concept screenshot as the shipped interface.
- Do not simulate product proof with decorative rectangles. Use a real screenshot, a genuine interactive preview, a generated product image, or no preview.
- Keep image captions functional. Credit a real creator when appropriate; do not fabricate archival language to make stock or generated media seem important.
- Match media crop, lighting, edge treatment, background, and shadow to the surrounding system. Avoid pasted-on imagery and automatic color washes.

## Copy and Data

- Use product language, not design commentary or prompt language.
- Make headings, labels, and button text concrete enough to understand by scanning.
- Use one voice and register across the surface.
- Preserve user-supplied wording. If examples are necessary, label them as sample or mock data.
- Never fabricate claims, testimonials, customer logos, usage statistics, availability, stock counts, version status, or engineering precision.
- Re-read every visible string. Replace unclear referents, forced metaphors, mock-poetic filler, fake humility, and generic startup language with direct wording.

## Color, Type, and Material

- Choose color from the brief and content. Purple, gradients, glass, cream, pure black, serif, sans serif, and monospace are all valid when intentional.
- Avoid the automatic combinations that recur across unrelated briefs: purple-blue glow on dark navy, warm beige plus brass for every premium consumer product, or neutral sans plus slate surfaces for every software product.
- Lock the palette and color temperature. Do not introduce unrelated accent colors or switch between warm and cool neutrals without a compositional reason.
- Choose typography for the audience and content rather than defaulting to one fashionable family. Define control and data typography as deliberately as display text.
- Use emphasis within a coherent type system. Do not inject a contrasting type family into a single word merely to manufacture personality.
- Use shadows, blur, transparency, gradient text, and texture sparingly and consistently. They should clarify hierarchy or material, not stand in for it.

## Motion and State

- Add motion only when it communicates hierarchy, feedback, continuity, state change, or narrative sequence.
- Do not add perpetual animation, marquees, parallax, magnetic controls, or scroll hijacking merely to prove the page is interactive.
- Keep task completion independent of animation and respect reduced-motion preferences.
- Design real hover, focus, pressed, selected, disabled, loading, empty, success, warning, and error states as the product requires.
- Do not use decorative dots or pulses as fake evidence of live state.

## Final Audit

Before approving a concept or delivering the demo, ask:

- Does the surface express this product, audience, and content, or could the same design fit any startup?
- Is there one clear visual thesis and a coherent system?
- Does every label, card, badge, dot, image, effect, and animation communicate something?
- Are section structures varied without becoming chaotic?
- Are claims and sample data grounded or clearly identified?
- Is the primary task obvious by scanning headings, controls, and state?
- Did implementation preserve the approved concept instead of drifting toward familiar defaults?

If several tells cluster together, simplify and recompose. Do not fix generic design by adding more decoration.
