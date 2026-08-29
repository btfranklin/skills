---
name: deep-code-elegance-and-beauty-review
description: >-
  Review one project for code elegance, beauty, developer joy, clarity, language conventions, naming, and locality. Evaluate the maintenance experience. Do not use this skill for defect, security, small-change, or visual UI reviews. Do not combine it with deep-codebase-review unless the user requests both skills.
---

# Deep Code Elegance and Beauty Review

Review the design and maintenance experience of one project. Support subjective assessments with specific code. Preserve useful observations that are not defects.

## Workflow

### 1. Enter the project

- Use the active project when its identity is clear. Otherwise, ask the user to select one project.
- Read repository instructions and relevant project documents. These can include the README, architecture, roadmap, and package documents.
- Scan the tree. Identify the primary modules and boundaries. Infer the intended structure before you assess it.
- Record a provisional first impression after this initial review and before detailed verification.
- Preserve this first impression in the report. Later evidence can change or limit it, but it must not replace it without explanation.

### 2. Inspect representative areas

- Sample core modules, boundaries, commands, configuration, tests, and documentation.
- Inspect unclear names, wrappers, repetition, extra process, or workflows until you understand the cause.
- Load [references/aesthetic-review-lenses.md](references/aesthetic-review-lenses.md) and select the review areas that apply to the project.

### 3. Ground the experience

- Connect positive and negative assessments to comprehension, confidence, maintenance effort, language suitability, or developer joy.
- Separate beauty, maintenance difficulty, and personal preference. Do not classify preferences as defects.
- Prefer small simplifications, clear names, good locality, or deletion. Avoid large rewrites without evidence.
- Briefly report an obvious critical correctness, security, privacy, or data-loss risk.
- Recommend a dedicated review for that risk. Do not change this report into a defect audit.

## Model Guidance

When the harness lets you choose a model, use a capable model that has good code understanding. Use low or medium reasoning effort. Do not use a low-capability model only because it is fast or inexpensive. The model must record its first impression before detailed checks. Later evidence can change or limit that impression. The first impression must remain visible. The model must not change the review into a correctness audit. If the harness does not have a reasoning setting, put these behavior rules in each reviewer's instructions.

## Aesthetic Council

For a substantial project, use a small council when sub-agents are available. Do not use a council when the user requests a solo review. Load [references/aesthetic-council-protocol.md](references/aesthetic-council-protocol.md) before you delegate work.

If sub-agents are not available, use the same review areas in a solo review. Also use a solo review for a small project. Combine all observations into one report.

## Output

Present:

1. First impression.
2. What is beautiful.
3. What causes maintenance difficulty.
4. Review-area summary.
5. What to protect.
6. Guidance.

Use file references when they clarify the assessment. Aesthetic observations do not require formal defect evidence. For a report example, read [examples/elegance-review-output.md](examples/elegance-review-output.md).

## Discipline

- Prefer a small number of specific observations. Do not report minor preferences as a list.
- Separate personal preference from a design that increases maintenance work.
- Do not recommend an abstraction only because repeated code exists. Confirm that the abstraction reduces comprehension or maintenance work.
- Use direct technical language for each observation.
- Do not edit files unless the user asks for changes.
