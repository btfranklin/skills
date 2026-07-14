# llms.txt Proposal Guide

Treat `/llms.txt` as an emerging proposal for presenting concise site context and curated resource links to LLMs at inference time. It is not a crawler-control mechanism, a replacement for `robots.txt` or sitemaps, or a guarantee of discovery, indexing, training, ranking, or citation.

Primary source: [the llms.txt proposal](https://llmstxt.org/). Verify it at execution time before asserting syntax or adoption.

## Format and order

A proposal-aligned file contains these elements in order:

1. An optional byte-order mark.
2. One H1 naming the project or site. **The H1 is the only required section.**
3. An optional blockquote containing a short summary.
4. Optional Markdown paragraphs or lists, but no headings, with details needed to interpret the linked material.
5. Zero or more H2 sections containing file lists.

Each item in an H2 file list contains a required Markdown link and may add a colon followed by a concise description:

```markdown
- [Link title](https://example.com/path): Optional description.
```

`## Optional` has special meaning: links in that section may be omitted when constructing a shorter context. Use it only for genuinely secondary material.

## Authoring decisions

- Inspect the live site or repository and use canonical, absolute URLs.
- Prefer a small set of authoritative documentation, API, guide, and example pages over an exhaustive sitemap.
- Use truthful link descriptions grounded in the target page.
- Put explanatory prose before the first H2; do not create an H2 section containing free prose instead of a file list.
- Omit empty sections and links that do not materially help a reader understand the site.
- Keep `robots.txt`, sitemap, SEO, access-control, and indexing claims outside this file.

## Validation

Check:

- exact filename and intended root location;
- exactly one H1 and correct element ordering;
- H2 bodies contain Markdown link lists;
- `## Optional` contains only secondary links;
- URLs are absolute, canonical, deduplicated, and reachable when network access is available;
- titles and descriptions match the linked content;
- the file makes no unsupported claims about how third-party systems will use it.

## Minimal example

```markdown
# Example Project

> A concise description of the project and intended audience.

Use the stable API reference for exact contracts; tutorials emphasize learning paths.

## Documentation

- [Documentation](https://example.com/docs): Canonical product documentation.
- [API reference](https://example.com/api): Supported endpoints and schemas.

## Optional

- [Examples](https://example.com/examples): Additional worked integrations.
```
