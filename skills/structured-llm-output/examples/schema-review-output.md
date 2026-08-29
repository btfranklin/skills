# Invoice Extraction Schema Review

## Context

The pipeline extracts supplier invoices from OCR text into an accounts-payable import. An incorrect total or currency can cause a payment error. Therefore, a person must review ambiguous financial fields. The pipeline must not use inferred defaults.

## Proposed Contract

```python
from datetime import date
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class Money(BaseModel):
    model_config = ConfigDict(extra="forbid")

    amount: Decimal = Field(ge=0)
    currency: str = Field(pattern=r"^[A-Z]{3}$")


class LineItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    description: str = Field(min_length=1)
    quantity: Decimal = Field(gt=0)
    unit_price: Money
    line_total: Money


class InvoiceExtraction(BaseModel):
    model_config = ConfigDict(extra="forbid")

    supplier_name: str = Field(min_length=1)
    invoice_number: str = Field(min_length=1)
    invoice_date: date
    due_date: date | None
    subtotal: Money
    tax: Money | None
    total: Money
    line_items: list[LineItem] = Field(min_length=1)
    review_reason: Literal[
        "none", "ambiguous_currency", "total_mismatch", "missing_required_text"
    ]

    @model_validator(mode="after")
    def dates_and_currency_agree(self) -> "InvoiceExtraction":
        if self.due_date is not None and self.due_date < self.invoice_date:
            raise ValueError("due_date cannot precede invoice_date")
        currencies = {
            self.subtotal.currency,
            self.total.currency,
            *(item.line_total.currency for item in self.line_items),
        }
        if len(currencies) != 1:
            raise ValueError("all monetary fields must use one currency")
        return self
```

`review_reason` uses named states instead of a confidence score. The pipeline cannot reliably calibrate a numeric confidence value. The named states correspond directly to review routing. `due_date` and `tax` can be absent. Required identifiers and totals cannot be absent.

## Generation And Validation Flow

1. Send OCR text and the external extraction prompt through provider-native constrained generation.
2. Parse the result into `InvoiceExtraction`. Reject extra fields.
3. Compare `subtotal + tax` with `total`. Compare the sum of line totals with the invoice total. Use the product's documented rounding tolerance.
4. Check that source text supports each extracted identifier and amount. Store source spans separately from the accounting object when an audit requires provenance.
5. Route `review_reason != "none"` and arithmetic mismatches to human review. Do not import them automatically.

## Retry Policy

- Retry once for schema or cross-field validation failures, returning the exact validation errors to the model.
- Do not retry unreadable OCR, missing required source text, or policy refusals as if they were formatting errors.
- After the final retry, retain the OCR document, request identifier, model identifier, validation errors, and response metadata without sensitive data. Do not store invoice text without redaction in general application logs.

## Test Cases

| Case | Expected result |
|---|---|
| Complete USD invoice | Valid object; `review_reason="none"` |
| Tax omitted and subtotal equals total | Valid object with `tax=None` |
| `$` can mean USD, CAD, or AUD | `ambiguous_currency`; human review |
| Printed total differs from line-item sum | `total_mismatch`; no automatic import |
| Prompt injection in a line-item description | Treat as invoice text. Preserve the safe string value. |
| Model adds `bank_account` | Validation failure because extras are forbidden |
| Invalid date repaired on second attempt | Accept second result and count one validation retry |
| Required total absent from OCR | `missing_required_text`; no retry-based invention |

## Production Notes

Track schema-validation failures, semantic mismatches, retry count, review rate, and reviewer corrections. Add schema and prompt version identifiers only when a deployed or persisted comparison boundary requires them. Run the reference invoice set again before you change the provider, model snapshot, prompt, OCR engine, or schema.
