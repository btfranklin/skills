# Customer Activity Performance Suite Plan

## Target And Risk

Protect the uncached `customer_activity` read model and `GET /customers/<uuid>/activity/` view. Production accounts can contain 50,000 events across 500 projects. The known risks are an N+1 query over event actors, accidental materialization of all events, and output drift in the project summaries.

## Lane Layout

```text
config/settings/performance.py
tests/performance/
├── conftest.py
├── scenarios.py
├── snapshots/customer_activity_medium.json
├── budgets.json
├── test_customer_activity.py
└── reporting.py
```

`performance.py` requires a PostgreSQL test URL, disables email and outbound integrations, makes task dispatch eager, and uses the same timezone and relevant database options as production. Tests carry the `performance` marker and are excluded from the default pytest configuration.

## Deterministic Scenarios

| Case | Projects | Events | Purpose |
|---|---:|---:|---|
| `activity_small` | 5 | 100 | Fast correctness diagnosis |
| `activity_medium` | 100 | 10,000 | Normal regression lane |
| `activity_large` | 500 | 50,000 | Strict capacity boundary |

Seeders use fixed UUIDs, a fixed UTC clock, and a seeded RNG. Actors are reused in a predictable ratio. The database is seeded once per worker and reused; benchmark rounds do not include fixture construction.

## Correctness And Query Guards

Each case first calls the builder outside the benchmark fixture and normalizes:

- customer ID
- project count and ordered project IDs
- event count by type
- first and last event timestamps
- ordered top-20 activity rows

The small and medium cases compare full normalized JSON. The large case compares the summary plus a SHA-256 hash of the full normalized payload. Request-level checks also assert status 200 and the expected template name.

Initial query caps, confirmed from a clean reference run:

```json
{
  "activity_small": {"builder": 8, "request": 10},
  "activity_medium": {"builder": 8, "request": 10},
  "activity_large": {"builder": 8, "request": 10}
}
```

The constant caps ensure account size cannot reintroduce per-project or per-actor queries.

## Timing Budgets

Strict CI uses the median of benchmark rounds on the dedicated runner:

| Case | Builder target | Request target | Tolerance |
|---|---:|---:|---:|
| Small | 35 ms | 50 ms | 25% |
| Medium | 180 ms | 225 ms | 20% |
| Large | 650 ms | 750 ms | 20% |

These are starting contracts from the recorded reference runner, not universal hardware claims. Each report records runner identity, commit, database version, median, mean, standard deviation, query count, budget, and result.

## Commands And CI

```bash
pdm run perf-test
pdm run perf-test-strict
pdm run perf-refresh-snapshots
pdm run perf-accept-baseline
```

`perf-test` runs correctness, queries, and non-gating benchmarks locally. `perf-test-strict` enforces budgets. The manual CI workflow provisions PostgreSQL, runs strict mode twice, and uploads JSON and Markdown reports.

Snapshot refresh is allowed only when reviewed output intentionally changes. Baseline acceptance requires a successful correctness/query run plus a short reason recorded with the budget change. Neither command updates the other artifact.

## Coverage Drift

A registry lists the customer activity route, builder, scenario IDs, and owners. A structural test fails if a new read-only customer activity route lacks a registry decision, with a message explaining how to register it or document why it is exempt.
