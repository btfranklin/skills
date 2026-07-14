# Agent-Legibility Audit: Parcelhook

## Repository Context

Parcelhook is a small Python service that receives carrier webhooks and publishes normalized shipment events. The repository contains one application package, 28 tests, a Dockerfile, and a single deployment workflow. This scale calls for a concise front door and operating map, not a broad documentation hierarchy.

## Strengths

- `pyproject.toml` exposes `test`, `lint`, and `serve` scripts through PDM.
- `parcelhook/webhooks.py` is a clear boundary between provider payloads and the internal `ShipmentEvent` model.
- CI runs lint and tests on every pull request.
- Provider fixtures make webhook behavior reproducible without network access.

## Findings

### High: The runnable path is not discoverable

`README.md` describes the product but has no install, local-run, fixture-replay, or test commands. A new agent must reverse-engineer PDM scripts, required environment variables, and the development webhook endpoint from configuration and tests.

**Recommended change:** add a compact Quickstart using the existing PDM commands, list required versus optional environment variables, and link to the fixture-replay command. Verify every command in a clean environment before publishing it.

### High: Deployment ownership is hidden in workflow YAML

The production service name, health endpoint, rollback command, and secret ownership appear only in `.github/workflows/deploy.yml`. There is no human-readable operating note, and the rollback step depends on knowledge not represented in the repository.

**Recommended change:** add `docs/operations.md` covering deploy trigger, health verification, rollback command, and the owner of each external secret. Mark the currently unknown secret-rotation process as `needs owner` rather than guessing it.

### Medium: Provider registration has an unenforced three-file convention

Adding a carrier requires a parser, registry entry, and fixture directory. Existing tests cover registered carriers, but no check detects an unregistered parser or a carrier without fixtures.

**Recommended change:** document the extension path in `AGENTS.md` and add one structural test comparing parser modules, registry keys, and fixture directories. Its failure should name the missing element and the command to rerun.

### Low: Architecture is implicit but small

The package has three understandable layers—transport, normalization, and publishing—but no map. A standalone architecture document would be excessive for this repository.

**Recommended change:** add a six-to-eight-line “How it fits together” section to the README with links to the three entry modules.

## Proportionate Artifact Set

```text
README.md              # purpose, quickstart, boundaries, architecture summary
AGENTS.md              # short task map and validation commands
docs/operations.md     # deploy, health, rollback, external ownership
```

No decision-log tree, generated-docs area, or separate architecture file is warranted yet.

## Remaining Off-Repo Knowledge

- Secret rotation procedure: unknown; needs an operational owner.
- Carrier sandbox credentials: externally managed; the repository should identify the owner and setup link without storing credentials.
- Production alert thresholds: visible only in the monitoring service; capture their intent and ownership in `docs/operations.md`.

## Priority Order

1. Make the existing local loop runnable from the README.
2. Capture deployment and rollback operations, preserving unknown ownership explicitly.
3. Add the provider-registration structural check and recovery message.

These changes remove the highest-cost rediscovery while keeping the documentation surface appropriate for a small service.
