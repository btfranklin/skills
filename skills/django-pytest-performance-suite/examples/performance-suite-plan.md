# Customer Activity Performance Suite Plan

## Target and risk

Protect the uncached `customer_activity` read model and `GET /customers/<uuid>/activity/` view. Production accounts can contain 50,000 events across 500 projects. The known risks are an N+1 query over event actors, accidental materialization of all events, and output drift in project summaries.

## Database fidelity

The performance settings use the same Django database backend, driver, transaction behavior, and schema options as the deployed application. The lane creates an isolated database through that backend's normal Django test-database lifecycle.

If the deployed database is embedded, each worker receives a disposable local database through the production backend. If it is client-server, CI provisions an isolated service using the production engine family. Managed-network latency is measured separately; this suite protects server-side work and does not claim to reproduce Internet distance.

Every report records the resolved backend, driver, engine version, topology, and relevant options. Replacing the engine with a convenient substitute would require an explicit approximation label and would disqualify its timing results from strict enforcement.

## Lane layout

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

The settings module disables email and outbound integrations, makes reachable background work deterministic, and preserves production-relevant database and timezone options. Tests carry the `performance` marker and remain outside the default pytest configuration.

## Deterministic scenarios

| Case | Projects | Events | Purpose |
|---|---:|---:|---|
| `activity_small` | 5 | 100 | Fast correctness diagnosis |
| `activity_medium` | 100 | 10,000 | Normal regression lane |
| `activity_large` | 500 | 50,000 | Capacity boundary |

Seeders use fixed UUIDs, a fixed UTC clock, and a seeded RNG. Actors are reused in a predictable ratio. The database is seeded once per isolated worker and reused; benchmark rounds do not include database creation or fixture construction.

## Correctness and query guards

Each case first calls the builder outside the benchmark fixture and normalizes:

- customer ID
- project count and ordered project IDs
- event count by type
- first and last event timestamps
- ordered top-20 activity rows

Small and medium cases compare full normalized JSON. The large case compares a reviewable summary plus a SHA-256 hash of the complete normalized payload. Request-level checks also assert status 200 and the expected template.

Initial query caps, confirmed from a clean reference run:

```json
{
  "activity_small": {"builder": 8, "request": 10},
  "activity_medium": {"builder": 8, "request": 10},
  "activity_large": {"builder": 8, "request": 10}
}
```

The constant caps ensure account size cannot reintroduce per-project or per-actor queries. If the backend does not expose a query boundary suitable for Django's capture utility, the lane substitutes a documented operation counter rather than silently dropping the guard.

## Timing budgets

Strict budgets are created only after repeated independent runs on the stable enforcement runner. Each eligible case records its median, mean, dispersion, maximum observed variation, chosen headroom, and runner/database profile. Unstable or topology-dependent cases remain observation-only.

The JSON and Markdown reports distinguish:

- correctness pass/fail
- query or operation cap pass/fail
- timing enforced/observation-only
- database profile matched/approximated

## Commands and CI

```bash
pdm run perf-test
pdm run perf-test-strict
pdm run perf-refresh-correctness
pdm run perf-accept-baseline
```

`perf-test` runs correctness, caps, and non-gating benchmarks locally. `perf-test-strict` enforces only calibrated budgets on the approved runner. CI provisions the database profile defined by the project, runs strict mode repeatedly enough to detect instability, and uploads JSON and Markdown reports.

Correctness refresh is allowed only for an intentional output change. Baseline acceptance requires successful correctness and cap checks plus recorded recalibration evidence. Neither command updates the other artifact.

## Coverage drift

A registry is added only if customer-activity GET surfaces form a bounded product family. It lists each route, builder, scenario IDs, and owner. A structural test then fails when a new route lacks a registry decision, with a message explaining how to register or exempt it.
