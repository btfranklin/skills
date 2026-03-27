---
name: make-repo-agent-legible
description: Improve a software repository's legibility for coding agents by turning implicit knowledge into discoverable, versioned in-repo artifacts; keeping AGENTS.md as a short map; structuring docs or other repo-local references as the system of record; and encoding architecture, quality, and operational constraints mechanically. Use when auditing or refactoring a repo for better agent autonomy, when tightening AGENTS.md and repo documentation, or when agent output suffers from missing context, architectural drift, stale docs, hidden conventions, or weak validation loops.
---

# Make Repo Agent Legible

## Overview

Make a repository easier for coding agents to navigate, modify, and validate. Treat agent legibility as the goal: if important knowledge is not versioned and discoverable inside the repo, treat it as missing.

## Workflow

1. Read the current repository entry points first:
- `AGENTS.md`
- top-level architecture and design docs
- docs indexes
- lint/test/CI config
- a representative slice of the code
2. Diagnose the main legibility failures with `references/legibility-rubric.md`. Look for missing maps, hidden conventions, stale docs, weak boundaries, and validation gaps.
3. Make `AGENTS.md` a map, not an encyclopedia. Keep it short, stable, and action-oriented. Point to deeper sources of truth instead of duplicating them.
4. Move important knowledge into the repo:
- architecture maps
- product, domain, design, or operational docs as appropriate
- execution plans and decision logs
- generated references such as schemas, contracts, or inventories
- reliability, security, and quality expectations
5. Treat `docs/` or another obvious repo-local knowledge area as the system of record for non-trivial repositories. Add indexes and cross-links so the agent can progressively discover depth instead of receiving one giant instruction blob.
6. Encode constraints mechanically wherever possible:
- boundary and dependency rules
- schema validation at the edges
- naming and logging invariants
- file-size or complexity limits
- documentation freshness and cross-link checks
7. Write remediation messages for lint and structural-test failures so another agent run can recover without human translation.
8. Increase runtime legibility when the task depends on behavior rather than static code. Make the relevant system locally runnable or inspectable, expose reproducible scripts, and give agents access to logs, metrics, traces, test harnesses, CLIs, UIs, or other feedback loops as appropriate.
9. Capture human taste once, then promote it into reusable artifacts. Convert repeated review comments and tribal knowledge into docs, helpers, lints, tests, or templates.
10. Plan for entropy. Add recurring doc-gardening, quality scoring, or targeted cleanup work so bad patterns are corrected continuously instead of in occasional cleanup sprints.
11. Report outcomes in terms of leverage:
- what was illegible
- what artifacts or enforcement were added
- what knowledge still lives outside the repo
- which next investment would most improve agent autonomy

## Default Deliverables

- A concise `AGENTS.md` that routes the agent to deeper sources.
- A repo-local knowledge structure with clear indexes.
- Architecture, operational, and planning artifacts for areas that are currently implicit.
- Mechanical checks for the highest-value invariants.
- A prioritized legibility audit with concrete next steps.

## Decision Rules

- Optimize for what a future agent run can discover and trust quickly.
- Prefer progressive disclosure over giant instruction files.
- Prefer boring, inspectable abstractions over opaque dependencies at critical boundaries.
- Enforce invariants centrally and allow flexibility inside those boundaries.
- Version plans, decisions, and standards near the code they govern.
- Treat stale documentation as a correctness problem, not a cosmetic one.

## Anti-Patterns

- A giant `AGENTS.md` that tries to teach the whole repo inline.
- Architecture that is only implied by folder names or team memory.
- Standards that exist only in chat threads, PR comments, or oral tradition.
- Lints that fail without telling the agent how to recover.
- Validation that checks syntax but not runtime behavior.
- Manual recurring cleanup with no codified principle behind it.

## Resources

### references/

- `legibility-rubric.md`: audit dimensions, failure modes, and prioritization checklist.
- `artifact-patterns.md`: recommended document set, layout patterns, and enforcement ideas.
