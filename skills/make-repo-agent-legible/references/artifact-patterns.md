# Agent-Legible Artifact Patterns

Select the smallest durable artifact that resolves the diagnosed discovery failure. Match existing repository vocabulary and layout.

## Scale The Artifact Set

For a small package or service, a README, short `AGENTS.md`, and one focused operations or architecture note may be sufficient. Add an indexed docs area only when several durable topics need separate ownership. Do not create empty architecture, security, reliability, decision, or planning documents to satisfy a generic tree.

## Common Artifacts

| Artifact | Use it when |
|---|---|
| README quickstart | The smallest useful install, run, or adoption loop is hard to discover. |
| `AGENTS.md` task map | Agents repeatedly search for commands, constraints, ownership, or task-specific entry points. |
| Architecture map | Domains, interfaces, or allowed dependency directions are not inferable safely. |
| Operations guide | Deploy, rollback, recovery, jobs, or external ownership depend on human memory. |
| Quality/reliability note | Important validation expectations span several tools or failure modes. |
| Decision record | A durable non-obvious tradeoff is likely to be reopened without its rationale. |
| Execution plan | Multi-iteration work needs versioned acceptance criteria and status. |
| Generated reference | Agents repeatedly rediscover schemas, inventories, contracts, or external state. |

Put each fact in one authoritative place and link to it from entry points. Preserve `unknown` or `needs owner` when external knowledge cannot be verified.

## Enforcement Ladder

Promote a recurring rule only as far as its frequency and impact justify:

1. Documented convention
2. Shared helper or template
3. Structural test or lint rule
4. CI gate

Good enforcement candidates include dependency direction, boundary schemas, registries, required cross-links, generated-reference freshness, and stable naming contracts. A failure message should name the violated rule, point to its source, and give the recovery command or edit location.

## Runtime Legibility

Static prose is insufficient when the work depends on behavior. Favor reproducible entrypoint scripts, deterministic fixtures, smoke tests, browser or terminal repros, and queryable logs or traces. Document required access without copying credentials or private data into the repository.

## Delivery

Summarize what was previously undiscoverable, which artifact or check now exposes it, how it was validated, and what remains external or unenforced.
