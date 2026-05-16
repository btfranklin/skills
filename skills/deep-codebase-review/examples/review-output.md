# Deep Codebase Review Output Example

Use this as a shape, not boilerplate. Keep the real report grounded in the repository under review.

## Findings

1. `[Severity] Short finding title` - `path/to/file.ext:line`
   Explain the mechanism: what can fail, why the current structure makes it likely, and what evidence supports the claim.

## Structural Pressure Points

- `Area`: describe duplication, unclear ownership, lifecycle risk, or local complexity that is not yet a concrete defect.

## Roadmap / Design Alignment

- `Document or plan`: state whether current implementation matches, exceeds, contradicts, or lags the documented direction.

## Open Questions

- Name assumptions that affect the review and the evidence needed to resolve them.

## Follow-Through

- List the highest-leverage fixes in order, separating quick cleanup from architectural work.
