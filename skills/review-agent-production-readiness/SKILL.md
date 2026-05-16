---
name: review-agent-production-readiness
description: >-
  Use when reviewing or hardening an OpenAI Agents SDK design, prototype, eval harness, or deployment plan for production readiness: architecture fit, tool safety, guardrails, approvals, failure modes, eval coverage, tracing, monitoring, rollout, cost/latency, privacy, compliance, and human oversight. Do not use as the primary source for building current SDK code, checking latest API syntax, generic OpenAI API troubleshooting, or non-agent application reviews; prefer official Agents SDK docs/skill first for implementation details. Output severity-ordered launch blockers, eval gaps, operations gaps, architecture-fit notes, and an ordered hardening plan.
---

# Review Agent Production Readiness

Use this skill as a second-pass production review for Agents SDK work. It is not a replacement for the official OpenAI Agents SDK skill or current OpenAI documentation.

## Workflow

1. Establish the target workflow: user goal, input/output contract, tools, state, side effects, approval gates, runtime surface, and whether the design is single-agent, multi-agent, sandbox-backed, or explicitly orchestrated code.
2. If the request requires current SDK APIs, implementation changes, sandbox semantics, eval platform config, or deployment commands, read the official Agents SDK docs or use the official OpenAI Agents SDK skill first.
3. Read `references/production-readiness-checklist.md` for the applicable review lenses.
4. Review the real artifact whenever available: source code, prompts, tool schemas, eval cases, traces, logs, deployment config, runbooks, dashboards, or incident notes.
5. Report concrete gaps before general advice. Separate must-fix launch blockers from follow-up hardening.

## Review Stance

- Prefer the simplest architecture that satisfies the workflow. Start with one agent and explicit code orchestration unless specialization, handoffs, or sandbox execution have a clear payoff.
- Treat every tool as a production interface: validate inputs, constrain permissions, bound runtime, make side effects idempotent where possible, and require approvals for irreversible or externally visible actions.
- Judge evals against behavior that matters: task success, required or forbidden tool calls, approvals, guardrails, state changes, traceability, failure handling, cost, and latency.
- Require observability that can diagnose real failures: trace IDs, tool-call logs, error classes, turn counts, latency/cost signals, escalation events, and enough context to reproduce issues without leaking secrets.
- Keep governance practical: scoped credentials, privacy controls, audit logs, rollout/rollback paths, human escalation, and ownership for incidents.

## Output Shape

For reviews, lead with findings ordered by severity and include file or artifact references when possible. Then include:

- Architecture fit: whether single-agent, multi-agent, sandbox, or explicit orchestration is justified.
- Launch blockers: issues that can cause unsafe actions, incorrect results, runaway cost, privacy exposure, or inability to debug.
- Eval gaps: missing cases or grading signals needed before trusting the workflow.
- Operations gaps: missing monitoring, alerting, rollout, rollback, cost/latency, or human-oversight controls.
- Next actions: a short, ordered hardening plan.

For design/planning requests, produce a production-readiness checklist tailored to the workflow rather than a generic essay.

For a worked review shape, read [examples/readiness-review-output.md](examples/readiness-review-output.md) when producing a full report.
