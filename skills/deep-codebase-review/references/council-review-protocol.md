# Council Review Protocol

Use this protocol for a broad review that needs separate specialist reviews. The coordinator controls the scope, verification, assessment, and final report.

## Activation

- Use council mode for whole-repository reviews when sub-agents are available.
- Also use it for substantial pull request or branch reviews.
- Do not delegate a small-diff review.
- Do not delegate a review when the user requests a solo review.
- If delegation is not available, state this limit.
- Continue with equivalent solo reviews unless the user required a council.
- Before delegating, name the roles and their non-overlapping scopes.
- Start with three or four specialists.
- Add an optional role only when the scope needs it.

## Core Roles

- `Coordinator / Lead Reviewer`: Define the scope. Establish intent. Verify important claims. Resolve disagreements. Write the report.
- `Correctness and Lifecycle Reviewer`: Review behavior, state transitions, persistence, cleanup, retries, idempotency, concurrency, and async continuation.
- `Architecture and Boundary Reviewer`: Review ownership, coupling, module structure, adapter use, stale abstractions, and incomplete refactors.
- `Tests and Contract Reviewer`: Review risk-heavy scenarios, architectural contracts, implementation overfitting, and misleading coverage.
- `Maintainability and Change-Cost Reviewer`: Identify behavior that is difficult to trace. Identify changes that cross unnecessary boundaries. Identify repeated code that can become inconsistent. Identify code that hides ownership or control flow. Identify future changes that do not have a clear location. Report only specific maintenance risks or structural future risks. Exclude aesthetic preferences, language conventions, developer joy, beauty, and naming preferences that do not have a specific maintenance cost.

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
- Classification as Critical, High, Medium, Low, or Future Risk.
- Explicit uncertainty and relevant contract gaps.
```

## Consolidation

Record useful claims in a private list. Use the fields `claim`, `evidence`, `mechanism`, `severity`, `corroboration`, `verification`, and `disposition`.

- Verify important claims directly.
- Merge claims that have the same cause. Preserve the strongest evidence.
- Resolve conflicts with the source code or documents.
- Change an unresolved conflict to an open question.
- Discard unsupported claims, vague preferences, and observations without a concrete downside.
- Keep future risks separate from findings.
- Produce one report with a consistent writing style. Do not return separate specialist summaries.
