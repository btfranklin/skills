# Production-Readiness Review: Claims Intake Assistant

Reviewed artifacts: `agent.py`, `tools/claims.py`, `prompts/claims-agent.md`, `evals/cases.json`, and `deploy/runbook.md`. The assistant summarizes insurance claims, reads policy records, and can submit a claim to the carrier after the customer confirms. Official Agents SDK documentation was checked on 2026-07-13; version-sensitive implementation details below should be reverified before use.

## Launch Blockers

1. **Critical — the agent can submit a claim without a distinct approval step.** `tools/claims.py:88` exposes `submit_claim()` beside read-only tools, while `prompts/claims-agent.md:41` permits submission when the user appears ready. A model inference is not durable approval for an externally visible legal and financial action. Require an explicit confirmation record bound to the final claim payload, reject stale or mismatched confirmations in the tool, and use narrower write credentials.
2. **High — retries can create duplicate claims.** `tools/claims.py:104` retries carrier timeouts without an idempotency key or reconciliation lookup. A timeout after carrier acceptance can submit the same claim twice. Derive a stable key from the local claim ID, persist each attempt, and reconcile an uncertain result before retrying.
3. **High — retrieved documents can override operating instructions.** `agent.py:73` inserts policy text into the same unmarked context as trusted instructions. A malicious attachment could direct the agent to disclose another customer's record or call the write tool. Delimit retrieved content as untrusted data, restrict policy lookup by authenticated customer ID in code, and add injection cases that assert forbidden tool calls.

## Architecture Fit

A single agent with explicit application orchestration is appropriate. Policy lookup and claim submission are a short, known sequence; no evidence justifies handoffs or a planner. Keep authentication, approval state, submission, and retry control in deterministic code. The model should extract claim details, identify missing information, and draft the summary.

## Eval Gaps

- The 18 current cases grade final-answer wording but do not assert tool calls or state changes.
- Add cases where a user edits claim details after approval, denies approval, embeds instructions in an attachment, lacks access to the policy, and receives a carrier timeout after acceptance.
- Assert that `submit_claim` is forbidden before approval, called once after matching approval, and never called for an unauthorized policy.
- Capture claim ID, approval ID, tool sequence, guardrail outcome, latency, and token cost with each result.

## Operations Gaps

- Traces record full policy text and medical details with no documented retention or redaction policy.
- The runbook has no alert for duplicate submissions, repeated tool failures, approval bypasses, or max-turn exhaustion.
- There is no staged rollout, rollback trigger, incident owner, or procedure for reconciling an uncertain carrier response.
- Cost and latency budgets are undefined; the agent can loop for 30 turns after repeated carrier errors.

## Hardening Plan

1. **Before any launch:** enforce payload-bound approval in code, add carrier idempotency and reconciliation, constrain record access, and treat retrieved content as untrusted.
2. **Before a staff pilot:** add stateful tool-call evals, redact sensitive traces, cap turns and retries, and document incident ownership and rollback.
3. **Before broader rollout:** run a limited cohort with duplicate-submission and approval-bypass alerts; establish per-claim latency and cost budgets from pilot data.

## Evidence Limits

No carrier contract, privacy assessment, production trace sample, or credential policy was available. Compliance, retention, and carrier-side idempotency therefore remain unverified rather than passed.
