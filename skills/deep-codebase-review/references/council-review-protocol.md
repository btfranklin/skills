# Council Review Protocol

Use this protocol for a broad review that benefits from distinct specialist passes. The coordinator owns scope, verification, judgment, and the final report.

## Activation

- Use council mode for whole-codebase reviews and substantial PR or branch reviews when sub-agents are available.
- Do not delegate ordinary small-diff reviews or user-requested solo reviews.
- If delegation is unavailable, disclose the limitation and continue with equivalent solo passes unless the user explicitly required a council.
- Before delegating, name the roles and their non-overlapping scopes.
- Start with three or four specialists; add an optional role only when the reviewed surface warrants it.

## Core Roles

- `Coordinator / Lead Reviewer`: Bound the review, establish intent, verify important claims, reconcile disagreements, and write the report.
- `Correctness and Lifecycle Reviewer`: Review behavior, state transitions, persistence, cleanup, retries, idempotency, concurrency, and async continuation.
- `Architecture and Boundary Reviewer`: Review ownership, coupling, module shape, adapter leakage, stale abstractions, and incomplete refactors.
- `Tests and Contract Reviewer`: Review risk-heavy scenarios, architectural contracts, implementation overfitting, and misleading coverage.
- `Code Aesthetics and Maintainability Reviewer`: Review naming, local simplicity, repeated ceremony, noisy plumbing, needless wrappers, and whether the next change has an obvious home.

## Optional Roles

- `Security and Data Reviewer`: Auth, permissions, secrets, privacy, destructive actions, untrusted input, and tenant isolation.
- `Operations and Infrastructure Reviewer`: Configuration, deployment, observability, migrations, background work, rollback, and retention.
- `Frontend and API Reviewer`: UI state, accessibility, API contracts, loading and error states, and client/server ownership.
- `AI and Structured Output Reviewer`: Prompt ownership, provider coupling, tool permissions, validation, evals, and traceability.
- `Documentation and Roadmap Reviewer`: Whether plans, architecture documents, comments, and public claims match the implementation.

## Specialist Assignment

Give each specialist this contract:

```text
You are the [ROLE] for a deep codebase review.

Scope:
- Review only [FILES / MODULES / DIFF].
- Focus on [ROLE-SPECIFIC CONCERNS].
- Do not edit files or expand into a generic review.

Return:
- Concise findings with exact file and line evidence when possible.
- The mechanism of harm or debt accumulation.
- Classification as Critical, High, Medium, Low, or Pressure Point.
- Explicit uncertainty and relevant contract gaps.
```

## Consolidation

Normalize useful claims into a private ledger containing `claim`, `evidence`, `mechanism`, `severity`, `corroboration`, `verification`, and `disposition`.

- Verify important claims directly.
- Merge claims that share a mechanism and preserve the strongest evidence.
- Resolve conflicts from source; downgrade unresolved ambiguity to an open question.
- Discard unsupported claims, vague preferences, and observations without a concrete downside.
- Keep pressure points separate from findings.
- Produce one report in the lead reviewer's voice, never a bundle of specialist summaries.
