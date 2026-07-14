# OpenAI Responses Webhooks in Django

Use this pattern after inspecting the application's models, queue, service layer, and HTMX conventions. Verify current API and SDK details from primary documentation before implementation.

## Primary sources

- [OpenAI webhook guide](https://developers.openai.com/api/docs/guides/webhooks)
- [OpenAI webhook event reference](https://developers.openai.com/api/docs/api-reference/webhook-events)
- [OpenAI background mode guide](https://developers.openai.com/api/docs/guides/background)
- [Django transactions](https://docs.djangoproject.com/en/6.0/topics/db/transactions/)
- [HTMX polling](https://htmx.org/examples/polling/)

## Lifecycle and correlation

1. Create a local job record before requesting a background response.
2. Call the official SDK with `client.responses.create(..., background=True)` and store the returned response ID on that job.
3. Treat the local response-ID mapping as the durable correlation mechanism. Request metadata may be useful after retrieval, but the webhook event itself should not be assumed to contain the full response or its metadata.
4. On a terminal webhook event, obtain the response ID from `event.data.id`, retrieve the response with `client.responses.retrieve(response_id)`, and apply the transition idempotently.
5. Persist terminal failures and diagnostic identifiers. Stop polling after every terminal state, not only success.

Keep prompts and reusable instructions in external Markdown files. Select models from current project configuration or verified official guidance rather than copying a model identifier from this reference.

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
        delivery, created = WebhookDelivery.objects.get_or_create(
            webhook_id=webhook_id,
            defaults={
                "event_type": event.type,
                "response_id": response_id,
            },
        )
        if created:
            transaction.on_commit(lambda: enqueue_webhook_delivery(delivery.pk))

    return HttpResponse(status=200)
```

Adapt the model and queue call to the repository. Give `webhook_id` a unique database constraint. Store only the event fields needed for processing and diagnostics; do not retain sensitive payloads by default.

The endpoint should perform signature verification, durable deduplication, and enqueueing only. Return a successful `2xx` within a few seconds. Offload response retrieval and other non-trivial work to the application's background worker.

## Process the delivery idempotently

The worker should:

1. Lock or atomically claim the delivery record.
2. Exit successfully if that delivery is already complete.
3. Resolve the local job by the stored OpenAI response ID.
4. Retrieve the full response for events that require response data.
5. Persist output through the project's normal service layer. The SDK's `response.output_text` is the simplest text accessor when text is the expected result.
6. Apply state transitions with compare-and-set or row locking so duplicate or out-of-order work cannot regress a terminal job.
7. Record retryable processing failures for the application's worker retry policy and mark permanent failures explicitly.

Unknown event types should normally be logged and acknowledged rather than retried forever. Verify the subscribed event types and their current schemas in the webhook event reference before coding terminal-state rules.

## Delivery failures and duplicates

- OpenAI retries webhook deliveries that do not receive a successful `2xx`, using exponential backoff for up to 72 hours.
- Redirects are treated as failures; configure the final endpoint URL directly.
- Duplicate deliveries can occur. Deduplicate with the `webhook-id` header and still make the worker idempotent.
- Once the endpoint has acknowledged an event, processing retries belong to the application's queue. Do not rely on OpenAI to redeliver successfully acknowledged work.
- If signature verification or durable receipt fails, return a non-`2xx` response so the delivery can be retried.

## HTMX polling

Return the initial job fragment immediately after the background response is created. While the local job is non-terminal, the fragment may poll a status endpoint:

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

The status view should authorize access to the job on every request. Return a pending fragment that retains polling while work continues. Return a final success or failure fragment without `hx-trigger` when the job reaches a terminal state. Handle missing, expired, and unauthorized jobs explicitly.

## Validation matrix

- Valid and invalid signatures using the raw request body
- Duplicate `webhook-id` deliveries
- Unknown and out-of-order event types
- Unknown response IDs and unauthorized job access
- Response retrieval failure followed by worker retry
- Successful completion and each supported terminal failure
- Database failure before durable receipt
- Queue failure after transaction commit
- Polling termination for success, failure, expiry, and deletion
- Redaction of secrets and sensitive response content from logs
