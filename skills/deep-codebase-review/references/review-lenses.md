# Review Lenses

Use these lenses selectively. Do not force every lens onto every repository, but do enough passes that the review covers correctness, clean code quality, and long-term maintainability.

In council mode, these lenses can guide specialist assignments, but the coordinator must synthesize the results into one report. Do not expose raw specialist notes as separate review sections.

## 1. System Intent

- What is the intended shape of the system?
- Which documents, conventions, or module boundaries define that shape?
- Has the implementation drifted from that intent?
- Are recent additions reinforcing the intended architecture or quietly replacing it?

## 2. Domain Boundaries

- Are core domain concepts distinct from adapters, UI, transport, or storage details?
- Are infrastructure concerns leaking into business/domain models?
- Are names still honest about what the code does?
- Are multiple layers solving the same problem differently?

## 3. Ownership and Lifecycle

- Is object ownership clear and enforced?
- Are creation, update, deletion, and cascade rules coherent?
- Are retained artifacts intentionally durable, or just never cleaned up?
- Are there records that outlive the data or tenant they conceptually belong to?

## 4. State Machines and Invariants

- Are statuses and transitions explicit?
- Can rows or jobs be processed twice?
- Are timeout, cancellation, retry, and failure states modeled clearly?
- Are invariants enforced in code, transaction boundaries, or constraints?

## 5. Concurrency and Idempotency

- Could multiple workers process the same work item?
- Is there a crash window between “side effect happened” and “state marked complete”?
- Are async paths reserving work safely?
- Do repeated inputs or retries create duplicates or drift?

## 6. Duplication and Missing Reuse

- Are similar workflows implemented in parallel with only small differences?
- Is there repeated adapter metadata handling, reservation logic, status updates, or serialization code?
- Would a shared helper reduce future bugs, or would it just hide healthy differences?
- Is there an obvious seam for extraction that has not been taken yet?

## 7. Local Simplicity and Elegance

- Does the code express the underlying idea directly, or does ceremony hide it?
- Are names, helpers, and module boundaries aesthetically coherent enough that the next change has an obvious home?
- Is the code DRY in the useful sense: shared concepts are represented once, while genuinely different cases remain separate?
- Are there over-abstracted layers, clever shortcuts, or generic helpers that make the common path harder to understand?
- Are there tangled conditionals, duplicated setup, or noisy plumbing that could become a small table, value object, helper, or clearer domain concept?

## 8. Module Shape

- Is a file turning into a catch-all or god module?
- Are public service boundaries clear?
- Are responsibilities grouped by domain behavior or by accident of history?
- Would a new feature likely extend an existing clean seam, or force edits in several unrelated places?

## 9. Data Modeling

- Do tables/models reflect the real concepts, or are they transport-shaped compromises?
- Are there denormalized fields that will drift from their true source?
- Are soft assumptions about uniqueness, ordering, or ownership left unenforced?
- Does the schema still match the product direction?

## 10. Prompting and AI-Specific Boundaries

- Are prompts explicit, inspectable, and externalized?
- Are model-specific behaviors creeping into code paths that should stay generic?
- Is prompt rendering simple and owned locally, or hidden behind unnecessary abstraction?
- Are structured-output assumptions validated, or just hoped for?

## 11. Testing Surface

- Do tests cover the architecture’s actual risk points, or mostly the easy paths?
- Are there scenario tests for lifecycle boundaries, retries, async continuations, and cleanup?
- Are tests readable enough to support future changes?
- Is fixture setup duplicated enough to justify factories or helpers?

## 12. Operability

- Can an operator tell what happened, why it happened, and what is stuck?
- Are logs, traces, or admin views aligned with the real failure modes?
- Is configuration validated early enough?
- Are retention and cleanup policies explicit?

## 13. Plan and Documentation Alignment

- Does the roadmap still point at the real next work?
- Are planning docs forward-looking, or have they turned into changelogs?
- Do comments and docs reflect the current architecture?
- Has new code introduced future refactor needs that should be recorded?

## 14. Smell Checklist

Common review triggers:

- a scheduler loop that keeps accumulating unrelated responsibilities
- a service module that owns orchestration, business logic, and transport details at once
- code that is correct only after tracing several needless layers or similarly shaped branches
- repeated string constants or metadata conventions scattered across files
- duplicated transaction wrappers or reservation patterns
- direct adapter objects leaking into core runtime paths
- “temporary” one-off implementations that already have two or three siblings
- persistent data without explicit deletion or retention rules
- tests that prove a feature works but not that it behaves safely under restart or duplication

## 15. Output Discipline

- Findings should be concrete, evidenced, and ranked.
- Pressure points should be explicit about why they are not yet findings.
- Keep cleanup suggestions scoped to the likely next refactor, not a full rewrite.
- Preserve the user’s architectural goals; do not recommend abstractions that fight the intended system shape.
- For council reviews, reconcile duplicate or conflicting claims before reporting them.
