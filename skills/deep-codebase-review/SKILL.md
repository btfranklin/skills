---
name: deep-codebase-review
description: >-
  Use when the user asks for a broad codebase review, substantial PR or branch review, architecture audit, tech-debt scan, cleanup assessment, structural sanity check, or verification that recent implementation still aligns with long-term design. This skill's default workflow is a sub-agent council review: when sub-agent tools are available, use specialist sub-agents unless the user explicitly asks for a solo review or says not to use sub-agents. Do not treat the user's failure to mention sub-agents as an opt-out. Focus on cruft, duplication, unclear boundaries, anti-patterns, missed reuse, lifecycle/concurrency risks, test and roadmap drift, and locally inelegant code shape. Do not use for a narrow bug fix, ordinary code review focused only on a small diff, frontend visual QA, repo-onboarding docs, or production-readiness review of an OpenAI Agents SDK system. Output findings first with file/line evidence, then structural pressure points, roadmap/design alignment notes, open questions, and concrete follow-through.
---

# Deep Codebase Review

Perform a broad structural review rather than a narrow bug hunt. Look for the places where the codebase is starting to bend: duplicated patterns, weak boundaries, missing shared abstractions, stale plans, hidden lifecycle risks, inelegant local structure, and shortcuts that will compound later.

## Review Workflow

### 1. Establish the intended shape first

- Read the planning docs, architecture notes, roadmap, and any repo-specific guidance before judging structure.
- Summarize the intended system shape in a few sentences for yourself before drawing conclusions.
- If the repo has no explicit design docs, infer the intended shape from naming, layout, and current abstractions, and state that inference clearly.

### 2. Build breadth before depth

- Scan the repository structure first with fast file and text search.
- Read enough files to understand boundaries, ownership, critical services, async paths, configuration, and tests.
- Prefer sampling all major layers before drilling deep into one file.
- When the codebase has a roadmap or plan document, compare that document against the current implementation while reviewing.

### 3. Review through multiple lenses

- Load [references/review-lenses.md](references/review-lenses.md) and use the sections that fit the codebase.
- Prioritize behavioral and structural risks over cosmetic cleanup.
- Treat duplication, implicit contracts, unnecessary complexity, and misplaced concepts as first-class review concerns, not secondary polish.
- Look for code whose local shape obscures the simple idea underneath: awkward naming, needless indirection, over- or under-abstraction, repeated ceremony, tangled conditionals, and modules that are correct but hard to read or extend.
- Treat compatibility shims, facade layers, re-export modules, and backwards-compatible wrappers as structural costs unless they serve a concrete current need.
- Prefer the forward-looking end-state when judging refactors; if a compatibility layer makes ownership or behavior less obvious, call that out.

### 4. Separate findings from pressure points

- Call something a finding when it has a concrete downside: bug risk, race condition, data-integrity issue, maintainability hazard, design contradiction, or likely regression path.
- Call something a pressure point when it is not broken yet but is on track to become expensive or fragile.
- Keep speculation clearly labeled. Do not present a stylistic preference as a defect.

### 5. Require evidence

- Cite exact files and lines for findings whenever possible.
- Explain the mechanism of failure or debt accumulation, not just the surface smell.
- If a concern depends on a runtime assumption, say so explicitly.
- If you think reuse is missing, identify the duplicated pattern and the likely seam for extraction.

### 6. Review the tests and plans too

- Check whether tests reinforce the intended architecture or quietly encode the wrong shape.
- Check whether roadmap or design documents are stale, misleading, or still missing key work that the code now depends on.
- Note when docs imply a cleaner or more complete state than the code actually provides.

## Default Council Mode

Council mode with sub-agents is the default for broad codebase reviews and substantial PR or branch reviews. If the current environment exposes sub-agent tools, use them unless the user explicitly asks for a solo review, disables sub-agents, or requests an ordinary small-diff review. The user does not need to say "sub-agent", "council", "parallel", or "delegate" for this default to apply.

Load [references/council-review-protocol.md](references/council-review-protocol.md) before delegating. Before spawning specialists, state briefly that council mode is being used and name the reviewer roles being delegated.

In council mode, the main agent is the coordinator. Specialist outputs are evidence inputs, not report sections. Assign distinct scopes, require concrete file/line evidence, reconcile contradictions, verify important claims yourself, and then produce one consolidated review.

No silent solo fallback: if council mode would normally apply but sub-agents cannot be spawned because the environment does not expose them or blocks them, explain the blocker and ask whether to continue with a solo multi-pass review.

For a user-requested solo review, run the same role-based passes locally: correctness and lifecycle, architecture and boundaries, tests and contracts, and code aesthetics, local simplicity, and maintainability.

## Output Standard

Default output order:

1. Findings, ordered by severity.
2. Structural pressure points and likely refactors.
3. Roadmap or design alignment notes.
4. Open questions or residual risk.

When the user asked for a review, keep findings primary. If there are no concrete findings, say so explicitly and still report the most important pressure points and testing gaps.

For a worked report shape, read [examples/review-output.md](examples/review-output.md) when producing a full written audit.

## Practical Heuristics

- Prefer a small number of high-signal findings over a long list of nits.
- Look for repeated transactional patterns, lifecycle code, adapter glue, and state transitions that want a shared helper or contract.
- Look for god modules early; they are easier to split before more features land.
- Look for elegant reductions: places where a small, well-named helper, value object, table-driven shape, or clearer boundary would make the code shorter, more obvious, and less error-prone.
- Look for domain leakage where adapter-specific or UI-specific concepts have crept into the core model.
- Look for stale abstractions that were right one milestone ago but now force awkward workarounds.
- Look for refactors that stopped halfway and left compatibility surfaces behind; do not treat preserving old import paths or old module shapes as inherently positive.
- When a split introduces a thin facade solely to avoid updating call sites, treat that as a likely review concern rather than a neutral implementation detail.
- Look for retention, cleanup, idempotency, and restart behavior in any persistent or asynchronous system.
- Treat tests, logging, and operator visibility as part of structure, not as optional add-ons.

## Follow-Through

- If the user wants fixes after the review, update the relevant roadmap or planning document in the same turn when the future work changes.
- Preserve the distinction between forward-looking planning documents and changelogs.
