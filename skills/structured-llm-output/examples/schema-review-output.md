# Invoice Extraction Schema Review

## Context

The pipeline extracts supplier invoices from OCR text into an accounts-payable import. An incorrect total or currency can cause a payment error. Therefore, a person must review ambiguous financial fields. The pipeline must not use inferred defaults.

## Proposed Contract

```python
from datetime import date
from decimal import Decimal
from typing import Annotated, Literal

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

    @model_validator(mode="after")
    def dates_and_currency_agree(self) -> "InvoiceExtraction":
        if self.due_date is not None and self.due_date < self.invoice_date:
            raise ValueError("due_date cannot precede invoice_date")
        currencies = {
            self.subtotal.currency,
            self.total.currency,
            *(item.line_total.currency for item in self.line_items),
            *(item.unit_price.currency for item in self.line_items),
            *([self.tax.currency] if self.tax is not None else []),
        }
        if len(currencies) != 1:
            raise ValueError("all monetary fields must use one currency")
        return self


class CompleteInvoice(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["complete"]
    invoice: InvoiceExtraction


class ReviewRequired(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["review_required"]
    reason: Literal[
        "ambiguous_currency", "total_mismatch", "missing_required_text",
        "unsupported_calculation",
    ]
    details: str = Field(min_length=1)


class ExtractionResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    result: Annotated[
        CompleteInvoice | ReviewRequired, Field(discriminator="status")
    ]


def arithmetic_errors(
    invoice: InvoiceExtraction, tolerance: Decimal
) -> list[str]:
    if not tolerance.is_finite() or tolerance < 0:
        raise ValueError("tolerance must be finite and nonnegative")
    errors = []
    for index, item in enumerate(invoice.line_items):
        if abs(item.quantity * item.unit_price.amount - item.line_total.amount) > tolerance:
            errors.append(f"line_items[{index}]: quantity times unit_price differs from line_total")
    line_sum = sum((item.line_total.amount for item in invoice.line_items), Decimal(0))
    if abs(line_sum - invoice.subtotal.amount) > tolerance:
        errors.append("line totals differ from subtotal")
    tax_amount = invoice.tax.amount if invoice.tax is not None else Decimal(0)
    if abs(invoice.subtotal.amount + tax_amount - invoice.total.amount) > tolerance:
        errors.append("subtotal plus tax differs from total")
    return errors
```

`ExtractionResult` separates a complete candidate from a request for human review. `ReviewRequired` needs no invented identifier, amount, or currency. It cannot enter the accounting import. A `complete` status means that required fields are present. It does not authorize import before host validation.

This example supports invoices with line totals before tax. It requires `quantity * unit_price = line_total`, `sum(line_totals) = subtotal`, and `subtotal + tax = total`, within the product's documented rounding tolerance. Supply that tolerance as a `Decimal`. Do not derive it from model output.

`tax=None` means that the source confirms no separate tax charge. It does not mean that tax is unknown. `due_date=None` means that the source has no due date. Route unknown tax to `missing_required_text`. Route tax-inclusive prices, discounts, fees, and other unsupported calculations to `unsupported_calculation`. Extend the contract only when the consumer supports those calculations.

## Generation And Validation Flow

1. Send OCR text and the external extraction prompt through provider-native constrained generation. Check provider support for the union schema before use.
2. Parse the result into `ExtractionResult`. Reject extra fields.
3. Route `ReviewRequired` to human review. Retain the source document with the review request.
4. For `CompleteInvoice`, run `arithmetic_errors` with the product's documented rounding tolerance. Route any errors to human review as `total_mismatch`. Do not retry a printed arithmetic mismatch to change source values.
5. Check that source text supports every extracted identifier, date, quantity, amount, and currency. Check that the source supports the calculation model. Route missing or ambiguous evidence to human review. Store source spans separately from the accounting object when an audit requires provenance.
6. Import only a complete invoice that passes arithmetic and source checks. Do not use the model's status as import authorization.

## Retry Policy

- Retry once for schema or cross-field validation failures, returning the exact validation errors to the model.
- Do not retry unreadable OCR, missing required source text, or policy refusals as if they were formatting errors.
- After the final retry, retain the OCR document, request identifier, model identifier, validation errors, and response metadata without sensitive data. Do not store invoice text without redaction in general application logs.

## Test Cases

| Case | Expected result |
|---|---|
| Complete USD invoice | `CompleteInvoice`; import only after host checks |
| No separate tax charge; subtotal equals total | `CompleteInvoice` with `tax=None` only when the source confirms no separate tax charge |
| `$` can mean USD, CAD, or AUD | `ambiguous_currency`; human review |
| Printed subtotal differs from line-item sum | `total_mismatch`; no automatic import |
| Prompt injection in a line-item description | Treat as invoice text. Preserve the safe string value. |
| Model adds `bank_account` | Validation failure because extras are forbidden |
| Invalid date repaired on second attempt | Accept second result and count one validation retry |
| Required total absent from OCR | `ReviewRequired` with `missing_required_text`; no invented total |
| Tax currency or unit-price currency differs | Cross-field validation failure; no automatic import |
| Subtotal 100, tax 10, total 110, line sum 100 | Arithmetic checks pass |
| Quantity times unit price differs from line total | `total_mismatch`; human review |
| Tax is unknown | `missing_required_text`; do not replace unknown tax with zero |
| Tax-inclusive prices or a separate discount | `unsupported_calculation`; human review |

## Production Notes

Track schema-validation failures, semantic mismatches, retry count, review rate, and reviewer corrections. Add schema and prompt version identifiers only when a deployed or persisted comparison boundary requires them. Run the reference invoice set again before you change the provider, model snapshot, prompt, OCR engine, or schema.
