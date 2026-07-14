# Django Performance Suite Patterns

Use these patterns after identifying the target workloads and production database contract.

## Preserve database fidelity

Record the production-relevant database profile before designing the lane:

- Django backend and database driver
- engine and extension versions
- embedded, in-memory, local service, remote service, replica, or managed topology
- transaction and isolation behavior
- connection, pooling, journal, cache, and durability options that affect the workload
- schema, indexes, constraints, and representative data distribution

The test target should preserve the behaviors the benchmark claims to protect. An embedded database should normally run through the real backend and driver against a disposable local database. A client-server database should use an isolated service rather than a substitute engine. If CI cannot reproduce a managed or remote topology, keep deterministic correctness and query checks there, calibrate timing on a stable representative runner, and label local timing as an approximation.

Do not include database creation, migrations, network setup, or fixture seeding in a timing round unless lifecycle or setup cost is the named workload.

## Seed once, measure separately

Build expensive scenario data outside benchmark rounds. Use fixed timestamps, identifiers, slugs, and RNG seeds. Reuse a seeded test database only when isolation remains trustworthy. Disable outbound calls and maintenance triggers; make reachable task execution deterministic.

Give each scenario a stable case ID and document the product scale it represents. Include enough rows, relationships, indexes, and value distributions to expose behavior hidden by ordinary fixtures.

## Choose the measured layer

- Benchmark builders, read models, or ORM services to localize application regressions.
- Add request-level cases when routing, serialization, templates, or middleware contribute meaningful work.
- Benchmark schema, transaction, connection, or backend operations directly when those are the product surface.
- Prefer `RequestFactory` only for request cases whose contract excludes middleware.

A registry is worthwhile only when a bounded family of routes or workloads should not escape coverage. Store the target, scenario IDs, owner, and any explicit exemption reason. Make structural-test failures explain how to register or exempt a surface.

## Normalize correctness

Remove unstable values and impose deterministic ordering before comparison. Good artifacts include stable identifiers, counts, labels, ordered summaries, schema state, transaction outcomes, and semantic response flags. Avoid raw HTML when a smaller representation protects the behavior.

Store full normalized JSON when humans can review it. For very large results, store a compact summary and a SHA-256 hash of the complete normalized payload.

## Capture queries or operations

Measure queries outside timing rounds so instrumentation does not distort results. Use Django query-capture utilities when they observe the relevant layer. For driver, connection, migration, or lifecycle work that query capture cannot represent faithfully, define an explicit operation counter with a documented boundary.

Assert case-specific caps. Prefer caps that should remain constant as scenario size grows; they expose N+1 and repeated-operation behavior more deterministically than elapsed time.

## Set timing contracts

Key budgets by stable case ID and record target time, tolerance, runner, operating system, Python, Django, database backend/driver, engine version, and topology. Calibrate from multiple independent clean processes on the environment that will enforce the budget.

Use median as the primary comparison and report mean and dispersion for diagnosis. Gate only workloads whose cross-run variance is low enough to distinguish a product regression from environmental noise. Leave unstable cases observation-only instead of widening tolerances until every run passes.

## Report and maintain

Write JSON for automation and Markdown for review. Include commit, case, scenario scale, database profile, runner, sample count, median, mean, dispersion, measured query/operation count, allowed limits, correctness status, and timing status.

Keep two deliberate operations:

- **Refresh correctness:** accept an intentional output-contract change after reviewing the normalized result.
- **Accept timing baseline:** accept an intentional steady-state performance change after correctness and query/operation checks pass and timing is recalibrated.

Neither operation should modify the other's artifacts. Never auto-accept a failing result.
