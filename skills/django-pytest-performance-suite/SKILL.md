---
name: django-pytest-performance-suite
description: >-
  Build a PostgreSQL-backed Django performance lane with pytest, deterministic data, correctness guards, query caps, budgets, and reports. Use when read models or read-only GET surfaces need regression protection. Do not use for one-off profiling, browser benchmarks, generic tests, production APM, SQLite-only checks, or non-Django services. Produce local and CI workflows with explicit baseline maintenance.
---

# Django Pytest Performance Suite

## Workflow

1. Inspect the existing Django, database, pytest, command, and CI conventions. Identify the production database and the uncached server-side work worth protecting.
2. Inventory target builders/read models and thin request wrappers. Start with high-value read-only GET surfaces.
3. Create a separate performance lane with dedicated settings, marker, commands, and on-demand CI. Do not slow the default unit-test loop.
4. Seed realistic scenarios deterministically: freeze time, fix identifiers and randomness, and block outbound or background side effects.
5. Run correctness before timing. Normalize the result, assert a snapshot or summary hash, then assert query count.
6. Benchmark stable work with `pytest-benchmark`. Cover the internal builder for diagnosis and the request wrapper for user-facing protection when both matter.
7. Store query caps and timing budgets by case. Generate machine-readable JSON and human-readable Markdown reports.
8. Keep snapshot refresh and timing-baseline acceptance as separate, explicit maintenance actions.
9. Register covered GET surfaces and add a structural check when unregistered surfaces would create meaningful drift.

Use the repository's package manager and task runner. Preserve existing test conventions unless they prevent an isolated, reproducible lane.

## Decisions

- Benchmark against PostgreSQL because this skill's contract is PostgreSQL-backed behavior; do not treat SQLite timings as representative.
- Prefer `RequestFactory` unless middleware or full request handling is part of the measured contract.
- Use full normalized snapshots for reviewable results and compact summaries plus hashes for very large payloads.
- Treat query caps as deterministic early warnings and timing budgets as environment-sensitive guardrails.
- Never update budgets automatically after a failure.

## Validation

Run the untimed correctness and query checks before the timing lane. Run strict mode twice on the intended runner to expose unstable data or excessive timing noise. Verify that normal tests exclude the performance marker, reports identify each case and budget, and maintenance commands cannot conflate output changes with performance changes.

## Resources

- Read [references/patterns.md](references/patterns.md) when implementing seed stability, snapshots, budgets, reporting, or surface registration.
- Read [examples/performance-suite-plan.md](examples/performance-suite-plan.md) when preparing a concrete suite plan or handoff.
