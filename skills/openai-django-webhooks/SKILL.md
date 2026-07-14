---
name: openai-django-webhooks
description: >-
  Use when building, wiring, or debugging asynchronous OpenAI Responses API workflows in Django: background requests, signed webhooks, response correlation, persistence, and HTMX status polling. Do not use for generic OpenAI calls, non-Django consumers, unrelated webhook providers, or frontend-only polling. Return scoped Django code or a plan covering security, lifecycle, failures, and validation.
---

# OpenAI Django Webhooks

## Workflow

1. Inspect the existing Django service, models, URLs, views, jobs, templates, and OpenAI client usage. Preserve established project conventions.
2. Define the lifecycle before coding: local record ID, OpenAI response ID, allowed states, terminal failures, duplicate events, retry policy, and which component owns each transition.
3. Read [the Django webhook flow reference](references/OPENAI_DJANGO_WEBHOOKS.md) for service, callback, response extraction, and HTMX polling patterns. Treat code snippets as illustrative until checked against current official documentation.
4. Keep OpenAI calls and state transitions in a service layer. Authenticate the callback, acknowledge it promptly, make processing idempotent, persist failures, and prevent polling after a terminal state.
5. Validate signature failures, duplicate delivery, out-of-order or unknown events, retrieval failure, terminal response failure, successful completion, and polling termination. Report exact evidence when diagnosing rather than guessing from symptoms.

## Freshness Gate

Verify current OpenAI Responses API fields, webhook event shapes, SDK verification helpers, retry behavior, and supported models in official OpenAI documentation before implementation. Record the documentation URL and access date in a plan or review. Check current Django and HTMX documentation when behavior depends on their versions; do not copy version-sensitive examples blindly.
