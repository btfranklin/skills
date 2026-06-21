# Aesthetic Review Lenses

Use these lenses selectively. Do not force every lens onto every repository. The goal is to understand the project's felt shape, not to produce a complete defect inventory.

## 1. Intended Shape

- What kind of place is this project trying to be?
- Which docs, module boundaries, commands, or naming conventions reveal that intent?
- Does the implementation reinforce the stated direction, or does it quietly pull the project somewhere else?
- If there are no design docs, what intended shape is implied by the current layout and vocabulary?

## 2. Cognitive Clarity and Simplicity

- Does the code express the underlying idea directly?
- Are important concepts split across too many files or hidden behind needless ceremony?
- Do helpers, constants, schemas, prompts, adapters, and test setup live where a maintainer would expect them?
- Does an abstraction reduce thought, or merely move thought elsewhere?
- Is there an obvious home for the next likely change?

## 3. Language and Framework Fit

- Does each language get to be itself, or is the project fighting its tools?
- In Python, notice plain functions, context managers, dataclasses or typed models where useful, simple data shapes, readable tests, and classes only where they clarify ownership.
- In TypeScript or JavaScript, notice meaningful types, clear async flow, framework-shaped boundaries, and object shapes that carry intent.
- In Swift, Rust, Go, Ruby, SQL, shell, or other languages, infer the local idiom from the ecosystem and existing code, then judge whether the code works with that grain.
- Avoid performative idiom. Prefer language features when they make the idea clearer, safer, or more pleasant.

## 4. Developer Experience and Joy

- How easily can a newcomer find the project's center?
- Do setup, commands, logs, errors, tests, fixtures, and docs create confidence or dread?
- Are important workflows visible, memorable, and named in ways that help?
- Do tests teach the system, or do they merely enforce implementation details?
- Where does the project feel generous: orienting names, explainable tools, calm docs, helpful errors, or boundaries that reduce anxiety?

## 5. Composition, Naming, and Vocabulary

- Do names carry the right level of abstraction?
- Does the folder structure form a memorable map?
- Are there competing centers of gravity?
- Is there vocabulary drift: several words for one idea, or one word doing too much work?
- Are repeated concepts represented once, while genuinely different cases remain comfortably separate?

## 6. Locality and Repetition

- Do related ideas live close enough together for the maintainer's mental model to stay intact?
- Is repeated setup or plumbing creating friction that a small helper, table, value object, or clearer boundary would remove?
- Is duplication healthy parallelism, or does it show that a shared concept is unnamed?
- Are wrappers, facades, re-export layers, or adapter glue making ownership less obvious?

## 7. Tests and Docs as Aesthetic Surfaces

- Do tests make important behavior easier to understand?
- Are fixtures and examples shaped like the domain, or like incidental implementation machinery?
- Do docs describe the real project, or a cleaner project that no longer exists?
- Are planning documents forward-looking, or have they become changelogs?
- Do comments remove effort, or do they add another layer to reconcile?

## 8. Disturbance Checklist

Common sources of aesthetic friction:

- a file that has become the dumping ground for unrelated responsibilities
- repeated setup rituals that make every change feel heavier
- names that describe implementation mechanics instead of domain meaning
- adapter or transport concepts leaking into core project vocabulary
- tests that require reading too much scaffolding before the scenario appears
- commands whose purpose or safe usage is hard to infer
- docs that hide the actual entry point
- generic helpers that make the common path harder to read
- compatibility wrappers kept after their current purpose has expired
- a beautiful local abstraction that makes the whole project harder to navigate

## 9. Output Discipline

- Ground aesthetic judgments in concrete artifacts.
- Explain the maintainer experience: what becomes easier, calmer, more obvious, more fragile, or more tiring.
- Keep taste preferences separate from disturbances that create real friction.
- Prefer small, high-leverage guidance over sweeping rewrites.
- Name what should be protected, not only what should change.
