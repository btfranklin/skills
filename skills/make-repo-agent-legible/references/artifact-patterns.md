# Agent-Legible Artifact Patterns

Use these patterns when turning repository knowledge into durable, discoverable artifacts.

## Minimal Artifact Set

Create or tighten these first:

- `AGENTS.md`: short map of the repo and how to work in it.
- `ARCHITECTURE.md`: top-level domain and layer map.
- `docs/`: indexed knowledge base for deeper material.
- repo-local plans for non-trivial work.
- CI or lint checks for the most important invariants.

## Suggested `docs/` Layout

Adjust to the repo size and repo type. This is an illustrative pattern, not a required tree:

```text
docs/
├── design-docs/
│   ├── index.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── ...
├── domain-specs/
│   ├── index.md
│   └── ...
├── references/
│   └── ...
├── ARCHITECTURE.md
├── INTERFACES.md
├── PLANS.md
├── OPERATIONS.md
├── QUALITY.md
├── RELIABILITY.md
└── SECURITY.md
```

Do not create the whole tree blindly. Add only the slices the repository can keep current, and rename them to fit the repository's actual shape.

## Document Roles

`AGENTS.md`
- Keep it short.
- Route by task type.
- Link to commands, architecture maps, and deeper docs.

`ARCHITECTURE.md`
- Explain domains, layers, interfaces, and dependency directions.
- Show what is forbidden, not only what exists.

`docs/design-docs/`
- Store durable reasoning about major systems and patterns.
- Index the documents and mark outdated material clearly.

`docs/exec-plans/`
- Store active plans, completed plans, and debt tracking.
- Keep plans versioned when the work spans multiple iterations.

`docs/generated/`
- Store generated references the agent should not have to rediscover from live systems, builds, schemas, inventories, or external tools.

`docs/references/`
- Store external or third-party references that matter repeatedly.

## Enforcement Ladder

Promote important rules through this ladder:

1. Ad-hoc review comment
2. Repo guideline
3. Shared helper or template
4. Lint rule or structural test
5. CI gate with actionable remediation text

If a problem repeats, move it up the ladder.

## Good Candidate Invariants

- Dependency direction between layers or packages
- Schema validation at external boundaries
- Structured logging shape
- Naming rules for types and schemas
- Maximum file size or function complexity in fragile areas
- Required docs indexes and cross-links
- Freshness checks for generated docs or references

## Runtime Legibility Upgrades

Use these when static structure is not enough:

- boot or entrypoint scripts that work per worktree or branch
- deterministic smoke tests for critical journeys
- browser automation or terminal-driven repros when interaction matters
- local logs, metrics, trace access, or state inspection tools
- reproducible fixtures, test corpora, and seed data

## Dependency Heuristic

Prefer dependencies and abstractions that the repository can inspect, test, and explain. If a critical third-party helper is opaque and repeatedly confuses the agent, consider wrapping it tightly or replacing the small subset you actually need.

## Delivery Standard

Finish with a concrete before/after summary:

- what the agent could not previously discover
- what artifact or enforcement now makes it visible
- what still requires future work
