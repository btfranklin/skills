# Concept Prompt Patterns

Use this reference during concept generation. Produce three concepts that solve the same problem. Make the composition, density, typography, interaction model, and visual style different in each concept.

## Intake

Capture or safely infer:

- Product type, domain, audience, and usage context
- Primary screen, workflow, decision, or conversion goal
- Requested area: one screen, a page section, or a full page
- Device priority. Use desktop as the default only when mobile use is not important.
- Required navigation, content, states, media, labels, and exact copy
- Existing brand assets, visual limits, implementation limits, and prohibited designs

Do not let image generation replace supplied information architecture or invent unrelated sections, claims, metrics, or product behavior.

## Shared Prompt Requirements

Include in every prompt:

- `Use case: ui-mockup`
- `Asset type: simulated application UI screenshot`
- The intended viewport and requested area
- Product purpose, audience, primary workflow, and required content
- The category name and its one-sentence visual definition
- Composition, navigation model, information density, typography style, surface treatment, imagery, component geometry, and interaction indicators
- A consistent palette, spacing system, surface system, icon treatment, and container model
- Practical constraints: readable hierarchy, code-native UI text and controls, separable imagery, accessible interaction structure, and implementable HTML/CSS
- Negative constraints from the brief and [visual-quality-and-ai-tells.md](visual-quality-and-ai-tells.md)

Ask for the complete requested area at a useful scale. For a full-page request, include enough page sections to evaluate the system. For an application or dashboard, include the primary work area and visible state. Do not accept a header-only crop for a larger request. Do not accept an image in which important text and components are unreadable.

Keep in-image copy minimal unless exact text matters. Quote required text and request verbatim rendering.

## Categories

### 1. Traditional

Create a familiar concept that is suitable for production:

- Use recognizable navigation, layout, and control conventions.
- Prioritize clear hierarchy and legible forms, tables, lists, media, or cards as the domain requires.
- Create a complete product design with a distinct brand style. Do not use a standard template without adaptation.
- Make the component system practical to reproduce.

The Traditional concept must be easy to trust and use. It must also have a distinct visual style.

### 2. Futuristic/Advanced

Create an advanced expert tool or experience that is possible in the near future:

- Use layered work areas, adaptive panels, depth, instruments, timelines, maps, graphs, or augmented previews only when they help the task.
- Use precise typography and high-contrast information architecture.
- Make advanced controls plausible and understandable.
- Create a strong visual effect without making the workflow difficult to use.

The Futuristic/Advanced concept must show capability and control. Do not add neon decoration or interface elements without a function.

### 3. High-concept/Strange

Create an unusual but implementable organizing idea:

- Connect an unusual organizing idea, geometry, surface treatment, editorial composition, or background state system to the domain.
- Give the concept consistent interaction conventions and a strong identity.
- Keep enough familiar controls and indicators to support accessible HTML and CSS.
- Use one clear organizing idea. Do not combine many novelty effects.

The High-concept/Strange concept can be unfamiliar, but it must remain usable. Do not create abstract art without a usable interface.

## Concept Review

Before presenting the batch, verify that:

- All three concepts solve the same brief and preserve required content.
- The concepts have different structures, not only different colors or decoration.
- Each concept has one clear visual idea and a coherent system.
- The requested surface is complete enough to evaluate.
- Important text, controls, component anatomy, and spacing are readable.
- Imagery and decorative assets have a practical production method.
- No concept relies on generic interface filler or several undesired patterns.
- Mobile or narrow-screen behavior can be inferred or is explicitly identified as a later detail need.

Regenerate a concept that fails this review. Do not present it with an apology.

## Presentation and Iteration

For each concept, provide the category name, image, exact prompt, and one short reason. Describe the intended appearance and operation of the product.

Then stop. Ask the user to choose one concept, request another set of three concepts, or give specific feedback. Preserve the three categories for a new set. For a requested variant or combination, identify each change.
