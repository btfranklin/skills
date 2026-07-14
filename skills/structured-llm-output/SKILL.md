---
name: structured-llm-output
description: >-
  Design, implement, or review typed LLM output with constrained generation, validation, bounded retries, and failure handling. Use when extraction, classification, or generated objects feed code. Do not use for ordinary prompts, unstructured chat, non-LLM validation, or API-key setup. Produce a schema and pipeline, tests, and production risks.
---

# Structured LLM Output

## Workflow

1. Inspect the source material, downstream consumer, provider, SDK, and existing validation conventions.
2. Define the smallest schema that represents the required facts. Distinguish required, optional, nullable, unknown, and unavailable values explicitly.
3. Prefer the provider's native schema-constrained output over prose instructions or manual JSON extraction.
4. Validate syntax, field constraints, cross-field invariants, and source faithfulness separately.
5. Retry only failures that another model attempt can plausibly repair. Bound attempts and preserve the final validation error.
6. Fail closed, return a typed partial result, or request human review according to the cost of a wrong value. Never invent a default for missing source evidence.
7. Test representative success, ambiguity, refusal, malformed input, unsupported values, injection attempts, and exhausted retries.
8. Report the schema contract, data flow, failure policy, observability, and unresolved risks.

Keep prompts in external Markdown files when implementing a repository workflow. Preserve the repository's provider and library choices unless the user asks for a migration.

## Freshness

Before giving provider- or library-specific code, verify the current official documentation for schema support, SDK interfaces, model compatibility, and retry behavior. Record the checked provider/library versions or verification date in the resulting review or implementation notes. Do not describe a model, SDK, or library release as latest without checking its primary source.

## Resources

- Read [references/structured-output-patterns.md](references/structured-output-patterns.md) when choosing schema, validation, retry, and production patterns.
- Read [examples/schema-review-output.md](examples/schema-review-output.md) when a concrete review shape would help.
