# Production-Readiness Review: Claims Intake Assistant

Reviewed artifacts: `agent.py`, `tools/claims.py`, `prompts/claims-agent.md`, `evals/cases.json`, and `deploy/runbook.md`. The assistant summarizes insurance claims and reads policy records. It can submit a claim to the carrier after the customer confirms. The reviewer checked official Agents SDK documentation on 2026-07-13. Verify the version-sensitive implementation details again before use.

## Launch Blockers

1. **Critical — the agent can submit a claim without a distinct approval step.** `tools/claims.py:88` exposes `submit_claim()` beside read-only tools. `prompts/claims-agent.md:41` permits submission when the user appears ready. A model inference is not recorded approval for an externally visible legal and financial action. Require an explicit confirmation record that is bound to the final claim payload. Make the tool reject obsolete or mismatched confirmations. Use write credentials with narrower permissions.
2. **High — retries can create duplicate claims.** `tools/claims.py:104` retries carrier timeouts without an idempotency key or reconciliation lookup. A timeout after carrier acceptance can submit the same claim twice. Derive a stable key from the local claim ID, persist each attempt, and reconcile an uncertain result before retrying.
3. **High — retrieved documents can override operating instructions.**
   `agent.py:73` inserts policy text into the same unmarked context as trusted instructions. A malicious attachment can direct the agent to disclose another customer's record or call the write tool. Mark retrieved content as untrusted data. Restrict policy lookup by authenticated customer ID in code. Add injection cases that confirm that prohibited tool calls do not occur.

## Architecture Fit

A single agent with explicit application control is suitable. Policy lookup and claim submission form a short known sequence. No evidence supports handoffs or a planner. Keep authentication, approval state, submission, and retry control in deterministic code. The model must extract claim details, identify missing information, and draft the summary.

## Eval Gaps

- The 18 current cases grade final-answer wording but do not assert tool calls or state changes.
- Add a case in which a user edits claim details after approval. Add cases for denied approval and instructions in an attachment. Add cases for unauthorized policy access and a carrier timeout after acceptance.
- Assert that `submit_claim` is forbidden before approval, called once after matching approval, and never called for an unauthorized policy.
- Capture the claim ID, approval ID, tool sequence, safety-check result, latency, and token cost with each result.

## Operations Gaps

- Traces record full policy text and medical details with no documented retention or redaction policy.
- The runbook has no alert for duplicate submissions, repeated tool failures, approval bypasses, or max-turn exhaustion.
- There is no staged rollout, rollback trigger, incident owner, or procedure for reconciling an uncertain carrier response.
- The team has not defined cost and latency budgets. The agent can loop for 30 turns after repeated carrier errors.

## Hardening Plan

1. **Before any launch:** Enforce approval that is bound to the payload. Add carrier idempotency and reconciliation. Limit record access. Treat retrieved content as untrusted.
2. **Before a staff pilot:** Add stateful tool-call evaluations. Remove sensitive data from traces. Limit turns and retries. Document incident ownership and rollback.
3. **Before broader rollout:** Run a limited user group with alerts for duplicate submission and approval bypass. Establish latency and cost budgets for each claim from pilot data.

## Evidence Limits

No carrier contract, privacy assessment, production trace sample, or credential policy was available. Compliance, retention, and carrier-side idempotency therefore remain unverified rather than passed.
