---
name: django-pytest-performance-suite
description: >-
  Use when building Django performance regression coverage with pytest-benchmark for ORM, views, schema, transactions, or backend behavior. Match the project's production database engine and topology; never prescribe one. Excludes one-off profiling, browser rendering, APM, and non-Django services. Return deterministic scenarios, correctness and query/operation guards, calibrated budgets, reports, and baseline maintenance.
---

# Django Pytest Performance Suite

## Workflow

1. Inspect the existing Django, database, pytest, command, and CI conventions. Record the production backend, driver, engine version, topology, relevant options, and workload scale.
2. Choose high-value uncached work: ORM queries, builders/read models, request wrappers, serializers, admin paths, migrations, schema operations, transactions, or database-backend behavior.
3. Define the database-fidelity contract before implementing tests. Reproduce the production-relevant engine and access mode; document any deliberate approximation and forbid production latency claims from it.
4. Create a separate performance lane with dedicated settings, marker, commands, and on-demand CI. Keep it out of the default unit-test loop.
5. Seed realistic scenarios deterministically. Fix time, identifiers, randomness, ordering, and external side effects; build expensive data outside benchmark rounds.
6. Run correctness before timing. Normalize results, compare a snapshot or summary hash, then enforce a query or operation cap appropriate to the measured layer.
7. Benchmark stable work with `pytest-benchmark`. Exclude setup and instrumentation unless their cost is the explicit subject of the case.
8. Calibrate timing budgets from repeated clean runs on the intended stable runner. Report machine-readable and human-readable results with environment and database context.
9. Keep correctness refresh and timing-baseline acceptance as separate, explicit maintenance actions. Add a coverage registry only for a bounded family of surfaces where drift is a real risk.

Use the repository's package manager and task runner. Preserve existing test conventions unless they prevent an isolated, reproducible lane.

## Decisions

- Never choose PostgreSQL, Turso, SQLite, or another database merely because the skill prefers it. Follow the target project's production contract.
- For embedded production databases, benchmark through the real Django backend and driver against an isolated local file or memory mode only when that mode matches the contract.
- For client-server or remote databases, preserve the relevant protocol and topology. Measure managed-network latency separately when CI cannot reproduce it faithfully.
- Prefer `RequestFactory` only when a request surface is under test and middleware is outside the measured contract.
- Use full normalized snapshots for reviewable results and summaries plus hashes for very large payloads.
- Treat query or operation caps as deterministic early warnings and timing budgets as runner-specific guardrails.
- Never update snapshots or budgets automatically after a failure.

## Freshness

Verify current Django, pytest, pytest-benchmark, database-backend, and driver behavior from the target repository and primary documentation when it affects instrumentation or configuration. Record the checked versions in reports; do not freeze a package or database version in this skill.

## Validation

Run untimed correctness and query/operation checks before timing. Repeat strict runs on the intended runner to quantify variance before enforcing a budget. Verify that ordinary tests exclude the performance marker, reports identify every case and environment, and maintenance commands cannot conflate semantic changes with performance changes.

## Resources

- Read [references/patterns.md](references/patterns.md) when implementing database fidelity, deterministic data, snapshots, caps, budgets, reporting, or optional coverage registration.
- Read [examples/performance-suite-plan.md](examples/performance-suite-plan.md) when preparing a concrete suite plan or handoff.
