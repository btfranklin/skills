---
name: deep-codebase-review
description: >-
  Use when reviewing an entire codebase, architecture, technical debt, structural quality, cleanup opportunities, or a substantial PR or branch. Produce evidence-backed findings about boundaries, lifecycle and concurrency, duplication, tests, plans, and maintainability. Do not use for small diffs, narrow bug fixes, frontend visual QA, repo-onboarding documentation, or OpenAI Agents SDK production-readiness review.
---

# Deep Codebase Review

Review how a system is bending, not merely whether isolated code works. Prioritize concrete structural and behavioral risks, then identify pressure points that will become expensive if left alone.

## Workflow

### 1. Bound the review

- Identify whether the target is a whole repository, merge-base diff, branch, or named set of modules.
- For a PR or branch, inspect the diff first. Expand only into dependencies, contracts, tests, and design documents needed to judge the change.
- State material scope exclusions and coverage limits in the report.

### 2. Establish intent

- Read repo-local instructions and the architecture, planning, roadmap, and package documents relevant to the bounded scope.
- Infer the intended shape from the implementation when explicit design guidance is absent, and label the inference.

### 3. Build breadth before depth

- Scan the relevant tree and sample every major layer within scope before drilling into suspicious areas.
- Load [references/review-lenses.md](references/review-lenses.md) and select the lenses that fit the system.
- Include tests and forward-looking plans when they define or contradict the intended contract.

### 4. Classify and verify

- Promote an observation to a finding only when it has a concrete downside: correctness risk, data-integrity risk, maintainability hazard, design contradiction, or likely regression path.
- Classify plausible future fragility without present harm as a pressure point.
- Cite exact files and lines whenever possible. Explain the failure or debt mechanism and label assumptions.
- Identify the duplicated pattern and likely extraction seam before recommending reuse.

## Council Mode

Use a small sub-agent council by default for whole-codebase reviews and substantial PR or branch reviews when sub-agents are available. Load [references/council-review-protocol.md](references/council-review-protocol.md) before delegating.

If sub-agents are unavailable, disclose the limitation and continue with the same role-based passes solo. Stop for confirmation only when the user explicitly required a council. Never paste raw specialist reports; verify and consolidate their evidence into one judgment.

## Output

Present:

1. Findings ordered by severity.
2. Structural pressure points and likely refactors.
3. Roadmap or design alignment.
4. Open questions and residual risk.
5. Highest-leverage follow-through.

Say explicitly when there are no concrete findings. Keep testing gaps and pressure points visible without inflating them into defects. For a concrete report model, read [examples/review-output.md](examples/review-output.md).

## Follow-Through

- Prefer a few high-signal corrections over broad cleanup or speculative redesign.
- When the user requests fixes, update a planning document only if it already serves as the authoritative forward-looking record, the accepted change alters future work, and documentation edits are within the requested scope.
- Keep forward-looking plans distinct from changelogs.
