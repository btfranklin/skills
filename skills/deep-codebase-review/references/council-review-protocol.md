# Council Review Protocol

Use this protocol when a deep review should be split across specialist reviewers. The coordinator owns the final judgment and must produce one coherent report.

## Activation Rules

- Use sub-agent council mode by default for broad codebase reviews and substantial PR or branch reviews.
- If sub-agent tools are available, use them unless the user explicitly asks for a solo review or says not to use sub-agents.
- Do not treat the user's failure to mention sub-agents, council mode, delegation, or parallel review as an opt-out.
- Do not use council mode when the user asks for a solo review, disables sub-agents, or requests an ordinary small-diff review.
- Do not spawn specialists for ordinary small-diff reviews.
- Before delegating, state that council mode is being used and name the specialist roles being assigned.
- Keep the council small: start with three to four specialists, then add an optional specialist only when the repo or PR clearly needs that lens.
- Give each specialist a distinct scope. Do not ask several agents to perform the same generic review.
- No silent solo fallback: if council mode would normally apply but sub-agents are unavailable or blocked, explain the blocker and ask whether to continue with a solo multi-pass review.

## Core Roster

- `Coordinator / Lead Reviewer`: Establish intent, choose specialists, keep scope bounded, verify key claims, reconcile disagreements, and write the final report.
- `Correctness and Lifecycle Reviewer`: Review behavior, edge cases, state transitions, persistence, cleanup, retries, idempotency, concurrency, and async continuation risks.
- `Architecture and Boundary Reviewer`: Review domain boundaries, coupling, module shape, ownership, adapter leakage, stale abstractions, and half-finished refactors.
- `Tests and Contract Reviewer`: Review whether tests encode the right contract, miss risk-heavy scenarios, overfit implementation details, or preserve the wrong structure.
- `Code Aesthetics, Local Simplicity, and Maintainability Reviewer`: Review whether the code is clean, intelligent, and elegantly organized, including duplicated ceremony, naming, noisy plumbing, tangled conditionals, needless wrappers, and whether the next change has an obvious home.

## Optional Specialists

Add only when the touched surface warrants it:

- `Security and Data Reviewer`: Auth, permissions, secrets, tenant isolation, privacy, destructive actions, and untrusted input.
- `Operations and Infrastructure Reviewer`: Configuration, deployment, observability, migrations, background jobs, rollback, retention, and operator workflows.
- `Frontend and API Reviewer`: UI state, accessibility, API contracts, loading/error states, compatibility, and client/server ownership.
- `AI, Prompting, and Structured Output Reviewer`: Prompt ownership, model/provider coupling, tool permissions, structured-output validation, evals, and traceability.
- `Documentation and Roadmap Reviewer`: Whether planning docs, architecture docs, comments, and public claims match the current implementation.

## Specialist Task Template

Use this shape when delegating. Fill in the repo, branch, PR, or changed-area context before sending.

```text
You are the [ROLE] for a deep codebase review.

Scope:
- Review only [FILES / MODULES / PR OR BRANCH SCOPE].
- Focus on [ROLE-SPECIFIC CONCERNS].
- Do not perform a generic review outside this scope.

Output:
- Findings with exact file/line evidence whenever possible.
- For each finding, explain the mechanism of harm or debt accumulation.
- Separate concrete findings from pressure points.
- Include severity: Critical, High, Medium, Low, or Pressure Point.
- Mark uncertainty explicitly when a claim depends on an assumption.
- Mention tests or docs only when they affect the reviewed contract.
- Keep the report concise and actionable.

Do not edit files. Do not paste broad summaries of unrelated code.
```

## Evidence Ledger

Before writing the final report, normalize specialist output into a private ledger:

- `claim`: the asserted bug, risk, drift, or pressure point.
- `evidence`: exact file/line references or concrete repo artifacts.
- `mechanism`: how it fails, compounds, or blocks the intended design.
- `severity`: final severity after coordinator review.
- `corroboration`: which specialists agree, conflict, or provide related evidence.
- `verification`: whether the coordinator checked the claim directly.
- `disposition`: final finding, pressure point, roadmap note, open question, or discarded.

## Consolidation Rules

- Do not paste raw specialist reports into the final answer.
- Deduplicate findings that share the same mechanism, even if specialists found them through different files.
- Prefer the most concrete mechanism and strongest evidence when merging related claims.
- Resolve contradictions by checking source files yourself. If the evidence remains ambiguous, downgrade to an open question or residual risk.
- Discard unsupported claims, vague style preferences, and observations without a clear downside.
- Promote an item to a finding only when there is a concrete bug risk, data-integrity issue, maintainability hazard, design contradiction, or likely regression path.
- Keep pressure points separate from findings when the risk is plausible but not yet harmful.
- The final report should read as one review from one lead reviewer: findings first, then structural pressure points, roadmap/design alignment, open questions, and follow-through.
