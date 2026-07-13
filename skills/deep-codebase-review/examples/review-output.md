# Deep Codebase Review Example

This fictional example demonstrates report depth and classification. Adapt it to the reviewed repository; do not reuse its conclusions.

## Review Method

Reviewed the `jobs/` merge-base diff plus the queue adapter, persistence model, and retry tests. Deployment configuration and unrelated HTTP endpoints were out of scope. Three specialists covered lifecycle, boundaries, and tests; the lead reviewer verified both reported findings.

## Findings

1. `[High] A retry can dispatch the same export twice` — `jobs/export_worker.py:88`

   The worker sends the export before recording the provider receipt. A crash between those operations leaves the row retryable even though the external side effect succeeded. The retry path calls the provider again because neither an idempotency key nor a durable dispatch state bridges that window.

2. `[Medium] Provider payloads have become the domain model` — `exports/models.py:41`

   `Export.metadata` stores adapter-specific status and destination fields that core scheduling code reads directly. Adding another provider now requires provider conditionals in both the model and scheduler, contradicting the documented adapter boundary in `docs/architecture.md`.

## Structural Pressure Points

- `jobs/export_worker.py`: reservation, dispatch, retry accounting, and cleanup now share one module. No behavior is currently incorrect beyond the crash window above, but the next delivery mode will require editing unrelated lifecycle branches. Extract the dispatch state transition before adding it.

## Roadmap / Design Alignment

- `docs/roadmap.md`: the claimed provider-neutral export layer is not yet true because provider metadata crosses into scheduling. Record the boundary repair only if this document remains the project's authoritative future-work list.

## Open Questions

- Does the provider honor a stable idempotency key? If not, the durable state transition needs a reconciliation path rather than simple replay protection.

## Follow-Through

1. Close the dispatch crash window with a durable idempotency contract and retry test.
2. Move provider status translation behind the adapter boundary.
3. Split cleanup only when the next delivery mode lands; it is a pressure point, not an urgent rewrite.
