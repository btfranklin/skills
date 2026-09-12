# Deep Codebase Review Example

This fictional example shows report depth and classification. Adapt the format to the reviewed repository. Do not reuse the conclusions.

## Review Method

The review covered the `jobs/` merge-base diff, queue adapter, persistence model, and retry tests. The review excluded deployment configuration and unrelated HTTP endpoints. Three specialists reviewed lifecycle, boundaries, and tests. The lead reviewer verified all three findings.

## Findings

1. `[High] A retry can dispatch the same export twice` — `jobs/export_worker.py:88`

   The worker sends the export before recording the provider receipt. A crash between those operations leaves the row retryable even though the external side effect succeeded. The retry logic calls the provider again because neither an idempotency key nor a durable dispatch state connects those operations.

2. `[Medium] Provider payloads have become the domain model` — `exports/models.py:41`

   `Export.metadata` stores adapter-specific status and destination fields. Core scheduling code reads these fields directly. A new provider now requires provider conditions in the model and scheduler. This requirement conflicts with the adapter boundary in `docs/architecture.md`.

3. `[Low] Forwarding layers repeat signature maintenance` — `exports/service.py:12`

   `exports/service.py`: `ExportService.run` only forwards to `ExportManager.run`, which only calls `write_csv`. Every signature change now crosses both wrappers and their forwarding tests. No caller uses a separate policy or lifecycle at either layer.

   Replace `service.run(records, destination)` with `write_csv(records, destination)` at the workflow boundary. Remove the two forwarding classes and their forwarding-only tests. Preserve output and failure tests. The workflow retains authorization and transaction ownership. This correction removes two maintenance locations without adding a general exporter interface. Retain either layer if further caller inspection reveals an external contract that requires it.

## Structural Future Risks

- `jobs/export_worker.py`: Reservation, dispatch, retry accounting, and cleanup use one module. Except for the crash interval above, current behavior is correct. The next delivery mode will require edits to unrelated lifecycle branches. The delivery-mode requirement is documented in `docs/roadmap.md`. Trace its dispatch edits before implementation. Defer the split until that work starts; current behavior does not require a new framework.

## Roadmap / Design Alignment

- `docs/roadmap.md`: The export layer is not provider neutral because provider metadata enters scheduling. Record the boundary repair only if this document is the authoritative list of future work.

## Open Questions

- Does the provider use a stable idempotency key? If not, the durable state transition needs a reconciliation process instead of simple replay protection.

## Follow-Through

1. Close the dispatch crash window with a durable idempotency contract and retry test.
2. Move provider status translation behind the adapter boundary.
3. Split cleanup only when the next delivery mode is implemented. This is a future risk, not an urgent rewrite.
