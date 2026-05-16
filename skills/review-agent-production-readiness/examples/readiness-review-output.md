# Agent Production-Readiness Review Output Example

Use this shape for full reviews. Keep findings concrete and tied to artifacts.

## Launch Blockers

1. `[Severity] Short blocker` - `artifact/path:line` or named design artifact.
   Explain the unsafe action, incorrect result, privacy exposure, cost risk, or debugging failure it can cause.

## Architecture Fit

- State whether single-agent, multi-agent, sandbox-backed, or explicit code orchestration is justified by the workflow.

## Eval Gaps

- Missing task-success cases.
- Missing required/forbidden tool-call assertions.
- Missing approval, guardrail, cost, latency, or failure-mode checks.

## Operations Gaps

- Missing tracing, logging, dashboards, alerting, rollout, rollback, escalation, ownership, or credential controls.

## Hardening Plan

1. Must-fix before launch.
2. Should-fix before broad rollout.
3. Follow-up monitoring or governance work.
