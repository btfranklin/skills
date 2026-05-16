# Structured Output Review Example

Use this shape when reviewing or designing a structured LLM output pipeline.

## Schema Fit

- Name the target object and whether fields are minimal, typed, bounded, and aligned to downstream use.

## Validation And Retry Flow

- Parse target: Pydantic model, JSON schema, Instructor response model, or PydanticAI result type.
- Validation: field constraints, cross-field validators, enum bounds, and normalized defaults.
- Retry/repair: when to retry, when to ask for clarification, and when to fail closed.

## Failure Cases

- Refusals or empty outputs.
- Partial extraction.
- Prompt injection or unsafe field content.
- Ambiguous source text.

## Tests

- Golden examples with expected structures.
- Invalid-output cases that must fail validation.
- Regression cases for retries and post-processing.

## Production Notes

- Logging/redaction, confidence or review flags, schema migration strategy, and metrics.
