# Customer Activity Performance Suite Plan

## Target and risk

Protect the uncached `customer_activity` read model and `GET /customers/<uuid>/activity/` view. Production accounts can contain 50,000 events across 500 projects. Known risks include an N+1 query over event actors and accidental loading of all events. Project summaries can also produce incorrect output after a change.

## Database fidelity

The performance settings use the same Django database backend, driver, transaction behavior, and schema options as the deployed application. The performance test group creates an isolated database through the normal Django test-database process for that backend.

If the deployed database is embedded, the test setup gives each worker a disposable local database through the production backend. If the database uses a client-server design, CI creates an isolated service that uses the production engine family. Measure managed-network latency separately. This suite protects server-side work and does not claim to reproduce Internet distance.

Every report records the resolved backend, driver, engine version, topology, and applicable options. If a test uses a substitute engine, label the test as an approximation. Do not enforce time limits from that test.

## File layout

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

The settings module disables email and outbound integrations. It makes reachable background work deterministic. It preserves the applicable production database and time-zone options. Tests use the `performance` marker and remain outside the default pytest configuration.

## Deterministic scenarios

| Case | Projects | Events | Purpose |
|---|---:|---:|---|
| `activity_small` | 5 | 100 | Fast correctness diagnosis |
| `activity_medium` | 100 | 10,000 | Normal regression case |
| `activity_large` | 500 | 50,000 | Capacity boundary |

Seeders use fixed UUIDs, a fixed UTC clock, and a seeded random number generator. Seeders reuse actors in a predictable ratio. The setup code seeds the database once for each isolated worker and then reuses it. Benchmark rounds do not include database creation or fixture construction.

## Correctness and query checks

Each case calls the builder outside the benchmark fixture first. It normalizes these values:

- customer ID
- project count and ordered project IDs
- event count by type
- first and last event timestamps
- ordered top-20 activity rows

The small and medium cases compare full normalized JSON. The large case compares a reviewable summary and a SHA-256 hash of the complete normalized payload. Request-level checks also require status 200 and the expected template.

The clean reference run confirmed these initial query limits:

```json
{
  "activity_small": {"builder": 8, "request": 10},
  "activity_medium": {"builder": 8, "request": 10},
  "activity_large": {"builder": 8, "request": 10}
}
```

The constant limits prevent account size from adding per-project or per-actor queries. If Django's capture utility cannot observe the applicable query boundary, use a documented operation counter. Do not remove the check without a report.

## Time limits

Create strict time limits only after repeated independent runs on the stable enforcement runner. Each eligible case records its median, mean, dispersion, maximum observed variation, selected tolerance, and runner and database profile. Record results for unstable or topology-dependent cases without enforcement.

The JSON and Markdown reports identify these results separately:

- correctness pass/fail
- query or operation limit pass/fail
- timing enforced/observation-only
- database profile matched/approximated

## Commands and CI

```bash
pdm run perf-test
pdm run perf-test-strict
pdm run perf-refresh-correctness
pdm run perf-accept-baseline
```

`perf-test` runs correctness checks, limits, and non-enforced benchmarks locally. `perf-test-strict` enforces only calibrated time limits on the approved runner. CI creates the database profile that the project defines. It runs strict mode enough times to detect instability. It uploads JSON and Markdown reports.

Update the correctness reference only for an intentional output change. Baseline acceptance requires successful correctness and limit checks. It also requires recorded recalibration evidence. Neither command updates the other file.

## Missing coverage

Add a registry only if customer-activity GET interfaces form a limited product family. The registry lists each route, builder, scenario ID, and owner. A structural test fails when a new route does not have a registry decision. Its message explains how to register or exempt the route.
