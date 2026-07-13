# Aesthetic Council Protocol

Use this protocol when an elegance review should be split across specialist reviewers. The coordinator owns the final judgment and must produce one coherent report.

## Activation Rules

- Use a small council for broad reviews of substantial projects when sub-agents are available, unless the user asks for a solo pass.
- Do not use a council for small-diff reviews or when the user only wants a quick impression.
- Before delegating, state that an aesthetic council is being used and name the roles being assigned.
- Give each reviewer a distinct lens. Do not ask several agents to perform the same generic review.
- Keep the council small: three to four reviewers is usually enough.
- If sub-agents are unavailable, disclose the limitation and continue with the same lenses solo unless the user explicitly required a council.

## Core Roster

- `Coordinator / Lead Reviewer`: Establish the intended shape, choose lenses, keep scope bounded, verify important claims, reconcile tensions, and write the final report.
- `Cognitive Clarity Reviewer`: Review whether the project expresses its ideas directly, whether abstractions reduce thought, and whether the next change has an obvious home.
- `Language and Idiom Reviewer`: Review whether each language and framework is used with its grain, without performative cleverness or needless ceremony.
- `Developer Experience Reviewer`: Review setup, commands, tests, docs, logs, errors, and workflows as surfaces that create confidence or dread.
- `Composition and Naming Reviewer`: Review vocabulary, folder layout, locality, repeated concepts, module rhythm, and whether names orient the maintainer.

## Optional Reviewers

Add only when the project strongly calls for the lens:

- `Tests as Teaching Reviewer`: Review whether tests explain the system, reveal meaningful scenarios, and support humane future change.
- `Documentation and Narrative Reviewer`: Review whether docs, comments, and planning artifacts make the project easier to enter.
- `Boundary and Locality Reviewer`: Review whether related concepts live near each other and whether adapters, domain logic, and workflows are placed naturally.

## Specialist Task Template

Use this shape when delegating. Fill in the repo and scope before sending.

```text
You are the [ROLE] for a deep code elegance and beauty review.

Scope:
- Review only [PROJECT / FILES / MODULES].
- Focus on [ROLE-SPECIFIC AESTHETIC CONCERNS].
- Do not turn this into a normal bug hunt.
- Do not edit files.

Output:
- Concrete observations with file, module, command, or doc evidence where useful.
- Explain how each observation affects comprehension, confidence, maintenance effort, or developer joy.
- Separate beauty, disturbances, and taste preferences.
- Mark uncertainty explicitly when a judgment depends on an assumption.
- Keep the report concise and grounded.
```

## Observation Ledger

Before writing the final report, normalize reviewer output into a private ledger:

- `observation`: the beauty, disturbance, or preference.
- `evidence`: exact file references, commands, module names, or repo artifacts.
- `human effect`: how the shape affects comprehension, confidence, anxiety, or future change.
- `classification`: beauty, disturbance, taste preference, guidance, or protect.
- `corroboration`: which reviewers agree, conflict, or provide related evidence.
- `verification`: whether the coordinator checked the claim directly.
- `disposition`: final report item, merged item, open question, or discarded.

## Consolidation Rules

- Do not paste raw specialist reports into the final answer.
- Deduplicate observations that describe the same experience, even if reviewers found them in different places.
- Resolve contradictions by checking source files yourself.
- Discard unsupported claims, generic compliments, and style preferences without a clear maintenance or cognition effect.
- Keep the final report in one voice: first impression, what is beautiful, what disturbs the peace, lens synthesis, what to protect, and guidance.
- Preserve the skill's purpose. Aesthetic review may mention correctness only when it affects trust, elegance, or developer experience.
