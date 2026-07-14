---
name: llms-txt-authoring
description: >-
  Use when creating, updating, validating, or reviewing a site-root `llms.txt` file as a concise map to canonical, LLM-friendly content. Trigger only when `llms.txt` is explicitly in scope, not for robots.txt, sitemaps, SEO metadata, READMEs, OpenAPI documentation, or AGENTS.md. Return a proposal-aligned file or evidence-backed review with useful links and validation notes.
---

# llms.txt Authoring

## Workflow

1. Inspect the live site or repository to identify the canonical documentation, API reference, guides, and examples. Do not invent pages or descriptions.
2. Read [the format guide](references/llms.txt.md) before authoring or judging structure. Treat `llms.txt` as an emerging proposal, not a crawler-control or guaranteed-discovery standard.
3. For a new file, adapt [the starter template](templates/llms.txt). Keep the H1, summary, context, categories, links, and descriptions concise; omit empty or low-value sections.
4. Validate the exact `/llms.txt` location, Markdown structure, absolute canonical URLs, truthful descriptions, duplicate links, and reachable targets when network access is available.
5. Return the complete file or severity-ordered findings. Distinguish proposal violations from optional editorial improvements.

## Freshness Gate

Before asserting required syntax, special section semantics, adoption, or ecosystem behavior, verify the current proposal at `https://llmstxt.org/` and prefer its linked primary materials. Record the source URL and access date in review notes. Never promise indexing, training, ranking, citation, or crawler behavior from publishing the file.
