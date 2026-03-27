# Repo Legibility Rubric

Use this rubric to audit how well a repository supports coding-agent autonomy.

## Audit Order

1. Read the entry points.
2. Score the repo across the dimensions below.
3. Fix the highest-leverage missing artifact or enforcement first.
4. Prefer adding durable structure over adding more prompt text.

## Dimensions

### 1. Entry-Point Map

Good state:
- `AGENTS.md` is short and current.
- It points to the real sources of truth.
- It tells the agent where to look next by task type.

Failure modes:
- `AGENTS.md` is huge, stale, or contradictory.
- The only way to learn the repo is by reading lots of random files.
- The agent must rediscover obvious navigation rules every run.

High-leverage fixes:
- Shrink `AGENTS.md` into a table of contents.
- Add direct links to architecture, docs indexes, plans, and test commands.

### 2. Repository System Of Record

Good state:
- Product, domain, design, architecture, operational, reliability, and security knowledge live in versioned repo artifacts as appropriate to the repository.
- Important decisions are documented near the codebase, not in external tools only.
- Docs have indexes and clear ownership.

Failure modes:
- Slack, Notion, or PR comments are the actual source of truth.
- Docs exist but have no structure, index, or freshness signal.
- Generated references such as schemas or API contracts are missing from the repo.

High-leverage fixes:
- Create a `docs/` structure with indexes.
- Add versioned decision logs and execution plans for non-trivial work.
- Check in generated reference artifacts that agents repeatedly need.

### 3. Architecture Discoverability

Good state:
- Domains, layers, and dependency directions are explicit.
- Cross-cutting concerns have named entry points.
- The repository explains why the main boundaries exist.

Failure modes:
- Folder structure is the only architecture documentation.
- Agents can create new edges without any visible rule.
- Important abstractions are hidden inside large utilities or framework magic.

High-leverage fixes:
- Add `ARCHITECTURE.md` or a top-level domain map.
- Describe permissible dependency directions and interfaces.
- Prefer abstractions the repo can fully inspect and test.

### 4. Mechanical Enforcement

Good state:
- The most important rules are enforced by linters, structural tests, or CI checks.
- Failure messages explain the intended recovery path.
- Boundary validation happens at system edges.

Failure modes:
- Standards are written down but never checked.
- Enforcement exists but produces opaque failures.
- Agents must guess data shapes from usage instead of validating boundaries.

High-leverage fixes:
- Add structural tests for dependency direction and naming rules.
- Validate schemas at boundaries.
- Improve lint output so it teaches the repair.

### 5. Task And Decision Memory

Good state:
- Non-trivial work has execution plans, progress logs, and completed artifacts.
- Technical debt is tracked in-repo.
- Agents can understand why prior work happened.

Failure modes:
- Large tasks live only in issue trackers or human memory.
- There is no durable record of tradeoffs.
- Refactors repeat because prior decisions are invisible.

High-leverage fixes:
- Add `docs/exec-plans/active`, `completed`, and a debt tracker.
- Version the acceptance criteria and decision notes with the code.

### 6. Runtime Legibility

Good state:
- The agent can run or inspect the relevant system, reproduce issues, and inspect runtime signals.
- Logs, metrics, traces, or test harnesses are accessible locally.
- Validation covers the important execution paths, not only static correctness.

Failure modes:
- The relevant service, package, CLI, job runner, or app is hard to run per branch or worktree.
- Runtime evidence is only visible to humans in remote dashboards.
- Bug fixing depends on hand-transcribed screenshots or anecdotes.

High-leverage fixes:
- Make the relevant runtime or tooling bootable or inspectable in isolated local environments.
- Provide scripts for repros, smoke tests, or deterministic command sequences.
- Expose runtime signals the agent can query directly.

### 7. Entropy Control

Good state:
- Golden principles are written down and enforced continuously.
- Cleanup work happens in small recurring increments.
- Quality grades or focused audits catch drift early.

Failure modes:
- The repo accumulates agent-generated drift until humans do a large cleanup.
- Bad patterns spread because nothing scans for them.
- Review feedback stays local to a single PR.

High-leverage fixes:
- Define a small set of golden principles.
- Add recurring doc-gardening or cleanup runs.
- Track quality scores or a short prioritized debt list.

## Prioritization Rule

Fix missing maps and missing enforcement before polishing prose. A shorter, better-linked repo with reliable checks usually produces more leverage than a larger body of instructions.

## Output Format

When reporting an audit, structure it as:

1. Current legibility strengths.
2. Highest-severity gaps.
3. The next one to three repo changes with the best leverage.
4. What still remains off-repo or unenforced.
