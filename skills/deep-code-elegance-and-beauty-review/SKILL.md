---
name: deep-code-elegance-and-beauty-review
description: >-
  Use only when the user explicitly invokes deep-code-elegance-and-beauty-review or asks for a broad elegance, beauty, aesthetic, joy, or contemplative review of one code project. Focus on cognitive clarity, simplicity, design elegance, idiomatic language fit, developer experience, naming, locality, repetition, shared concepts, and whether the code feels peaceful or joyful to work in. Do not use for ordinary bug hunting, security review, small-diff review, frontend visual QA, or evidence-first deep-codebase-review unless the user explicitly asks to combine them. Output a grounded aesthetic report: first impression, what is beautiful, what disturbs the peace, council observations, guidance, and what to protect.
---

# Deep Code Elegance and Beauty Review

Review a single code project as an artifact of thought, craft, and maintenance experience. Seek the places where the code feels clear, direct, humane, and beautiful, and the places where it creates confusion, friction, noise, or ugliness.

This is not a bug hunt. Use evidence to stay grounded in the actual project, but do not flatten every observation into a defect. Let aesthetic, experiential, and maintainability judgments survive as themselves.

## Operating Stance

- Establish the intended shape first: read repo-local instructions, important docs, architecture notes, roadmap docs, and package manifests before judging whether the project feels coherent.
- Wander before judging: inspect the top-level structure, then sample the important docs, modules, tests, and workflows.
- Treat the codebase as a designed space. Notice shape, rhythm, locality, names, seams, ceremony, repetition, and the path a future maintainer must walk.
- Prefer concrete observations over generic taste. Refer to files, modules, names, or patterns when making a judgment.
- Explain the human mechanism: how the code shape changes comprehension, confidence, anxiety, or ease of future change.
- Keep subjective language honest. It is acceptable to say "this feels..." when the feeling is grounded in a specific code shape.
- Do not prioritize correctness, security, or exhaustive risk discovery. Mention obvious hazards only when they affect elegance, trust, or developer experience.
- Do not edit files unless the user explicitly asks for changes.
- Review one project at a time. If the user points at multiple projects, choose the active project or ask which one should be entered.

## Aesthetic Council

For a substantial project, use a small internal council of lenses. If sub-agents are available and the review scope is broad, delegate these lenses unless the user asks for a solo pass. If sub-agents are unavailable or the project is small, run the same passes yourself.

Do not present the council as a set of competing reports. Synthesize the voices into one coherent experience.

- For broad or delegated reviews, read [references/aesthetic-council-protocol.md](references/aesthetic-council-protocol.md) before assigning reviewer roles.
- For fuller lens prompts, read [references/aesthetic-review-lenses.md](references/aesthetic-review-lenses.md) and use only the sections that fit the project.

## Review Method

1. Enter the project:
   - Read repo-local instructions such as `AGENTS.md`, `README`, architecture docs, roadmap docs, and package manifests.
   - Scan the tree before diving into details.
   - Identify the project's apparent center: the modules, workflows, or documents that reveal its design.
   - Summarize the intended shape for yourself before deciding what feels elegant or strained.

2. Wander through representative spaces:
   - Sample core source files, boundary modules, command entry points, configuration, tests, and docs.
   - Favor breadth before depth. This review is about the felt shape of the project, not total coverage.
   - Follow tension: when a name, wrapper, repeated pattern, or workflow feels awkward, inspect enough nearby code to understand why.

3. Hold the aesthetic council:
   - Run the cognitive clarity, idiom, developer experience, and composition lenses.
   - Preserve observations that are meaningful even when they are not defects.
   - Separate beauty, disturbances, and taste preferences. A disturbance should explain how it creates friction, confusion, distrust, or loss of joy.

4. Offer guidance:
   - Recommend changes that would make the project more beautiful, elegant, humane, and pleasant to maintain.
   - Prefer small, high-leverage refinements over grand rewrites.
   - Name what should be protected, not only what should be changed.

## Output Shape

Use a calm, reflective, concrete report. Prefer this order:

1. First impression: the felt shape of the project after entering it.
2. What is beautiful: patterns, modules, names, flows, or tests that bring clarity or joy.
3. What disturbs the peace: confusing, noisy, repetitive, misplaced, unidiomatic, or emotionally expensive areas.
4. Council observations: a brief synthesis from the main lenses, not raw sub-reports.
5. Guidance: practical ways to make the codebase more elegant, humane, and joy-inducing.
6. What to protect: the existing qualities that future work should preserve.

When useful, include file references. Do not require every aesthetic observation to meet the standard of a formal defect finding.

For a worked report shape, read [examples/elegance-review-output.md](examples/elegance-review-output.md) when producing a full written review.

## Practical Heuristics

- Prefer a few memorable, well-evidenced observations over a catalog of nits.
- Look for the project's center of gravity: the module, vocabulary, workflow, or document that makes the rest understandable.
- Look for elegant reductions: a name, value object, table, helper, folder move, or deletion that would make the idea more direct.
- Notice repeated ceremony, noisy adapter code, similar branches, or setup rituals that make future changes feel heavier than they should.
- Notice tests and docs as part of the aesthetic surface: they can either teach the project calmly or force the maintainer to reverse-engineer it.
- Treat compatibility wrappers, facades, and re-export layers as aesthetic costs unless they serve a concrete current purpose.
- Distinguish "I would write it differently" from "this shape makes the next person work harder."
- Name what should be protected before recommending change.

## Anti-Patterns

- Do not turn the review into a normal bug list.
- Do not rank everything by severity.
- Do not bury aesthetic experience under evidence mechanics.
- Do not praise or criticize style without connecting it to cognition, maintenance, language fit, or developer experience.
- Do not recommend abstraction merely because duplication exists; ask whether the abstraction would make the code more peaceful.
- Do not use mystical language as a substitute for concrete engineering perception.
