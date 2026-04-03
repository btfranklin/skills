---
name: django-pytest-performance-suite
description: Design and implement Postgres-backed Django performance regression suites using pytest, pytest-django, RequestFactory, and pytest-benchmark. Use when Codex needs to benchmark or guard Django view, read-model, or request-surface performance; create a separate performance test lane; seed deterministic large datasets; enforce timing or query budgets; generate benchmark reports; or keep new read-only GET surfaces covered by structural tests.
---

# Django Pytest Performance Suite

## Overview

Build trustworthy Django performance regression coverage for server-side surfaces. Prefer this skill when the goal is not a one-off benchmark, but a repeatable lane that can detect correctness drift, query regressions, and timing regressions over time.

## Workflow

1. Identify the performance surface.
   - Separate pure builders/read models from thin request/view wrappers.
   - Prefer benchmarking uncached server-side work first.
   - For Django UI work, cover read-only GET surfaces before thinking about browser rendering.
2. Create a separate performance lane.
   - Keep it out of the default unit-test path.
   - Use a dedicated settings module.
   - Require PostgreSQL instead of SQLite.
   - Use explicit commands such as `perf-test`, `perf-test-strict`, `perf-refresh-snapshots`, and `perf-accept-baseline`.
3. Make the run deterministic.
   - Seed fixed timestamps, UUIDs, slugs, and RNG.
   - Block background dispatch and outbound integration behavior.
   - Keep Celery eager if task code may be touched indirectly.
   - Use reusable databases when setup cost is large.
4. Validate correctness before timing.
   - Run an untimed pass first.
   - Normalize the result into stable JSON.
   - Compare it to a checked-in known-good artifact.
   - Count queries and assert a cap.
   - Only then run the benchmark timing pass.
5. Record and enforce budgets.
   - Keep checked-in timing budgets per surface and scenario.
   - Keep checked-in query caps per surface and scenario.
   - Generate machine-readable and human-readable reports for each run.
6. Protect coverage from drifting.
   - Keep a registry of read-only GET surfaces.
   - Add a structural test that fails when a new GET surface is unregistered.

## Design Rules

- Measure against PostgreSQL. SQLite timings are not useful for Django performance guardrails.
- Treat timing and correctness as separate concerns. A fast wrong result is still a regression.
- Pair query caps with timing budgets. Query counts are often the clearest early-warning signal.
- Benchmark both layers when possible:
  - builder/read-model cost for diagnosis
  - request/view wrapper cost for user-facing surfaces
- Prefer RequestFactory for request-surface measurements unless middleware behavior is the thing being tested.
- Keep large datasets realistic enough to trigger ORM and template-shaping costs that small fixtures hide.
- Store large-case correctness as summaries plus a payload hash instead of enormous snapshots.
- Keep baseline changes explicit. Refresh snapshots only for intentional output changes. Accept timing baselines only for intentional steady-state changes.

## Implementation Pattern

When building the suite, create these pieces:

- A dedicated Django settings module for performance runs.
- A `tests/performance/` package.
- Deterministic scenario seeders.
- Result normalizers that remove unstable fields.
- Snapshot assertions for correctness.
- Query-count capture helpers.
- A checked-in budget table.
- A report writer for latest results.
- A manual CI workflow that runs the strict lane and uploads artifacts.

For a detailed implementation checklist and the non-obvious stability techniques, read [references/patterns.md](references/patterns.md).

## What To Avoid

- Do not mix performance tests into the default `pdm run test` or `pytest` path when they require heavy setup.
- Do not benchmark only tiny fixtures and assume the result generalizes.
- Do not rely on timing alone when large ORM regressions can be caught deterministically with query caps.
- Do not keep snapshots of raw HTML or full contexts if they include unstable values that will churn constantly.
- Do not silently update budgets after every run. That destroys the regression signal.
- Do not let new GET surfaces appear without performance-suite registration.

## Output Expectations

When the user asks for this kind of work, produce:

- the separate pytest lane
- deterministic scenarios sized to the product surface
- snapshot and query-count guards
- timing budgets and artifact reports
- run commands for local and CI usage
- documentation for refresh and baseline-accept workflows

If the repository already has ad hoc benchmarks, prefer folding them into the same lane rather than leaving multiple incompatible performance workflows in place.
