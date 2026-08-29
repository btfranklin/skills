# Agent-Legible Artifact Patterns

Select the smallest maintained artifact that corrects the identified discovery problem. Use the existing repository vocabulary and layout.

## Scale The Artifact Set

For a small package or service, use a README and a short `AGENTS.md`. Add one focused operations or architecture document when necessary. Add an indexed documents area only when several maintained topics need separate owners. Do not create empty documents to satisfy a generic structure.

## Common Artifacts

| Artifact | Use it when |
|---|---|
| README quickstart | The minimum useful install, run, or adoption workflow is difficult to find. |
| `AGENTS.md` task guide | Agents repeatedly search for commands, constraints, ownership, or task-specific entry points. |
| Architecture document | Agents cannot safely infer domains, interfaces, or allowed dependency directions. |
| Operations guide | Deploy, rollback, recovery, jobs, or external ownership depend on human memory. |
| Quality/reliability note | Important validation expectations span several tools or failure modes. |
| Decision record | The team can repeat a significant decision without its reason. |
| Execution plan | Multi-iteration work needs versioned acceptance criteria and status. |
| Generated reference | Agents repeatedly rediscover schemas, inventories, contracts, or external state. |

Put each fact in one authoritative place. Link to it from entry documents. Preserve `unknown` or `needs owner` when you cannot verify external knowledge.

## Enforcement Ladder

Select an enforcement level from the rule frequency and impact:

1. Documented convention
2. Shared helper or template
3. Structural test or lint rule
4. CI check

Possible enforcement candidates include dependency direction, boundary schemas, registries, required cross-links, generated-reference currency, and stable naming contracts. A failure message must name the violated rule. It must identify the rule source and give the recovery command or edit location.

## Runtime Legibility

Static prose is not sufficient when the work depends on behavior. Use repeatable entry scripts, deterministic fixtures, basic tests, browser or terminal reproductions, and queryable logs or traces. Document required access. Do not copy credentials or private data into the repository.

## Delivery

Summarize the information that was difficult to find. Identify the artifact or check that now provides it. State how you validated it. State what remains external or unenforced.
