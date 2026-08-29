# Production Readiness Checklist

Use this reference to review OpenAI Agents SDK systems for production risk. Apply only the sections relevant to the user's workflow and artifact.

## Architecture Fit

- Prefer a single `Agent` with explicit control until evidence supports specialists, handoffs, structured outputs, or sandbox execution.
- Prefer deterministic code flow for known sequences. Use planner-style agent behavior only when the next step genuinely depends on user context or model judgment.
- Use a multi-agent design only when it has a verified net benefit. Assess specialization, parallel work, routing, latency, token cost, context-transfer risk, and debugging cost.
- Use a sandbox-backed agent only when it requires an isolated workspace. Examples include inspecting files, running commands, using workspace skills, and creating artifacts.
- Define the contract before judging architecture: goal, inputs, outputs, tools, state, permissions, approval gates, and smoke command.

## Tools and Side Effects

- Give each tool a narrow purpose, explicit name, clear docstring, typed arguments, and constrained schemas.
- Validate tool inputs at the boundary even when SDK schema generation is present.
- Add timeouts, retry limits, payload limits, and explicit error handling around network, file, database, or shell operations.
- Make tools with side effects idempotent when the external system supports it. Use idempotency keys, duplicate detection, simulation modes, or confirmation records for billing, messaging, writes, deletes, deployments, and ticket creation.
- Separate read-only tools from write tools. Give write tools narrower credentials and more approval requirements.
- Log tool calls with trace/session correlation, sanitized arguments, result class, duration, and failure reason.

## Safety Checks, Approvals, and Escalation

- Add input safety checks for prompt injection, unsupported scope, unsafe instructions, sensitive data, and malformed requests.
- Add output safety checks for policy violations, unsupported claims, private data disclosure, unsafe action instructions, and schema violations.
- Require explicit user or operator approval before irreversible, destructive, financial, externally visible, or security-sensitive actions.
- Define the response when a safety check fails. The system can block, transform, ask a question, escalate to a person, or use deterministic code.
- Add human escalation paths for low confidence, repeated tool failures, high-risk user intent, policy ambiguity, or max-turn/timeout exhaustion.

## Evals and Testing

- Test deterministic tools directly with ordinary unit/integration tests before relying on agent-level evals.
- Exercise the real agent path in local evaluations. Do not mock the behavior under review. Mock an external dependency only when the test must isolate it.
- Include successful cases and cases with missing evidence or ambiguous input. Include tool failures, prohibited tool use, required tool use, and approval checks. Include failed safety checks, state changes, handoffs, and regressions from observed defects.
- Grade durable behavior rather than exact prose unless the wording is contractual.
- Capture trace IDs, tool calls, structured outputs, safety-check results, state changes, latency, and cost signals in evaluation results.
- Keep a small, fast smoke set for development and a broader regression set for release checks.

## Observability and Debugging

- Give every run a trace or correlation ID. Include the ID in user-facing logs, tool logs, evaluation results, and error reports.
- Track agent-level metrics. Include task success, tool results, average turns, maximum-turn events, and timeouts. Also include failed safety checks, handoffs, escalations, retries, latency, and cost.
- Store enough sanitized context to reproduce failures. Include the user intent class, selected tools, and safe tool input and output data. Include the model, prompt, and deployment versions.
- Make privacy choices explicit. Do not store raw sensitive data unless there is a defined need, retention policy, and access control.
- Add alerts for increases in tool failures, timeouts, safety-check blocks, escalation rate, cost, latency, and unexpected write actions.

## Deployment and Rollout

- Require a runnable local command and a smoke result before reviewing deployment readiness.
- For HTTP services, require `PORT` support and a readiness endpoint such as `/health`.
- Record versions for prompts, tools, evaluation datasets, and deployment artifacts. Use these records to trace regressions to a specific change.
- Use a gradual rollout for high-risk workflows. Keep the rollback process simple and tested.
- Define the owner, on-call contact procedure, incident severity, rollback trigger, and customer communication procedure.
- Verify environment variables, credentials, sandbox backend, model access, ports, containers/processes, and generated deployment files before calling a deployment ready.

## Security, Privacy, and Compliance

- Use least-privilege credentials for every external system the agent can touch.
- Keep secrets out of prompts, traces, eval fixtures, generated briefs, logs, and committed files.
- Restrict file, shell, network, and database access according to the workflow's real needs.
- Add audit logs for sensitive reads and all writes.
- Document data retention, deletion, and access-review expectations for conversations, traces, eval datasets, and tool outputs.
- For regulated or high-stakes domains, require a domain-specific review. Do not rely only on general-purpose safety checks.

## Cost, Latency, and Scaling

- Track cost per task or conversation and identify expensive outliers.
- Limit loops with maximum turns, timeouts, and alternate behavior.
- Prefer lower-cost or faster paths for simple cases when they preserve quality.
- Run independent work in parallel only when the latency reduction is greater than the added orchestration and debugging cost.
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
- What is the rollback procedure if a new prompt, model, tool, or deployment behaves incorrectly?
- Which logs, traces, or eval artifacts contain sensitive data?
