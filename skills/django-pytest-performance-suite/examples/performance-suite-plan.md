# Performance Suite Plan Example

Use this shape when the user needs a full Django performance lane rather than a one-off timing run.

## Target Surfaces

- `Surface`: view/read model/builder, expected scale, uncached path, and user-facing risk.

## Suite Layout

- `settings`: dedicated PostgreSQL-backed performance settings module.
- `tests/performance/`: scenario seeders, result normalizers, query helpers, benchmarks, and reports.
- `budgets`: checked-in timing and query caps per scenario.

## Correctness Before Timing

- Normalize output to stable JSON or summary hashes.
- Assert snapshots/hashes before running timed benchmarks.
- Assert query caps separately from elapsed time.

## Commands

```bash
pdm run perf-test
pdm run perf-test-strict
pdm run perf-refresh-snapshots
pdm run perf-accept-baseline
```

## CI / Reporting

- Manual workflow for strict runs.
- Upload machine-readable and human-readable reports.
- Document when snapshots and baselines may be refreshed.
