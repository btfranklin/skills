# Django Performance Suite Patterns

Use this file when implementing or extending a Django performance regression lane and you need the detailed patterns, not just the top-level workflow.

## Separate Lane Pattern

Create a dedicated lane instead of extending the default unit-test path.

- Use a dedicated settings module.
- Require PostgreSQL.
- Keep commands separate from normal test commands.
- Prefer manual or on-demand CI, not every-PR by default, unless the suite is already cheap and stable.

Why:

- heavy seeded datasets slow normal feedback loops
- PostgreSQL-backed tests usually need different setup than unit tests
- budgets and snapshots require deliberate maintenance

## Deterministic Runtime Pattern

Keep the performance lane as deterministic as possible.

- Fix timestamps and time zones.
- Fix UUIDs, slugs, and seeded random values.
- Reuse a seeded database when possible.
- Force Celery eager mode if task dispatch can be reached.
- Monkeypatch or block outbound sync, webhook enqueue, or background maintenance triggers.

Goal:

- each run measures the same server-side work
- correctness artifacts stay stable
- timing noise is reduced enough to make budgets meaningful

## Surface Coverage Pattern

Cover both of these:

1. heavy builders or read models
2. thin request-level wrappers for the real GET surfaces

Builder benchmarks help answer where the time is actually spent. Request-level benchmarks protect the real surface that users hit.

For Django pages, maintain a registry of read-only GET views and add a structural test that fails when a new GET surface is unregistered.

## Correctness-Then-Timing Pattern

Use this order:

1. build the result once
2. normalize it into stable JSON
3. compare against a checked-in artifact
4. capture and assert query counts
5. run the timed benchmark

This prevents meaningless timing passes on a broken or drifting result.

## Snapshot Pattern

Normalize aggressively before snapshotting.

Good snapshot fields:

- counts
- slugs
- labels
- stable IDs
- stable lists or summaries
- small semantic booleans for responses

Avoid snapshotting:

- timestamps that change per run
- unordered structures
- raw HTML when only structure matters
- giant payloads that no one will review

For small or medium scenarios, store full normalized snapshots.

For very large scenarios, store:

- a compact summary
- a SHA-256 of the full normalized payload

This keeps completeness checks without exploding repository size.

## Budget Pattern

Keep one checked-in budget table keyed by case ID.

Each case should usually include:

- `target_ms`
- `tolerance_pct`
- `max_queries`

Treat this as the contract for strict mode.

Use two maintenance actions, not one:

- refresh snapshots for intentional output drift
- accept baseline for intentional timing changes

Do not blur those steps together.

## Reporting Pattern

Always generate artifacts after a timing run.

Useful outputs:

- JSON for automation or later analysis
- Markdown for humans scanning regressions

The report should show:

- case name
- median and mean
- current budget
- max allowed time
- query cap
- pass or fail

## Common Tool Choices

Typical stack:

- `pytest`
- `pytest-django`
- `pytest-benchmark`
- Django `RequestFactory`
- Django query capture utilities

Helpful options:

- `--reuse-db` for expensive seeded lanes
- a dedicated marker such as `performance`
- a dedicated settings module via `--ds=...`

## Common Failure Modes

- Using SQLite and thinking the timings represent production behavior.
- Mixing perf tests into default CI and then disabling them because they are too slow.
- Measuring only full requests and having no idea where the cost actually is.
- Measuring only internal builders and forgetting to protect the real surface.
- Letting snapshots churn because unstable fields were not normalized away.
- Updating budgets casually whenever strict mode fails.
- Missing newly added views because there is no surface registry.

## Implementation Checklist

- Add a dedicated performance settings module.
- Add a `performance` pytest marker.
- Add separate local commands.
- Seed deterministic scenarios.
- Add builder benchmarks for heavy shaping code.
- Add request-level benchmarks for real GET surfaces.
- Normalize results before snapshotting.
- Assert query caps.
- Store checked-in timing budgets.
- Write JSON and Markdown reports.
- Add a manual CI workflow.
- Document the maintenance workflow.
