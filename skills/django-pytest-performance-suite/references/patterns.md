# Django Performance Suite Patterns

Use these patterns after identifying the target workloads and production database contract.

## Preserve database fidelity

Record the applicable production database profile before you design the performance tests:

- Django backend and database driver
- engine and extension versions
- embedded, in-memory, local service, remote service, replica, or managed topology
- transaction behavior and isolation behavior
- connection, pooling, journal, cache, and durability options that affect the workload
- schema, indexes, constraints, and representative data distribution

The test target must preserve the behaviors that the benchmark claims to protect. Run an embedded database through the real backend and driver. Use a disposable local database unless the production contract requires a different mode. Use an isolated service for a client-server database. Do not use a substitute engine. If CI cannot reproduce a managed or remote topology, keep deterministic correctness and query checks in CI. Calibrate time limits on a stable representative runner. Label local time measurements as an approximation.

Do not include database creation or migrations in a timing round. Do not include network setup or fixture seeding. Include these operations only when lifecycle or setup cost is the named workload.

## Seed once, measure separately

Build expensive scenario data outside benchmark rounds. Use fixed timestamps, identifiers, slugs, and random number generator seeds. Reuse a seeded test database only when tests preserve isolation. Disable outbound calls and maintenance triggers. Make reachable task execution deterministic.

Give each scenario a stable case ID. Document the product scale that it represents. Include enough rows, relationships, indexes, and value distributions to expose behavior that ordinary fixtures do not expose.

## Choose the measured layer

- Benchmark builders, read models, or ORM services to localize application regressions.
- Add request-level cases when routing, serialization, templates, or middleware contribute meaningful work.
- Benchmark schema, transaction, connection, or backend operations directly when the product exposes those operations.
- Prefer `RequestFactory` only for request cases whose contract excludes middleware.

Use a registry only for a limited family of routes or workloads that requires complete coverage. Store the target, scenario IDs, owner, and each explicit exemption reason. Make structural-test failures explain how to register or exempt an interface.

## Normalize correctness

Remove unstable values and impose deterministic ordering before comparison. Good artifacts include stable identifiers, counts, labels, ordered summaries, schema state, transaction outcomes, and semantic response flags. Avoid raw HTML when a smaller representation protects the behavior.

Store full normalized JSON when a person can review it. For very large results, store a compact summary and a SHA-256 hash of the complete normalized payload.

## Capture queries or operations

Measure queries outside timing rounds so instrumentation does not distort results. Use Django query-capture utilities when they observe the relevant layer. Define an explicit operation counter when query capture cannot represent the work accurately. Document the boundary for driver, connection, migration, or lifecycle work.

Enforce a limit for each case. Prefer limits that must remain constant as the scenario size grows. These limits identify N+1 queries and repeated operations more reliably than elapsed time.

## Set timing contracts

Key time limits by stable case ID. Record the target time, tolerance, runner, operating system, Python, Django, database backend and driver, engine version, and topology. Calibrate the limit with multiple independent clean processes in the environment that will enforce it.

Use the median as the primary comparison. Report the mean and dispersion for diagnosis. Enforce time limits only for workloads with low variation between runs. The variation must be low enough to distinguish a product regression from environmental changes. Record unstable cases without enforcement. Do not increase tolerances until every run passes.

## Report and maintain

Write JSON for automation and Markdown for review. Include the commit, case, scenario scale, database profile, runner, and sample count. Include the median, mean, dispersion, measured query or operation count, allowed limits, correctness status, and timing status.

Keep two deliberate operations:

- **Update correctness reference:** Accept an intentional output-contract change after you review the normalized result.
- **Accept time baseline:** Accept an intentional stable performance change after correctness and query or operation checks pass. Recalibrate the time limit first.

Neither operation must modify the files of the other operation. Never accept a failing result automatically.
