---
name: make-repo-agent-legible
description: >-
  Use when auditing or refactoring a software repo so coding agents can navigate, modify, and validate it autonomously: README front door, short AGENTS.md map, repo-local docs as system of record, architecture/operations/quality artifacts, indexes, cross-links, and mechanical checks for hidden conventions. Do not use for a general code-quality review, standalone marketing README rewrite, product documentation, narrow bug fixes, or framework-specific implementation work unless the core issue is missing agent-readable repo context. Output repo-local artifacts or a legibility audit that identifies missing knowledge, added maps/docs/checks, remaining off-repo context, and the next highest-leverage improvement.
---

# Make Repo Agent Legible

## Overview

Make a repository easier for coding agents to navigate, modify, and validate. Treat agent legibility as the goal: if important knowledge is not versioned and discoverable inside the repo, treat it as missing.

## Workflow

1. Read the current repository entry points first:
- `README.md`
- `AGENTS.md`
- top-level architecture and design docs
- docs indexes
- lint/test/CI config
- a representative slice of the code
2. Diagnose the main legibility failures with `references/legibility-rubric.md`. Look for missing maps, hidden conventions, stale docs, weak boundaries, and validation gaps.
3. Treat `README.md` as the repository front door for humans and agents. In most repos it should quickly answer what this is, who it is for, how to install or run the smallest useful loop, where the project fits, and what it does not do. Keep deeper implementation, operations, and agent instructions behind clearly named links instead of forcing first-time readers through repo topology.
4. Make `AGENTS.md` a map, not an encyclopedia. Keep it short, stable, and action-oriented. Point coding agents to deeper sources of truth by task type instead of duplicating the README or docs.
5. Separate README and AGENTS responsibilities:
- `README.md`: public or team-facing front door, quickstart, user/contributor orientation, and a final navigation section for deeper docs.
- `AGENTS.md`: coding-agent operating map, repository-specific constraints, validation commands, ownership boundaries, and task routing.
- `docs/` or equivalent: durable system of record for architecture, design, operations, quality, decisions, and long-lived plans.
6. Move important knowledge into the repo:
- architecture maps
- product, domain, design, or operational docs as appropriate
- execution plans and decision logs
- generated references such as schemas, contracts, or inventories
- reliability, security, and quality expectations
7. Treat `docs/` or another obvious repo-local knowledge area as the system of record for non-trivial repositories. Add indexes and cross-links so the agent can progressively discover depth instead of receiving one giant instruction blob.
8. Encode constraints mechanically wherever possible:
- boundary and dependency rules
- schema validation at the edges
- naming and logging invariants
- file-size or complexity limits
- documentation freshness and cross-link checks
9. Write remediation messages for lint and structural-test failures so another agent run can recover without human translation.
10. Increase runtime legibility when the task depends on behavior rather than static code. Make the relevant system locally runnable or inspectable, expose reproducible scripts, and give agents access to logs, metrics, traces, test harnesses, CLIs, UIs, or other feedback loops as appropriate.
11. Capture human taste once, then promote it into reusable artifacts. Convert repeated review comments and tribal knowledge into docs, helpers, lints, tests, or templates.
12. Plan for entropy. Add recurring doc-gardening, quality scoring, or targeted cleanup work so bad patterns are corrected continuously instead of in occasional cleanup sprints.
13. Report outcomes in terms of leverage:
- what was illegible
- what artifacts or enforcement were added
- what knowledge still lives outside the repo
- which next investment would most improve agent autonomy

## Default Deliverables

- A README that works as a front door: clear purpose, quickstart, project boundaries, links to examples/docs, and a contributor or agent navigation section when appropriate.
- A concise `AGENTS.md` that routes the agent to deeper sources.
- A repo-local knowledge structure with clear indexes.
- Architecture, operational, and planning artifacts for areas that are currently implicit.
- Mechanical checks for the highest-value invariants.
- A prioritized legibility audit with concrete next steps.

## Decision Rules

- Optimize for what a future agent run can discover and trust quickly.
- Prefer progressive disclosure over giant instruction files.
- Keep the README useful to a first-time human while making its deeper links precise enough for agents.
- Do not turn README into AGENTS.md. Put operational agent rules in `AGENTS.md` and make README point there.
- Prefer boring, inspectable abstractions over opaque dependencies at critical boundaries.
- Enforce invariants centrally and allow flexibility inside those boundaries.
- Version plans, decisions, and standards near the code they govern.
- Treat stale documentation as a correctness problem, not a cosmetic one.

## Anti-Patterns

- A README that is only a maintainer map and does not tell a new user what the project is, how to try it, or where the boundaries are.
- A README that tries to hold every implementation detail instead of routing to durable docs.
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

### examples/

- `legibility-audit-output.md`: worked shape for reporting a full audit.
