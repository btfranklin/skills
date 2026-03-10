# OpenAI Responses API & Webhooks in Django: A Survival Guide

**Target Audience:** AI Agents & Developers implementing Async OpenAI features.
**Context:** OpenAI's "Responses API" (Async/Agentic) behaves differently from the standard Chat Completions API.

---

## 1. The Service Layer: Calling the API

**Endpoint:** `https://api.openai.com/v1/responses`

Do NOT use the standard `chat.completions.create`. Use a raw HTTP request or a client wrapper for the Responses endpoint.

**Key Parameters:**
*   **`model`**: e.g., `gpt-4o` or `gpt-5.1`
*   **`input`**: The user request (string). **NOT** `messages`.
*   **`instructions`**: System instructions (string).
*   **`background`**: `True`. This is CRITICAL. It tells OpenAI to return immediately and call your webhook later.
*   **`metadata`**: A dictionary of your custom state (e.g., `{"conversation_id": "123"}`).

**Anti-Pattern (DO NOT DO THIS):**
*   Do NOT pass a `webhook` URL in the payload. The webhook URL is configured in the **OpenAI Dashboard**, not per-request.

```python
# Correct Usage
payload = {
    "model": "gpt-5.1",
    "background": True,
    "input": "User query here",
    "instructions": "System prompt here",
    "metadata": {"type": "chat_message", "id": "123"}
}
```

---

## 2. The Webhook View: Processing the Callback

**Security:**
Use `svix` to verify the signature. Access `request.headers` and `request.body`.

```python
from svix.webhooks import Webhook
wh = Webhook(settings.OPENAI_WEBHOOK_SECRET)
wh.verify(request.body, request.headers)
```

**Payload Structure & Nuances:**
The payload structure can be tricky.
1.  **Event Type:** `payload.get('type')` (e.g., `response.completed`).
2.  **Data Wrapper:** The actual data is often deep inside `payload['data']`.
3.  **Metadata Location:** It should be in `payload['data']['response']['metadata']`.

**CRITICAL FALLBACK STRATEGY:**
Sometimes, the webhook payload **truncates** or omits metadata and content.
**ALWAYS** implement this fallback logic:
1.  Try to extract `metadata`.
2.  If missing, extract `response_id` from `payload['data']['id']` or `payload['data']['response']['id']`.
3.  **Fetch the full response** from the API (`GET /v1/responses/{id}`).
4.  Use the fetched object to populate metadata and content.

**Content Extraction:**
Content is NOT a simple string. It is a list of atoms.
Look for items where `type == 'output_text'` (or legacy `message`).

```python
# Robust Extraction Logic
content = ""
output_items = response_obj.get('output', [])
for item in output_items:
    if item.get('type') == 'message': # Container
        inner = item.get('content', [])
        if isinstance(inner, list):
            for part in inner:
                if part.get('type') == 'output_text': # The actual text
                    content += part.get('text', '')
```

---

## 3. The Frontend: Asynchronous Polling

Since the API is async, you cannot render the response immediately.

**Pattern:**
1.  User sends message -> Server returns a "Thinking..." bubble (Status 200).
2.  The bubble includes an HTMX trigger to **poll** a status endpoint.
    *   `hx-get="/chat/{id}/poll/"`
    *   `hx-trigger="every 2s"`
3.  **Polling View:** Checks the DB.
    *   If **Not Ready**: Return `HttpResponse(status=204)` (No Content). HTMX does nothing and polls again.
    *   If **Ready**: Return the rendered message HTML. HTMX replaces the bubble.

---

## Summary Checklist
- [ ] Service: Use `background: True`.
- [ ] Service: Use `input` (user) and `instructions` (system).
- [ ] View: Verify Webhook Signature.
- [ ] View: **Implement "Fetch on Missing Metadata" Fallback.**
- [ ] View: specific extraction for `output_text`.
- [ ] UI: Implement `hx-trigger="every 2s"` polling loop.
