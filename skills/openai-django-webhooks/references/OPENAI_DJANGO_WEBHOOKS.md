# OpenAI Responses Webhooks in Django

Inspect the application's models, queue, service layer, and HTMX conventions before you use this pattern. Verify current API and SDK details in primary documentation before implementation.

## Primary sources

- [OpenAI webhook guide](https://developers.openai.com/api/docs/guides/webhooks)
- [OpenAI webhook event reference](https://developers.openai.com/api/docs/api-reference/webhook-events)
- [OpenAI background mode guide](https://developers.openai.com/api/docs/guides/background)
- [Django transactions](https://docs.djangoproject.com/en/6.0/topics/db/transactions/)
- [HTMX polling](https://htmx.org/examples/polling/)

## Lifecycle and correlation

1. Create a local job record before requesting a background response.
2. Call the official SDK with `client.responses.create(..., background=True)` and store the returned response ID on that job.
3. Use the local response-ID mapping as the durable correlation mechanism. Request metadata can help after retrieval. Do not assume that the webhook event contains the full response or its metadata.
4. On a terminal webhook event, get the response ID from `event.data.id`. Retrieve the response with `client.responses.retrieve(response_id)`. Apply the transition idempotently.
5. Persist terminal failures and diagnostic identifiers. Stop polling after every terminal state, including success and failure.

Keep prompts and reusable instructions in external Markdown files. Select models from the current project configuration or from verified official guidance. Do not copy a model identifier from this reference.

## Verify and acknowledge the webhook

Use the raw request body and the official SDK helper. Do not parse JSON before signature verification.

```python
from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from openai import InvalidWebhookSignatureError, OpenAI

client = OpenAI()


@csrf_exempt
@require_POST
def openai_webhook(request):
    try:
        event = client.webhooks.unwrap(
            request.body,
            request.headers,
            secret=settings.OPENAI_WEBHOOK_SECRET,
        )
    except InvalidWebhookSignatureError:
        return HttpResponse(status=400)

    webhook_id = request.headers.get("webhook-id")
    response_id = getattr(event.data, "id", None)

    with transaction.atomic():
        delivery, _ = WebhookDelivery.objects.get_or_create(
            webhook_id=webhook_id,
            defaults={
                "event_type": event.type,
                "response_id": response_id,
            },
        )
        transaction.on_commit(lambda: enqueue_webhook_delivery(delivery.pk))

    return HttpResponse(status=200)
```

Adapt the model and queue call to the repository. Give `webhook_id` a unique database constraint. Store only the event fields that processing and diagnostics require. Do not retain sensitive payloads by default.

Enqueue the delivery after every verified request, including a duplicate request. A saved receipt does not prove that the queue accepted the work. The queue call must raise if it cannot confirm durable acceptance. Let that failure produce a non-`2xx` response. A repeated request then retries enqueueing with the same delivery ID. If queue acceptance is uncertain, a repeated request can enqueue twice. The worker must safely skip completed deliveries. Use a durable queue with worker retries; an in-process callback alone is not durable.

The endpoint must perform only signature verification, durable deduplication, and enqueueing. Return a successful `2xx` within a few seconds. Use the application's background worker for response retrieval and other work that can delay the response.

## Process the delivery idempotently

The worker must:

1. Lock or atomically claim the delivery record.
2. Exit successfully if that delivery is already complete.
3. Resolve the local job by the stored OpenAI response ID.
4. Retrieve the full response for events that require response data.
5. Persist output through the project's service layer. Use the SDK's `response.output_text` when the expected result is text.
6. Apply state transitions with compare-and-set or row locking so duplicate or out-of-order work cannot regress a terminal job.
7. Record retryable processing failures for the application's worker retry policy. Mark permanent failures explicitly.

Prefer to log and acknowledge unknown event types. Do not retry them without a defined stop condition. Before you write terminal-state rules, verify the subscribed event types and their current schemas in the webhook event reference.

## Delivery failures and duplicates

- OpenAI retries webhook deliveries that do not receive a successful `2xx`. It uses exponential backoff for up to 72 hours.
- The service treats redirects as failures. Configure the final endpoint URL directly.
- Duplicate deliveries can occur. Use the `webhook-id` header to remove duplicates. Also make the worker idempotent.
- Once the endpoint has acknowledged an event, processing retries belong to the application's queue. Do not rely on OpenAI to redeliver successfully acknowledged work.
- If signature verification or durable receipt fails, return a non-`2xx` response so the delivery can be retried.

## HTMX polling

Return the initial job fragment immediately after the application creates the background response. While the local job is not terminal, the fragment can poll a status endpoint:

```html
<section
  id="job-{{ job.pk }}"
  hx-get="{% url 'job-status' job.pk %}"
  hx-trigger="every 2s"
  hx-swap="outerHTML"
>
  Processing…
</section>
```

The status view must authorize access to the job on every request. Return a pending fragment that continues polling while work continues. When the job reaches a terminal state, return a final success or failure fragment without `hx-trigger`. Handle missing, expired, and unauthorized jobs explicitly.

## Validation matrix

- Valid and invalid signatures using the raw request body
- Duplicate `webhook-id` deliveries
- Unknown and out-of-order event types
- Unknown response IDs and unauthorized job access
- Response retrieval failure followed by worker retry
- Successful completion and each supported terminal failure
- Database failure before durable receipt
- Queue failure after transaction commit, followed by a repeated delivery that enqueues the saved record
- Uncertain queue acceptance followed by duplicate worker execution
- Polling termination for success, failure, expiry, and deletion
- Redaction of secrets and sensitive response content from logs
