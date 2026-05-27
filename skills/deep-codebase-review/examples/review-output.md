# Deep Codebase Review Output Example

Use this as a shape, not boilerplate. Keep the real report grounded in the repository under review.

For default sub-agent council reviews, do not paste raw sub-agent reports. The final output should read as one consolidated review from the lead reviewer. Include a brief review-method note when it helps the user understand scope, delegated roles, or residual risk.

## Review Method

- Optional: state whether this was a council review or a solo multi-pass review, name delegated roles when relevant, and list important scope limits.

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
