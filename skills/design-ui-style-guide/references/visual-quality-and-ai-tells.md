# Visual Quality and Undesired Model Patterns

Use this reference when you write concept prompts. Use it when you review generated concepts, extract the style guide, and check the rendered demo. Its purpose is to identify repetitive model defaults. It does not prohibit valid design patterns.

## Decision Rule

Start with the brief, audience, product type, content, brand, and approved concept. Mark a pattern as undesired when it adds decoration without a clear purpose or repeats filler. Keep the pattern when it communicates meaning, belongs to the brand, or supports a product requirement.

Use one consistent visual definition. Do not combine visual techniques only because they are popular. Establish one palette, shape system, typography system, icon treatment, surface model, and spacing system. Vary these systems only through an explicit rule.

## Common Undesired Patterns

Avoid clustering these patterns by default:

- Purple-blue mesh gradients, neon glows, glassmorphism, or bokeh orbs used as generic atmosphere
- A centered headline on an abstract dark background without a product-specific visual idea
- Three equal feature cards, repeated bento tiles, stacked card mosaics, or a card around every region
- The same split image/text section repeated in a zigzag down the page
- Repeated section headers with a large headline on one side and a small floating explainer on the other
- Small uppercase, monospaced, wide-tracked eyebrow labels above every hero or section heading
- Decorative section numbering such as `01 / Capabilities`, image counters users do not need, or step labels that repeat visible sequence
- Hero badges, version stamps, invitation labels, or status claims that are not real product information
- Pills, tags, or pseudo-editorial labels over images; fake archive captions or photo credits for generated or stock imagery
- Decorative status dots, build/version footers, locale/time/weather strips, or scroll instructions without functional value
- Decorative word strips such as `DESIGN / BUILD / SHIP` added only to fill space
- Fake product screenshots assembled from meaningless rectangles, task rows, terminal frames, or dashboard fragments
- Fake metrics, implausibly round numbers, unsupported precise values, generic testimonials, invented social proof, or placeholder brands presented as fact
- Generic marketing language such as “elevate,” “unleash,” “seamless,” “next-generation,” or “revolutionize” where a concrete action or benefit is available

Do not use this list to create a different standard template. Asymmetric layouts, serif type, off-black backgrounds, and photography are options. They are not required replacements.

## Eyebrows and Micro-Labels

An eyebrow is a small label above a heading. It often uses uppercase, monospaced, or widely spaced text. Use it only when it supplies information that the heading cannot supply. This information can be a real category, state, or navigation indicator. It is an undesired pattern when it is only decoration.

- Omit the eyebrow by default. Let the heading identify the section.
- Never add section numbers merely to make the page look art-directed.
- Do not use an eyebrow on adjacent sections. On a long page, use no more than one eyebrow in approximately three sections. This limit is not a target.
- Do not combine an eyebrow, badge, status strip, micro-tagline, and supporting paragraph in the same hero.
- Prefer a plain-language label over cryptic metadata when categorization is genuinely needed.

## Composition and Containers

- Start with composition and information hierarchy. Do not start with a list of components.
- Give each section one primary job and one dominant visual idea.
- Use cards only when containment, comparison, selection, or elevation communicates structure. Otherwise, use an open layout, bands, lists, tables, rails, dividers, or white space.
- Vary the structure of sections on a long page. Do not repeat one section formula more than twice in sequence.
- Avoid equal three-card feature rows unless exactly three peer items must be compared and equal weight is meaningful.
- Keep one consistent container and geometry system. Use mixed radii, border weights, shadows, or pill treatments only when an explicit semantic rule requires them.
- Make the first viewport fit the available screen. Keep the primary action or task visible. Include persistent navigation in the available height.
- Keep navigation quiet enough to preserve the primary task. Do not fill headers with ornamental controls or pseudo-status widgets.

## Imagery and Product Representation

- Use imagery when it communicates product, brand, place, or narrative meaning. Do not require imagery for a tool whose work area is the main subject.
- Keep interactive UI text and controls in code. Generated images may supply photography, illustration, texture, products, environments, or other visual assets.
- Do not use a generated concept screenshot as the shipped interface.
- Do not simulate product proof with decorative rectangles. Use a real screenshot, a genuine interactive preview, a generated product image, or no preview.
- Keep image captions functional. Credit a real creator when applicable. Do not use invented archival language to give stock or generated media false importance.
- Match media crop, lighting, edge treatment, background, and shadow to the surrounding system. Avoid pasted-on imagery and automatic color washes.

## Copy and Data

- Use product language, not design commentary or prompt language.
- Make headings, labels, and button text concrete enough to understand by scanning.
- Use consistent language and the same language level across the interface.
- Preserve user-supplied wording. If examples are necessary, label them as sample or mock data.
- Never fabricate claims, testimonials, customer logos, usage statistics, availability, stock counts, version status, or engineering precision.
- Read every visible string again. Replace unclear references, forced comparisons, decorative poetic text, false modesty, and generic startup language with direct wording.

## Color, Type, and Surfaces

- Choose color from the brief and content. Purple, gradients, glass, cream, pure black, serif, sans serif, and monospace are all valid when intentional.
- Avoid automatic color and type combinations that recur across unrelated briefs. Examples include a purple-blue glow on dark navy and warm beige with brass. Another example is neutral sans-serif type with slate surfaces for every software product.
- Keep the palette and color temperature consistent. Do not add unrelated accent colors. Do not switch between warm and cool neutral colors without a composition requirement.
- Choose typography for the audience and content rather than defaulting to one fashionable family. Define control and data typography as deliberately as display text.
- Use emphasis within a consistent type system. Do not use a contrasting type family for one word only to create visual distinction.
- Use shadows, blur, transparency, gradient text, and texture only when necessary. Use them consistently. They must clarify hierarchy or surface treatment.

## Motion and State

- Add motion only when it communicates hierarchy, feedback, continuity, a state change, or a narrative sequence.
- Do not add perpetual animation, marquees, parallax, magnetic controls, or scroll hijacking merely to prove the page is interactive.
- Keep task completion independent of animation. Respect reduced-motion preferences.
- Design real hover, focus, pressed, selected, disabled, loading, empty, success, warning, and error states as the product requires.
- Do not use decorative dots or pulses as fake evidence of live state.

## Final Audit

Before approving a concept or delivering the demo, ask:

- Does the interface represent this product, audience, and content? Could the same design fit any startup?
- Does the interface have one clear visual definition and a consistent system?
- Does every label, card, badge, dot, image, effect, and animation communicate something?
- Are section structures varied without becoming chaotic?
- Are claims and sample data grounded or clearly identified?
- Is the primary task obvious by scanning headings, controls, and state?
- Did the implementation preserve the approved concept? Did it introduce familiar defaults that the approved concept does not contain?

If the design contains several undesired patterns, simplify the composition. Do not add more decoration to correct a generic design.
