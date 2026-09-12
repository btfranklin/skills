# Aesthetic Council Protocol

Use this protocol when an elegance review needs specialist reviewers. The coordinator owns the final assessment and must produce one report.

## Activation Rules

- Use a small council for a broad review of a substantial project when sub-agents are available.
- Do not use a council when the user requests a solo review.
- Do not use a council for small-diff reviews or when the user only wants a quick impression.
- Before you delegate work, state that you will use an aesthetic council. Name the assigned roles.
- Give each reviewer a distinct review area. Do not ask several agents to perform the same generic review.
- Use three or four reviewers unless the scope requires another reviewer.
- If sub-agents are not available, state this limit.
- Continue with the same review areas in a solo review unless the user required a council.

## Core Roster

- `Coordinator / Lead Reviewer`: Establish the intended structure. Choose review areas. Limit the scope. Verify important claims. Resolve conflicting assessments. Write the final report.
- `Cognitive Clarity Reviewer`: Assess whether the project expresses its ideas directly. Assess whether abstractions reduce comprehension work. Trace one or two likely changes from project evidence. Compare a small adjustment with retaining the design. Assess whether deletion reduces the concepts a maintainer must understand.
- `Language and Convention Reviewer`: Assess whether the code follows the normal conventions of each language and framework. Read the applicable Python or TypeScript guide. Compare representative calls with language and framework conventions. Identify existing capabilities that can replace custom machinery.
- `Developer Experience Reviewer`: Assess setup, commands, tests, documents, logs, errors, and workflows. Explain how they affect confidence or concern.
- `Composition and Naming Reviewer`: Assess vocabulary, folder layout, locality, repeated concepts, module organization, and names. Read complete calls with their receivers and arguments. Check ownership before recommending method moves. Show conditional before-and-after examples.

## Optional Reviewers

Add an optional reviewer only when the project needs that review area:

- `Tests as Teaching Reviewer`: Review whether tests explain the system, reveal meaningful scenarios, and support humane future change.
- `Documentation and Narrative Reviewer`: Review whether documentation, comments, and planning artifacts make the project easier to understand.
- `Boundary and Locality Reviewer`: Review whether related concepts live near each other. Review whether adapters, domain logic, and workflows have clear locations.

## Specialist Task Template

Use this template when you delegate work. Fill in the repository and scope before you send it.

```text
You are the [ROLE] for a deep code elegance and beauty review.

Scope:
- Review only [PROJECT / FILES / MODULES].
- Focus on [ROLE-SPECIFIC AESTHETIC CONCERNS].
- Use low or medium reasoning effort when the harness exposes that setting.
- Read [ASSIGNED REFERENCE PATHS]. Use design-judgment.md and the applicable language guide for naming, structural, or simplification work.
- Check actual callers and ownership. Support likely changes with project evidence and label assumptions.
- Consider deletion before new machinery. Preserve clear code and useful boundaries.
- Record your provisional first impression after initial orientation and before detailed verification. Keep it distinct when later evidence qualifies it.
- Do not turn this into a general defect review.
- Do not edit files.

Output:
- Concrete observations with file, module, command, or doc evidence where useful.
- Explain how each observation affects comprehension, confidence, maintenance effort, or developer joy.
- Separate beauty, maintenance difficulty, and personal preferences.
- Mark uncertainty explicitly when a judgment depends on an assumption.
- For a naming recommendation, show a small before-and-after call and explain when to retain the current form.
- For a structural recommendation, explain the likely change, its evidence, and the current comprehension cost.
- For subtraction, identify what disappears, what remains, and how required behavior is preserved.
- Keep the report concise and grounded.
```

## Observation Ledger

Before you write the final report, record reviewer output in a private list:

- `observation`: the beauty, maintenance difficulty, or preference.
- `evidence`: exact file references, commands, module names, or repository artifacts.
- `human effect`: how the design affects comprehension, confidence, concern, or future change.
- `classification`: beauty, maintenance difficulty, taste preference, guidance, or protect.
- `corroboration`: which reviewers agree, conflict, or provide related evidence.
- `verification`: whether the coordinator checked the claim directly.
- `disposition`: final report item, merged item, open question, or discarded.

## Consolidation Rules

- Do not paste raw specialist reports into the final answer.
- Merge observations that describe the same experience. Do this when reviewers find them in different places.
- Resolve conflicts by checking the source files and representative callers.
- Verify likely-change evidence and compatibility constraints. Reject unsupported future requirements.
- Check that simplification preserves distinct policies and lifecycles. Fewer lines alone do not establish a benefit.
- Discard unsupported claims, generic compliments, and style preferences without a clear maintenance or cognition effect.
- Use consistent language in the final report. Include the first impression, beauty, maintenance difficulty, review-area summary, items to protect, and guidance.
- Preserve the skill's purpose. An aesthetic review can mention correctness only when it affects trust, elegance, or developer experience.
