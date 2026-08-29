# Aesthetic Review Areas

Select only the review areas that apply to the repository. The goal is to understand the project's design and maintenance experience. Do not produce a complete defect list.

## 1. Intended Structure

- What design does this project intend to use?
- Which documents, module boundaries, commands, or naming conventions reveal that intent?
- Does the implementation support the stated direction?
- Does it move the project to a different direction?
- If there are no design documents, what structure do the current layout and vocabulary imply?

## 2. Cognitive Clarity and Simplicity

- Does the code express the underlying idea directly?
- Are important concepts split across too many files?
- Does unnecessary process hide them?
- Are helpers, constants, schemas, prompts, adapters, and test setup in the location that a maintainer expects?
- Does an abstraction reduce comprehension work, or move that work to another location?
- Is there a clear location for the next likely change?

## 3. Language and Framework Use

- Does the code use the normal features and conventions of each language?
- In Python, notice plain functions, context managers, and simple data shapes. Notice useful dataclasses or typed models. Assess whether tests are readable. Use classes only when they clarify ownership.
- In TypeScript or JavaScript, notice meaningful types and clear asynchronous control flow. Notice framework conventions and object structures that communicate intent.
- In Swift, Rust, Go, Ruby, SQL, shell, or another language, identify the local conventions from the ecosystem and existing code.
- Then assess whether the code follows those conventions.
- Do not use a language feature only to show language knowledge. Use it when it makes an idea clearer, safer, or easier to maintain.

## 4. Developer Experience and Joy

- How easily can a new maintainer find the primary modules and entry points?
- Do setup, commands, logs, errors, tests, fixtures, and documents create confidence or concern?
- Are important workflows visible, memorable, and named in ways that help?
- Do tests teach the system, or do they merely enforce implementation details?
- Which names, tools, documents, errors, or boundaries help a maintainer understand the project?

## 5. Composition, Naming, and Vocabulary

- Do names carry the right level of abstraction?
- Does the folder structure clearly show the project organization?
- Do multiple modules appear to own the same primary behavior?
- Does the project use several words for one concept?
- Does one word refer to too many concepts?
- Does the project represent each repeated concept once? Does it keep different cases separate?

## 6. Locality and Repetition

- Does the project keep related ideas close enough for a maintainer to understand them together?
- Does repeated setup or infrastructure code increase maintenance work?
- Can a small helper, table, value object, or clear boundary reduce that work?
- Does repeated code represent necessary parallel behavior? Does it show an unnamed shared concept?
- Do wrappers, facades, re-export layers, or adapter code make ownership less obvious?

## 7. Tests and Documentation in the Maintenance Experience

- Do tests make important behavior easier to understand?
- Are fixtures and examples shaped like the domain, or like incidental implementation machinery?
- Does the documentation describe the real project, or a cleaner project that no longer exists?
- Are planning documents forward-looking, or have they become changelogs?
- Do comments remove effort, or do they add another layer to reconcile?

## 8. Maintenance-Difficulty Checklist

Common causes of maintenance difficulty:

- a file that contains unrelated responsibilities
- repeated setup steps that increase the work for each change
- names that describe implementation mechanics instead of domain meaning
- adapter or transport concepts used in core project vocabulary
- tests that require reading too much scaffolding before the scenario appears
- commands whose purpose or safe usage is hard to infer
- documents that do not identify the actual entry point
- generic helpers that make frequent operations harder to read
- compatibility wrappers kept after their current purpose has expired
- a local abstraction that makes the whole project more difficult to navigate

## 9. Output Discipline

- Ground aesthetic judgments in concrete artifacts.
- Explain the maintainer experience. State what becomes easier, clearer, more fragile, or more difficult.
- Keep personal preferences separate from maintenance difficulty.
- Prefer small guidance with verified benefit. Avoid broad rewrites.
- Name what the project must protect. Do not report only necessary changes.
