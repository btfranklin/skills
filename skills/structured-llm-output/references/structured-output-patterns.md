# Structured Output Patterns

Use this reference after the target object, source, consumer, and failure cost are known.

## Choose The Contract

- Model the smallest object downstream code needs.
- Use enumerations for closed vocabularies. Use limited strings or numbers when the domain supplies real limits.
- Distinguish absent, unknown, not applicable, and empty values. Do not hide missing evidence behind a fabricated default.
- For extraction, preserve source provenance when an audit must inspect decisions.
- Reject unexpected properties at trust boundaries. Permit additional properties only when the contract requires them.

## Prefer Provider-Native Constrained Generation

Use provider-native constrained generation when it supports the required schema. It reduces syntax failures. It does not prove that values are correct, complete, safe, or supported by the input. Avoid regular-expression extraction. Do not search prose for the first brace pair. Do not depend only on an instruction to respond with JSON.

Generate schemas from the application's typed model when the provider supports this method. This keeps runtime validation and the generation contract consistent. Confirm which JSON Schema features the selected provider and model support.

## Layer Validation

1. **Transport:** the provider completed the request without a refusal or truncation.
2. **Structure:** output parses and matches the declared schema.
3. **Domain:** field and cross-field invariants hold.
4. **Faithfulness:** The source supports extracted or summarized facts.
5. **Policy:** The output satisfies unsafe-content, authorization, privacy, and human-review rules.

Keep deterministic calculations in code. A model can extract quantities and prices. Application code must calculate and compare totals.

## Bound Retries

- Retry only when another attempt can repair the failure, such as a correctable validation error.
- Return concise validation errors to the model. Do not return the full retry transcript.
- Set an explicit attempt limit and terminal outcome.
- Do not retry ambiguous or missing source evidence into a plausible-looking invention.
- Separate provider and network retries from model validation retries. Set limits and observability for both types.

## Test And Operate

Cover valid, boundary, ambiguous, adversarial, refusal, malformed, partial, and retry-exhaustion cases. Maintain representative reference inputs. Check typed output and downstream decisions. Measure validation failures, semantic failures, retries, latency, token cost, review rate, and corrections. Remove sensitive inputs and outputs from logs.

Model behavior can change when the schema does not change. Record the provider, model identifier, SDK or library versions, and verification date for repeatable comparisons. Add schema or prompt version identifiers only when a deployed or persisted compatibility boundary requires them.

## Primary Documentation

Verify current interfaces and limitations before implementation:

- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/), [validators](https://docs.pydantic.dev/latest/concepts/validators/), and [JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
- [PydanticAI output](https://ai.pydantic.dev/output/)
- [Instructor validation](https://python.useinstructor.com/learning/patterns/field_validation/) and [retry mechanisms](https://python.useinstructor.com/learning/validation/retry_mechanisms/)

Treat these pages as the authoritative sources for their products. Do not infer guarantees for other providers from one library's examples.
