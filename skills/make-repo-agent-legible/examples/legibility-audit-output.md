# Agent-Legibility Audit: Parcelhook

## Repository Context

Parcelhook is a small Python service that receives carrier webhooks and publishes normalized shipment events. The repository contains one application package, 28 tests, a Dockerfile, and one deployment workflow. This scale needs a concise entry document and operations guide. It does not need a broad document hierarchy.

## Strengths

- `pyproject.toml` exposes `test`, `lint`, and `serve` scripts through PDM.
- `parcelhook/webhooks.py` is a clear boundary between provider payloads and the internal `ShipmentEvent` model.
- CI runs lint and tests on every pull request.
- Provider fixtures make webhook behavior reproducible without network access.

## Findings

### High: The startup procedure is not discoverable

`README.md` describes the product but does not contain install, local-run, fixture-replay, or test commands. A new agent must infer PDM scripts, required environment variables, and the development webhook endpoint from configuration and tests.

**Recommended change:** Add a compact Quickstart that uses the existing PDM commands. List required and optional environment variables. Link to the fixture-replay command. Verify each command in a clean environment before publication.

### High: Only the workflow YAML identifies deployment ownership

The production service name, health endpoint, rollback command, and secret ownership appear only in `.github/workflows/deploy.yml`. There is no operations document for people. The rollback step depends on information that is not in the repository.

**Recommended change:** Add `docs/operations.md`. Document the deployment trigger, health verification, rollback command, and owner of each external secret. Mark the unknown secret-rotation process as `needs owner`. Do not infer it.

### Medium: Provider registration has an unenforced three-file convention

Adding a carrier requires a parser, registry entry, and fixture directory. Existing tests cover registered carriers. No check detects an unregistered parser or a carrier without fixtures.

**Recommended change:** Document the extension process in `AGENTS.md`. Add one structural test that compares parser modules, registry keys, and fixture directories. Its failure must name the missing element and the command to run again.

### Low: Architecture is implicit but small

The package has three clear layers: transport, normalization, and publishing. It does not have an architecture document. A separate architecture document is not necessary for this repository.

**Recommended change:** Add a section of six to eight lines to the README. Name it `How it fits together`. Link to the three entry modules.

## Proportionate Artifact Set

```text
README.md              # purpose, quickstart, boundaries, architecture summary
AGENTS.md              # short task guide and validation commands
docs/operations.md     # deploy, health, rollback, external ownership
```

A decision-log tree, generated-documents area, and separate architecture file are not necessary now.

## Knowledge Outside the Repository

- Secret rotation procedure: unknown; needs an operational owner.
- Carrier sandbox credentials: managed externally. The repository must identify the owner and setup link. It must not store the credentials.
- Production alert thresholds: visible only in the monitoring service; capture their intent and ownership in `docs/operations.md`.

## Priority Order

1. Make the existing local loop runnable from the README.
2. Capture deployment and rollback operations, preserving unknown ownership explicitly.
3. Add the provider-registration structural check and recovery message.

These changes prevent the most costly repeated searches. They keep the document set suitable for a small service.
