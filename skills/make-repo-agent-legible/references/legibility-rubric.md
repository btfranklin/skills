# Repository Agent-Legibility Rubric

Score each relevant dimension as **clear**, **partial**, **missing**, or **not necessary at this repository's scale**. Cite files, commands, or observed gaps. Do not infer undocumented knowledge.

## Entry Points

Can a first-time agent learn the repository purpose, boundary, minimum useful workflow, validation commands, and next information source? Check whether the README and agent instructions provide different necessary information. Check that they do not conflict.

## Authoritative Sources

Can the agent locate the necessary authoritative product, domain, architecture, operations, and quality information? Report essential facts that exist only in chat, external tools, workflow code, or human memory. Preserve unknown ownership explicitly.

## Architecture

Can an agent find domains, interfaces, shared entry points, and prohibited dependency directions? The necessary detail depends on system complexity. Folder names can be sufficient for a small package. They are not sufficient for a system with multiple services.

## Mechanical Enforcement

Do schemas, structural tests, linters, or CI check repeated high-impact constraints? Does each failure explain the rule and recovery action? Do not recommend automation for a rare low-risk convention when documentation has a lower cost.

## Task And Decision Memory

Can an agent find the reason and status for significant current work? Add plans, debt tracking, and decision records only when work duration and recurrence justify their maintenance cost.

## Runtime Inspection

Can the agent run or reproduce the relevant behavior? Can it inspect logs, state, reports, or traces without manually copied evidence? Identify access that must remain external. Document its owner. Do not copy secrets.

## Maintenance Control

Does the repository detect obsolete links, obsolete generated artifacts, undocumented interfaces, or structural changes? Does it run these checks at a suitable interval? Prefer one focused check to broad recurring cleanup instructions.

## Prioritization

Rank findings by repeated search cost, probability of incorrect changes, operational risk, and remedy maintenance cost. Recommend one to three changes with the greatest verified benefit. Report existing strengths. State what must remain unchanged.
