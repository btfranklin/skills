# Structured Output Patterns

Use this reference after the target object, source, consumer, and failure cost are known.

## Choose The Contract

- Model the smallest object downstream code needs.
- Use enums for closed vocabularies and bounded strings or numbers where the domain supplies real limits.
- Distinguish absent, unknown, not applicable, and empty values. Do not hide missing evidence behind a fabricated default.
- For extraction, preserve source provenance when decisions must be audited.
- Reject unexpected properties at trust boundaries unless forward-compatible extras are an intentional contract.

## Prefer Constrained Generation

Use a provider's native structured-output or strict tool-schema capability when it supports the required schema. It reduces syntax failures but does not prove that values are correct, complete, safe, or grounded in the input. Avoid regex extraction, searching prose for the first brace pair, or relying only on “respond with JSON.”

Generate schemas from the application's typed model when practical so runtime validation and the generation contract do not drift. Confirm which JSON Schema features the selected provider and model currently support.

## Layer Validation

1. **Transport:** the request completed and was not refused or truncated.
2. **Structure:** output parses and matches the declared schema.
3. **Domain:** field and cross-field invariants hold.
4. **Faithfulness:** extracted or summarized facts are supported by the source.
5. **Policy:** unsafe content, authorization, privacy, and human-review rules are satisfied.

Keep deterministic calculations in code. A model may extract quantities and prices; application code should calculate and compare totals.

## Bound Retries

- Retry only when another attempt can repair the failure, such as a correctable validation error.
- Feed back concise validation errors, not an ever-growing transcript.
- Set an explicit attempt limit and terminal outcome.
- Do not retry ambiguous or missing source evidence into a plausible-looking invention.
- Separate provider/network retry policy from model validation retries; both need limits and observability.

## Test And Operate

Cover valid, boundary, ambiguous, adversarial, refusal, malformed, partial, and retry-exhaustion cases. Maintain representative golden inputs and assert both typed output and downstream decisions. Measure validation failures, semantic failures, retries, latency, token cost, review rate, and corrections. Redact sensitive inputs and outputs from logs.

Model behavior can change even when the schema does not. Record the provider, model identifier, SDK or library versions, and verification date for reproducible comparisons. Add schema or prompt version identifiers only when a deployed or persisted compatibility boundary requires them.

## Primary Documentation

Verify current interfaces and limitations before implementation:

- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/), [validators](https://docs.pydantic.dev/latest/concepts/validators/), and [JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
- [PydanticAI output](https://ai.pydantic.dev/output/)
- [Instructor validation](https://python.useinstructor.com/learning/patterns/field_validation/) and [retry mechanisms](https://python.useinstructor.com/learning/validation/retry_mechanisms/)

Treat these pages as the authority for their own products. Do not infer cross-provider guarantees from one library's examples.
