---
name: review-agent-production-readiness
description: >-
  Use when reviewing an OpenAI Agents SDK design, prototype, eval harness, or deployment plan for production readiness: architecture fit, tool safety, approvals, failures, evals, observability, rollout, cost, privacy, and human oversight. Do not use as the source for current SDK syntax or for non-agent systems. Return evidence-backed, severity-ordered blockers, gaps, and hardening actions.
---

# Review Agent Production Readiness

## Workflow

1. Bound the review: goal, inputs and outputs, tools, state, side effects, approvals, runtime, users, and deployment stage. Review only; do not implement hardening unless asked.
2. Inspect the real evidence available: code, external prompt files, tool schemas, eval results, traces, logs, deployment configuration, runbooks, dashboards, and incident notes. Mark unavailable evidence as unknown.
3. Read [the production-readiness checklist](references/production-readiness-checklist.md) and apply only the relevant lenses.
4. Test the architecture against concrete harms: unsafe actions, incorrect results, privacy exposure, runaway cost or latency, and failures that operators cannot diagnose or reverse.
5. Separate verified launch blockers from follow-up hardening and personal design preferences. Cite files, lines, traces, or named artifacts when possible.

## Freshness Gate

Use the official OpenAI Agents SDK documentation or the official Agents SDK skill whenever a conclusion depends on current SDK APIs, model behavior, tracing, sandbox semantics, eval configuration, or deployment commands. Record the documentation URL and access date in a full report. Do not rely on examples in this skill for version-sensitive syntax.

## Output Shape

Lead with severity-ordered findings, then cover architecture fit, eval gaps, operations gaps, and an ordered hardening plan. If no launch blockers are supported by evidence, say so plainly and still identify unknowns.

For a full report, read the [worked readiness review](examples/readiness-review-output.md). For a design-only request, adapt its headings into a tailored pre-launch checklist.
