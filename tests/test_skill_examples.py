"""Execute published examples and check specific instruction contracts."""

import ast
from contextlib import contextmanager
from copy import deepcopy
from decimal import Decimal
from pathlib import Path
import re
import sqlite3
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from pydantic import ValidationError


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def python_example(relative_path):
    path = SKILLS / relative_path
    blocks = re.findall(r"^```python\n(.*?)^```", path.read_text(), re.M | re.S)
    if len(blocks) != 1:
        raise AssertionError(f"Expected one Python example in {path}")
    return blocks[0]


def invoice_contract():
    namespace = {"__name__": "invoice_example"}
    exec(compile(python_example(
        "structured-llm-output/examples/schema-review-output.md"
    ), "invoice_example", "exec"), namespace)
    return namespace


class InvoiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = invoice_contract()

    def setUp(self):
        def money(amount):
            return {"amount": amount, "currency": "USD"}

        self.invoice = {
            "supplier_name": "Example Supplier",
            "invoice_number": "INV-1",
            "invoice_date": "2026-09-01",
            "due_date": None,
            "subtotal": money("100"),
            "tax": money("10"),
            "total": money("110"),
            "line_items": [{
                "description": "Example item",
                "quantity": "2",
                "unit_price": money("50"),
                "line_total": money("100"),
            }],
        }

    def errors(self, data):
        invoice = self.contract["InvoiceExtraction"].model_validate(data)
        return self.contract["arithmetic_errors"](invoice, Decimal("0.01"))

    def test_taxed_invoice_passes(self):
        self.assertEqual(self.errors(self.invoice), [])

    def test_confirmed_no_separate_tax_passes(self):
        self.invoice["tax"] = None
        self.invoice["total"]["amount"] = "100"
        self.assertEqual(self.errors(self.invoice), [])

    def test_missing_and_ambiguous_values_need_no_invented_invoice(self):
        for reason in ("missing_required_text", "ambiguous_currency"):
            with self.subTest(reason=reason):
                parsed = self.contract["ExtractionResult"].model_validate({
                    "result": {"status": "review_required", "reason": reason,
                               "details": "The source does not establish the value."}
                })
                self.assertIsInstance(parsed.result, self.contract["ReviewRequired"])
                self.assertFalse(hasattr(parsed.result, "invoice"))

    def test_complete_result_rejects_missing_total(self):
        del self.invoice["total"]
        with self.assertRaises(ValidationError):
            self.contract["ExtractionResult"].model_validate({
                "result": {"status": "complete", "invoice": self.invoice}
            })

    def test_every_money_field_rejects_a_different_currency(self):
        for field in ("subtotal", "tax", "total", "unit_price", "line_total"):
            with self.subTest(field=field):
                data = deepcopy(self.invoice)
                owner = data["line_items"][0] if field in ("unit_price", "line_total") else data
                owner[field]["currency"] = "CAD"
                with self.assertRaises(ValidationError):
                    self.contract["InvoiceExtraction"].model_validate(data)

    def test_each_arithmetic_boundary_detects_a_mismatch(self):
        for field in ("quantity", "subtotal", "total"):
            with self.subTest(field=field):
                data = deepcopy(self.invoice)
                if field == "quantity":
                    data["line_items"][0][field] = "3"
                else:
                    data[field]["amount"] = "999"
                self.assertTrue(self.errors(data))

    def test_model_cannot_add_payment_instructions(self):
        self.invoice["bank_account"] = "unrequested"
        with self.assertRaises(ValidationError):
            self.contract["InvoiceExtraction"].model_validate(self.invoice)


