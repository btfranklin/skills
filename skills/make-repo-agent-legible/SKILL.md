---
name: make-repo-agent-legible
description: >-
  Audit or refactor a repository so coding agents can discover its purpose, architecture, constraints, workflows, validation, and sources of truth. Use when essential knowledge is hidden, stale, or unenforced. Do not use for general code review, marketing-only README work, product docs, or narrow implementation. Produce a prioritized audit or proportionate repo-local maps, docs, links, and checks.
---

# Make Repo Agent Legible

## Workflow

1. Establish repository scale and type. Preserve effective documentation conventions; do not impose a large-repository document tree on a small package.
2. Read the entry points, instructions, docs indexes, build/test/CI configuration, and a representative code slice.
3. Audit navigation, source-of-truth ownership, architecture, enforcement, task memory, runtime inspection, and entropy control with the rubric.
4. Separate roles:
   - `README.md`: purpose, audience, smallest useful loop, boundaries, and deeper navigation.
   - `AGENTS.md`: short coding-agent map, repository constraints, validation commands, and task routing.
   - deeper repo-local docs: durable architecture, operations, quality, decisions, and plans only where the repository needs them.
5. Prioritize the smallest artifact or check that removes the most repeated rediscovery. Link to the authoritative source instead of duplicating it.
6. Move important off-repo knowledge into versioned artifacts only when verified. Mark inaccessible or uncertain knowledge as unknown; never reconstruct it from guesswork.
7. Encode repeated, high-value constraints mechanically where practical. Make failure messages explain how to recover.
8. Validate links, commands, ownership boundaries, and relevant runtime paths. Report what remains off-repo or unenforced.

For an audit-only request, inspect and report without editing. For implementation, keep changes proportional to the repository and preserve unrelated documentation.

## Decisions

- Prefer a short map over a comprehensive instruction blob.
- Add architecture, operations, decision, or plan artifacts only when the repository's scale and work patterns justify maintaining them.
- Keep one authoritative home for each fact; use indexes and cross-links for discovery.
- Promote recurring rules from prose to helpers, structural tests, linters, or CI only when the enforcement cost is justified.
- Treat runnable commands, deterministic reproductions, logs, and inspectable state as part of legibility when static docs are insufficient.

## Resources

- Read [references/legibility-rubric.md](references/legibility-rubric.md) when auditing and prioritizing gaps.
- Read [references/artifact-patterns.md](references/artifact-patterns.md) only when selecting or implementing repo-local artifacts and enforcement.
- Read [examples/legibility-audit-output.md](examples/legibility-audit-output.md) when preparing a concrete audit report.
