# Repository Agent-Legibility Rubric

Score each relevant dimension as **clear**, **partial**, **missing**, or **not warranted at this repository's scale**. Cite files, commands, or observed gaps; do not infer undocumented knowledge.

## Entry Points

Can a first-time agent learn the repository's purpose, boundary, smallest useful loop, validation commands, and next source by task type? Check whether README and agent instructions complement rather than duplicate or contradict each other.

## Source Of Truth

Can the agent locate authoritative product, domain, architecture, operational, and quality knowledge that the repository actually needs? Flag essential facts trapped in chat, external tools, workflow code, or human memory. Preserve unknown ownership explicitly.

## Architecture

Are domains, interfaces, cross-cutting entry points, and forbidden dependency directions discoverable in proportion to the system's complexity? Folder names alone may be adequate for a tiny package but not for a multi-service system.

## Mechanical Enforcement

Are repeated high-impact constraints checked by schemas, structural tests, linters, or CI? Do failures explain the rule and recovery path? Do not recommend automation where a rare low-risk convention is cheaper to document.

## Task And Decision Memory

Can an agent recover the rationale and status of non-trivial ongoing work? Plans, debt tracking, and decision records should exist only where the work's duration and recurrence justify their maintenance.

## Runtime Inspection

Can the agent run or reproduce the relevant path and inspect logs, state, reports, or traces without relying on hand-transcribed evidence? Identify access that must remain external and document its ownership rather than copying secrets.

## Entropy Control

Does the repository catch stale links, generated artifacts, undocumented surfaces, or spreading structural drift at an appropriate cadence? Prefer one focused check over broad recurring cleanup instructions.

## Prioritization

Rank findings by rediscovery cost, likelihood of incorrect changes, operational risk, and maintenance cost of the remedy. Recommend the next one to three changes with the greatest net leverage. Report existing strengths and what should remain unchanged.
