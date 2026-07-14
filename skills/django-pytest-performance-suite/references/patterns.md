# Django Performance Suite Patterns

Use these details while implementing a lane after following the core workflow in `SKILL.md`.

## Seed Once, Measure Separately

Build expensive scenario data outside benchmark rounds. Use fixed timestamps, UUIDs, slugs, and RNG seeds. Reuse the seeded test database where the repository can do so safely. Disable outbound calls and maintenance triggers; make reachable task execution deterministic.

Give each scenario a stable case ID and document the product scale it represents. Include enough rows and relationships to expose ORM behavior hidden by ordinary fixtures.

## Protect Builders And Requests

Benchmark heavy builders or read models to localize regressions. Add a request-level case for the real GET surface when URL resolution, serialization, templates, or middleware contribute meaningful work. Prefer `RequestFactory` when middleware is outside the contract.

A surface registry is worthwhile when a bounded family of GET routes should not escape coverage. Store route, builder, scenario IDs, and an explicit exemption reason where relevant. Make the structural test's failure explain how to register or exempt a surface.

## Normalize Correctness

Remove unstable values and impose deterministic ordering before comparison. Good artifacts include stable identifiers, counts, labels, ordered summaries, and semantic response flags. Avoid raw HTML when a smaller semantic representation protects the behavior.

Store full normalized JSON when humans can review it. For very large results, store a compact summary and a SHA-256 hash of the complete normalized payload.

## Capture Queries

Measure queries outside timing rounds so instrumentation does not distort the benchmark. Use Django query-capture utilities and assert a case-specific maximum. Prefer caps that should remain constant as scenario size grows; they expose N+1 behavior more clearly than elapsed time.

## Set Timing Contracts

Key budgets by stable case ID and include target time, tolerance, and runner context. Calibrate them from repeated clean runs on the intended environment. Do not present one machine's numbers as universal performance requirements.

Use median as the primary comparison and report mean and dispersion for diagnosis. If repeated strict runs are unstable, fix the workload or runner before widening tolerances.

## Report And Maintain

Write JSON for automation and Markdown for review. Include commit, case, runner, database version, sample count, median, mean, dispersion, measured queries, allowed limits, and pass/fail status.

Keep two deliberate operations:

- **Refresh snapshots:** accept an intentional output-contract change after review.
- **Accept baseline:** accept an intentional performance-contract change after correctness and query checks pass.

Neither operation should modify the other's artifacts. Never auto-accept a failing result.
