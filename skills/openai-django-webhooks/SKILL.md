---
name: openai-django-webhooks
description: >-
  Use when building, wiring, or debugging OpenAI Responses API async workflows in Django, including background responses, webhook endpoints, svix signature verification, metadata correlation, service-layer handling, and HTMX polling/status updates. Do not use for generic OpenAI API usage, non-Django webhook consumers, synchronous chat completions, Stripe/GitHub webhooks, or frontend-only polling UI without OpenAI response handling. Output Django code or a concrete implementation/debug plan covering endpoint security, response metadata, persistence, polling lifecycle, failure handling, and validation steps.
---

# OpenAI Django Webhooks

## Quick start
- Read `references/OPENAI_DJANGO_WEBHOOKS.md` for the recommended service-layer and webhook flow.
- Follow the signature verification and metadata fallback guidance when wiring endpoints.
- Use `rg` against the reference for targeted sections (webhooks, polling, svix).

## Reference map
- `references/OPENAI_DJANGO_WEBHOOKS.md`
