---
name: deep-code-elegance-and-beauty-review
description: >-
  Use when the user asks for a broad review of code elegance, beauty, developer joy, cognitive clarity, idiomatic language fit, naming, locality, or contemplative craft in one project. Evaluate code as a humane maintenance experience rather than a defect inventory. Do not use for ordinary bug, security, small-diff, or frontend visual reviews, or for deep-codebase-review unless the user explicitly combines them.
---

# Deep Code Elegance and Beauty Review

Review one project as an artifact of thought, craft, and maintenance experience. Ground subjective judgment in concrete code while preserving observations that matter even when they are not defects.

## Workflow

### 1. Enter the project

- Use the active project when it is unambiguous; otherwise ask which single project to enter.
- Read repo-local instructions and the relevant README, architecture, roadmap, and package documents.
- Scan the tree, identify the apparent center of gravity, and infer the intended shape before judging it.
- Record a provisional first impression after this initial orientation and before detailed verification. Preserve it as the project's immediate felt shape; later evidence can qualify it but must not silently replace it.

### 2. Wander with purpose

- Sample core modules, boundaries, commands, configuration, tests, and documentation.
- Follow tension in names, wrappers, repetition, ceremony, or workflows far enough to understand its cause.
- Load [references/aesthetic-review-lenses.md](references/aesthetic-review-lenses.md) and select the lenses that fit the project.

### 3. Ground the experience

- Connect praise and criticism to comprehension, confidence, maintenance effort, language fit, or developer joy.
- Separate beauty, genuine disturbance, and personal taste. Do not turn preferences into defects.
- Prefer small reductions, clearer names, better locality, or deletion over grand rewrites.
- Briefly surface any obvious critical correctness, security, privacy, or data-loss hazard, then recommend a dedicated review without turning this report into a bug audit.

## Model Guidance

When the harness lets you choose a model, use a capable model that has good code understanding. Use low or medium reasoning effort. Do not use a low-capability model only because it is fast or inexpensive. The model must record its first impression before it does detailed checks. Later evidence can change or limit that impression, but the impression must remain visible. The model must not change the review into a correctness audit. If the harness does not have a reasoning setting, put these behavior rules in each reviewer's instructions.

## Aesthetic Council

For a substantial project, use a small council when sub-agents are available and the user did not request a solo pass. Load [references/aesthetic-council-protocol.md](references/aesthetic-council-protocol.md) before delegating.

If sub-agents are unavailable or the project is small, continue with the same lenses solo. Synthesize all observations into one voice.

## Output

Present:

1. First impression.
2. What is beautiful.
3. What disturbs the peace.
4. Lens synthesis.
5. What to protect.
6. Guidance.

Use file references where they clarify the judgment, but do not force every aesthetic observation into formal defect evidence. For a concrete report model, read [examples/elegance-review-output.md](examples/elegance-review-output.md).

## Discipline

- Prefer a few memorable, grounded observations over a catalog of nits.
- Distinguish "I would write it differently" from "this shape makes the next person work harder."
- Do not recommend an abstraction merely because duplication exists; ask whether it reduces thought.
- Do not use mystical language as a substitute for engineering perception.
- Do not edit files unless the user asks for changes.
