# Concept Prompt Patterns

Use this reference during concept generation. Produce three directions that solve the same problem while differing materially in composition, density, typography, interaction model, and visual character.

## Intake

Capture or safely infer:

- Product type, domain, audience, and usage context
- Primary screen, workflow, decision, or conversion goal
- Requested surface scope: one screen, a page section, or a full-page rhythm
- Device priority; default to desktop only when mobile is not central
- Required navigation, content, states, media, labels, and exact copy
- Existing brand assets, visual constraints, implementation constraints, and forbidden directions

Do not let image generation replace supplied information architecture or invent unrelated sections, claims, metrics, or product behavior.

## Shared Prompt Requirements

Include in every prompt:

- `Use case: ui-mockup`
- `Asset type: simulated application UI screenshot`
- The intended viewport and requested surface scope
- Product purpose, audience, primary workflow, and required content
- The lane name and its one-sentence visual thesis
- Composition, navigation model, information density, typography character, material language, imagery, component geometry, and interaction cues
- A coherent palette, spacing rhythm, surface system, icon treatment, and container model
- Practical constraints: readable hierarchy, code-native UI text and controls, separable imagery, accessible interaction structure, and implementable HTML/CSS
- Negative constraints from the brief and [visual-quality-and-ai-tells.md](visual-quality-and-ai-tells.md)

Ask for the complete requested surface at a useful scale. A full-page request needs enough downstream rhythm to judge the system; an app or dashboard needs the primary working surface and visible state. Do not accept a header-only crop for a broader request or one compressed image whose important text and components are unreadable.

Keep in-image copy minimal unless exact text matters. Quote required text and request verbatim rendering.

## Fixed Lanes

### 1. Traditional

Create the familiar, production-ready answer for the category:

- Use recognizable navigation, layout, and control conventions.
- Prioritize clear hierarchy and legible forms, tables, lists, media, or cards as the domain requires.
- Aim for mature product quality and a distinctive brand expression, not a stock template.
- Make the component system practical to reproduce.

Traditional means trustworthy and immediately usable, not bland.

### 2. Futuristic/Advanced

Create a high-capability, near-future expert tool or experience:

- Use layered operational surfaces, adaptive panels, spatial depth, instrumentation, timelines, maps, graphs, or augmented previews only when relevant.
- Use precise typography and high-contrast information architecture.
- Make advanced controls plausible and understandable.
- Create cinematic presence without sacrificing the workflow.

Advanced means capability and control, not neon decoration or meaningless dashboard chrome.

### 3. High-concept/Strange

Create an unusual but implementable organizing idea:

- Tie a surprising metaphor, geometry, material, editorial composition, or ambient state system to the domain.
- Give the direction a coherent interaction grammar and strong identity.
- Retain enough recognizable affordance to become accessible HTML/CSS.
- Prefer one clear conceptual move over a pile of novelty effects.

Strange means productively unfamiliar, not abstract art without a usable interface.

## Concept Audit

Before presenting the batch, verify that:

- All three concepts solve the same brief and preserve required content.
- The lanes differ structurally, not just by palette or decoration.
- Each concept has one clear visual idea and a coherent system.
- The requested surface is complete enough to evaluate.
- Important text, controls, component anatomy, and spacing are readable.
- Imagery and decorative assets have a plausible production path.
- No direction relies on generic UI filler or clustered anti-tells.
- Mobile or narrow-screen behavior can be inferred or is explicitly identified as a later detail need.

Regenerate a failing direction rather than apologizing for it in the presentation.

## Presentation and Iteration

For each option, provide the lane name, image, exact prompt, and one short rationale describing how the direction would make the product feel and operate.

Then stop. Ask the user to choose one, request another three-lane batch, or give targeted feedback. Preserve the three lanes for a new batch; for a requested variant or blend, label exactly what changed.
