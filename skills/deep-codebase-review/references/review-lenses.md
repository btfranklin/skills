# Review Areas

Select only the review areas that apply to the repository. Review enough areas to cover correctness, code quality, and long-term maintenance.

In council mode, use these review areas to assign specialist work. The coordinator must combine the results into one report. Do not include specialist notes as separate report sections.

## 1. System Intent

- What is the intended structure of the system?
- Which documents, conventions, or module boundaries define that structure?
- Has the implementation changed from that intent?
- Do recent additions support the intended architecture or replace it without an explicit decision?

## 2. Domain Boundaries

- Are core domain concepts distinct from adapters, UI, transport, or storage details?
- Do business or domain models contain infrastructure concerns?
- Do names describe what the code does?
- Are multiple layers solving the same problem differently?

## 3. Ownership and Lifecycle

- Is object ownership clear and enforced?
- Are creation, update, deletion, and cascade rules coherent?
- Does the system retain artifacts intentionally, or does it omit cleanup?
- Are there records that outlive the data or tenant they conceptually belong to?

## 4. State Machines and Invariants

- Are statuses and transitions explicit?
- Can the system process rows or jobs twice?
- Are timeout, cancellation, retry, and failure states modeled clearly?
- Are invariants enforced in code, transaction boundaries, or constraints?

## 5. Concurrency and Idempotency

- Can multiple workers process the same work item?
- Is there a crash window between “side effect happened” and “state marked complete”?
- Are async paths reserving work safely?
- Do repeated inputs or retries create duplicates or inconsistent state?

## 6. Duplication and Missing Reuse

- Are similar workflows implemented in parallel with only small differences?
- Is there repeated adapter metadata handling, reservation logic, status updates, or serialization code?
- Can a shared helper reduce future defects without hiding necessary differences?
- Is there a clear boundary for a shared implementation?

## 7. Traceability and Change Cost

- Can a reviewer trace a behavior through the necessary modules without unrelated paths?
- Does a small behavior change require edits in unrelated modules?
- Do repeated concepts have one implementation, or can parallel implementations become inconsistent?
- Do abstractions hide ownership, state changes, or control flow?
- Does each expected future change have a clear implementation location?
- Can a smaller interface or helper reduce a verified maintenance cost?

## 8. Module Structure

- Does a file contain many unrelated responsibilities?
- Are public service boundaries clear?
- Are responsibilities grouped by domain behavior?
- Does a new feature have a clear module boundary?
- Does it require edits in several unrelated places?

## 9. Data Modeling

- Do tables/models reflect the real concepts, or are they transport-shaped compromises?
- Are there denormalized fields that can become inconsistent with the authoritative source?
- Are soft assumptions about uniqueness, ordering, or ownership left unenforced?
- Does the schema still match the product direction?

## 10. Prompting and AI-Specific Boundaries

- Are prompts explicit, inspectable, and externalized?
- Do model-specific behaviors enter code paths that must remain generic?
- Is prompt rendering simple and owned locally, or hidden behind unnecessary abstraction?
- Does validation enforce the structured-output assumptions?

## 11. Test Coverage

- Do tests cover the important architecture risks?
- Are there scenario tests for lifecycle boundaries, retries, async continuations, and cleanup?
- Are tests readable enough to support future changes?
- Does repeated fixture setup have a verified maintenance cost that a factory or helper can reduce?

## 12. Operability

- Can an operator tell what happened, why it happened, and what is stuck?
- Are logs, traces, or admin views aligned with the real failure modes?
- Is configuration validated early enough?
- Are retention and cleanup policies explicit?

## 13. Plan and Documentation Alignment

- Does the roadmap still point at the real next work?
- Are planning documents forward-looking, or have they become changelogs?
- Do comments and documentation reflect the current architecture?
- Has new code introduced future refactor needs that require a record?

## 14. Common Risk Patterns

Common review triggers:

- a scheduler loop that keeps accumulating unrelated responsibilities
- a service module that owns orchestration, business logic, and transport details
- code that requires review across unnecessary layers or similar branches
- repeated string constants or metadata conventions scattered across files
- duplicated transaction wrappers or reservation patterns
- direct adapter objects used in core runtime code
- temporary implementations that have two or three similar implementations
- persistent data without explicit deletion or retention rules
- tests that prove a feature works but not that it behaves safely under restart or duplication

## 15. Output Discipline

- Findings must be specific, supported by evidence, and ranked.
- For each future risk, state why it is not a finding.
- Limit cleanup suggestions to the next supported refactor. Do not recommend a full rewrite without evidence.
- Preserve the user’s architectural goals. Do not recommend abstractions that conflict with the intended system structure.
- For council reviews, reconcile duplicate or conflicting claims before reporting them.