class ReceiptStore:
    """Use SQLite to preserve receipts across failed queue calls."""

    def __init__(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE receipts (id INTEGER PRIMARY KEY, webhook_id TEXT UNIQUE)")
        self.callbacks = []

    @contextmanager
    def atomic(self):
        self.callbacks = []
        with self.db:
            yield
        for callback in self.callbacks:
            callback()

    def on_commit(self, callback):
        self.callbacks.append(callback)

    def get_or_create(self, webhook_id, defaults):
        row = self.db.execute("SELECT id FROM receipts WHERE webhook_id = ?", (webhook_id,)).fetchone()
        if row:
            return SimpleNamespace(pk=row[0]), False
        cursor = self.db.execute("INSERT INTO receipts (webhook_id) VALUES (?)", (webhook_id,))
        return SimpleNamespace(pk=cursor.lastrowid), True


class WebhookTests(unittest.TestCase):
    def setUp(self):
        self.store = ReceiptStore()
        self.addCleanup(self.store.db.close)
        self.queue = Mock()
        self.signature_error = type("InvalidSignature", (Exception,), {})
        self.client = SimpleNamespace(webhooks=SimpleNamespace(unwrap=Mock(
            return_value=SimpleNamespace(type="response.completed", data=SimpleNamespace(id="resp-1"))
        )))
        tree = ast.parse(python_example(
            "openai-django-webhooks/references/OPENAI_DJANGO_WEBHOOKS.md"
        ))
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef))
        function.decorator_list = []
        namespace = {
            "transaction": self.store,
            "WebhookDelivery": SimpleNamespace(objects=self.store),
            "enqueue_webhook_delivery": self.queue,
            "client": self.client,
            "settings": SimpleNamespace(OPENAI_WEBHOOK_SECRET="test-secret"),
            "InvalidWebhookSignatureError": self.signature_error,
            "HttpResponse": lambda status: status,
        }
        exec(compile(ast.Module(body=[function], type_ignores=[]), "webhook_example", "exec"), namespace)
        self.endpoint = namespace["openai_webhook"]
        self.request = SimpleNamespace(body=b"signed body", headers={"webhook-id": "event-1"})

    def test_queue_failure_then_redelivery_recovers_committed_receipt(self):
        self.queue.side_effect = [ConnectionError("Queue unavailable"), None]
        with self.assertRaises(ConnectionError):
            self.endpoint(self.request)
        self.assertEqual(self.store.db.execute("SELECT COUNT(*) FROM receipts").fetchone()[0], 1)
        self.assertEqual(self.endpoint(self.request), 200)
        self.assertEqual(self.queue.call_count, 2)
        self.assertEqual(self.queue.call_args_list[0], self.queue.call_args_list[1])

    def test_uncertain_acceptance_reuses_delivery_identity(self):
        accepted = []

        def accept_then_timeout(delivery_id):
            accepted.append(delivery_id)
            raise TimeoutError("Acceptance response lost")

        self.queue.side_effect = accept_then_timeout
        with self.assertRaises(TimeoutError):
            self.endpoint(self.request)
        self.queue.side_effect = accepted.append
        self.assertEqual(self.endpoint(self.request), 200)
        self.assertEqual(accepted, [1, 1])

    def test_invalid_signature_does_not_record_or_enqueue(self):
        self.client.webhooks.unwrap.side_effect = self.signature_error()
        self.assertEqual(self.endpoint(self.request), 400)
        self.queue.assert_not_called()
        self.assertEqual(self.store.db.execute("SELECT COUNT(*) FROM receipts").fetchone()[0], 0)


class InstructionContractTests(unittest.TestCase):
    """Protect the resolved rules; these checks do not grade agent behavior."""

    def test_both_database_documents_prohibit_substitute_engines(self):
        for relative in ("references/patterns.md", "examples/performance-suite-plan.md"):
            with self.subTest(document=relative):
                text = (SKILLS / "django-pytest-performance-suite" / relative).read_text()
                self.assertIn("Do not use a substitute engine.", text)
                self.assertNotIn("If a test uses a substitute engine", text)

    def test_missing_companion_uses_local_fallback(self):
        text = (SKILLS / "design-ui-style-guide/SKILL.md").read_text()
        self.assertIn("If `design-html-first-web-uis` is missing, continue", text)
        self.assertNotIn("Ask the user to approve that exact installation", text)


if __name__ == "__main__":
    unittest.main()
