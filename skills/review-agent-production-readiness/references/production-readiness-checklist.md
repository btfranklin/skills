# Production Readiness Checklist

Use this reference to review OpenAI Agents SDK systems for production risk. Apply only the sections relevant to the user's workflow and artifact.

## Architecture Fit

- Prefer a single `Agent` plus explicit orchestration until there is evidence that specialists, handoffs, structured outputs, or sandbox execution are needed.
- Prefer deterministic code flow for known sequences. Use planner-style agent behavior only when the next step genuinely depends on user context or model judgment.
- Use multi-agent designs when specialization, parallelism, or routing is valuable enough to justify extra latency, token cost, context-passing risk, and debugging complexity.
- Use sandbox-backed agents only when the agent must inspect files, run commands, use workspace skills, or create artifacts in an isolated workspace.
- Define the contract before judging architecture: goal, inputs, outputs, tools, state, permissions, approval gates, and smoke command.

## Tools and Side Effects

- Give each tool a narrow purpose, explicit name, clear docstring, typed arguments, and constrained schemas.
- Validate tool inputs at the boundary even when SDK schema generation is present.
- Add timeouts, retry limits, payload limits, and explicit error handling around network, file, database, or shell operations.
- Make side-effecting tools idempotent where possible. Use idempotency keys, duplicate detection, dry-run modes, or confirmation records for actions like billing, messaging, writes, deletes, deployment, and ticket creation.
- Separate read-only tools from write tools. Give write tools narrower credentials and more approval friction.
- Log tool calls with trace/session correlation, sanitized arguments, result class, duration, and failure reason.

## Guardrails, Approvals, and Escalation

- Add input guardrails for prompt injection, unsupported scope, unsafe instructions, sensitive data, and malformed requests.
- Add output guardrails for policy violations, ungrounded claims, private data disclosure, unsafe action instructions, and schema violations.
- Require explicit user or operator approval before irreversible, destructive, financial, externally visible, or security-sensitive actions.
- Define what happens when guardrails trip: block, transform, ask a clarifying question, escalate to a human, or fall back to deterministic code.
- Add human escalation paths for low confidence, repeated tool failures, high-risk user intent, policy ambiguity, or max-turn/timeout exhaustion.

## Evals and Testing

- Test deterministic tools directly with ordinary unit/integration tests before relying on agent-level evals.
- Exercise the real agent path in local evals. Avoid mocks for the behavior being judged unless the external dependency must be isolated.
- Include cases for happy paths, missing evidence, ambiguous input, tool failure, forbidden tool use, required tool use, approval gates, guardrail trips, state changes, handoffs, and regressions from observed bugs.
- Grade durable behavior rather than exact prose unless the wording is contractual.
- Capture trace IDs, tool calls, structured outputs, guardrail outcomes, state mutations, latency, and cost signals in eval results.
- Keep a small, fast smoke set for development and a broader regression set for release checks.

## Observability and Debugging

- Ensure every run has a trace or correlation ID that appears in user-facing logs, tool logs, eval results, and error reports.
- Track agent-level metrics: task success, tool success/failure, average turns, max-turn hits, timeouts, guardrail trips, handoffs, escalations, retries, latency, and cost.
- Store enough sanitized context to reproduce failures: user intent class, selected tools, tool inputs/outputs where safe, model/version, prompt/version, and deployment version.
- Make privacy choices explicit. Do not store raw sensitive data unless there is a defined need, retention policy, and access control.
- Add alerting for spikes in tool failures, timeouts, guardrail blocks, escalation rate, cost, latency, and unexpected write actions.

## Deployment and Rollout

- Require a runnable local command and a smoke result before reviewing deployment readiness.
- For HTTP services, require `PORT` support and a readiness endpoint such as `/health`.
- Version prompts, tools, eval datasets, and deployment artifacts so regressions can be traced to a concrete change.
- Use gradual rollout for high-risk workflows. Keep rollback simple and tested.
- Define owner, on-call path, incident severity, rollback trigger, and customer/support communication path.
- Verify environment variables, credentials, sandbox backend, model access, ports, containers/processes, and generated deployment files before calling a deployment ready.

## Security, Privacy, and Compliance

- Use least-privilege credentials for every external system the agent can touch.
- Keep secrets out of prompts, traces, eval fixtures, generated briefs, logs, and committed files.
- Restrict file, shell, network, and database access according to the workflow's real needs.
- Add audit logs for sensitive reads and all writes.
- Document data retention, deletion, and access-review expectations for conversations, traces, eval datasets, and tool outputs.
- For regulated or high-stakes domains, require a domain-specific review rather than relying on general-purpose guardrails.

## Cost, Latency, and Scaling

- Track cost per task or conversation and identify expensive outliers.
- Bound loops with max turns, timeouts, and fallback behavior.
- Prefer cheaper or faster paths for simple cases when quality is preserved.
- Parallelize independent work only when the latency gain is worth the added orchestration and debugging complexity.
- Cache deterministic or stable intermediate results when safe and privacy-compatible.
- Add rate limits and budget controls for user, tenant, job, or workflow scope.

## Common Failure Modes to Probe

- The agent loops on the same failing tool.
- The agent calls a write tool before approval.
- The agent ignores retrieval or evidence tools and guesses.
- A handoff loses required context or duplicates work.
- The agent treats stale state as current.
- A tool timeout or partial failure produces a confident final answer.
- A prompt injection inside retrieved/tool content changes the agent's instructions.
- Evals pass because they check prose while the workflow took the wrong action.
- Traces/logs cannot explain why a user-visible result happened.
- Cost or latency grows superlinearly as the task becomes more complex.

## Review Questions

- What exact user harm or business harm can happen if the agent is wrong?
- Which actions are irreversible or externally visible?
- What must be true before the agent can act without human approval?
- How will the team detect a model, prompt, tool, or data-source regression?
- How can an engineer reproduce a bad run from a user report?
- What is the rollback path if a new prompt, model, tool, or deployment behaves badly?
- Which logs, traces, or eval artifacts contain sensitive data?
