# llms.txt Proposal Guide

Treat `/llms.txt` as an emerging proposal. It presents site context and a selected set of resource links to LLMs at inference time. It does not control crawlers. It does not replace `robots.txt` or sitemaps. It does not guarantee discovery, indexing, training, ranking, or citation.

Primary source: [the llms.txt proposal](https://llmstxt.org/). Verify it when you do the task. Do this before you state syntax or adoption.

## Format and order

A proposal-aligned file contains these elements in order:

1. An optional byte-order mark.
2. One H1 naming the project or site. **The H1 is the only required section.**
3. An optional blockquote containing a short summary.
4. Optional Markdown paragraphs or lists that help a reader interpret the linked material. Do not use headings in this content.
5. Zero or more H2 sections containing file lists.

Each item in an H2 file list must contain a Markdown link. You can add a colon and a short description:

```markdown
- [Link title](https://example.com/path): Optional description.
```

`## Optional` has a special meaning. A system can omit links in this section when it creates a shorter context. Use this section only for secondary material.

## Authoring decisions

- Inspect the live site or repository and use canonical, absolute URLs.
- Select a small set of authoritative documentation, API, guide, and example pages. Do not reproduce the complete sitemap.
- Use truthful link descriptions grounded in the target page.
- Put explanatory prose before the first H2. Do not put free prose in an H2 section that must contain a file list.
- Omit empty sections. Omit links that do not help a reader understand the site.
- Keep `robots.txt`, sitemap, SEO, access-control, and indexing claims outside this file.

## Validation

Check:

- Exact filename and intended root location.
- Exactly one H1 and correct element order.
- H2 bodies that contain Markdown link lists.
- An `## Optional` section that contains only secondary links.
- Absolute and canonical URLs.
- No URL occurs more than once.
- Reachable URLs when network access is available.
- Titles and descriptions that match the linked content.
- the file makes no unsupported claims about how third-party systems will use it.

## Minimal example

```markdown
# Example Project

> A short description of the project and its intended audience.

Use the stable API reference for exact contracts. Use the tutorials for guided learning.

## Documentation

- [Documentation](https://example.com/docs): Canonical product documentation.
- [API reference](https://example.com/api): Supported endpoints and schemas.

## Optional

- [Examples](https://example.com/examples): Additional worked integrations.
```
