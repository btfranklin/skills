# Design for Likely Change

Use this guide for structural and maintenance assessment. Report current harm as a finding. Report a supported future weakness as a future risk. Clearer phrasing alone belongs in an elegance review.

## Assess a Concrete Change

1. Find evidence in the roadmap, recent changes, existing variants, or unresolved requirements. Separate documented plans from assumptions.
2. Select one or two likely changes that exercise the boundaries in scope. Do not invent requirements to justify a preferred architecture. If evidence is absent, state that limit.
3. Trace the required edits through the current design. Identify repeated rules, exposed implementation details, state owners, and unrelated responsibilities that must change together.
4. Compare the current design with the smallest useful correction. Include its present implementation cost and maintenance cost. Consider how easily each choice can be reversed.
5. Recommend a correction now, retention of the current design, or a concrete condition for later work. Do not implement the hypothetical feature during review.

File count alone is not evidence of poor structure. An adapter, registration entry, and tests can be coherent parts of one change. Repeated provider conditions in unrelated business rules can indicate a broken boundary.

## Inspect Names as Contracts

Read representative calls with their receivers, arguments, return values, and surrounding control flow. Inspect the implementation before attributing ownership or effects to a name.

- Does the name imply lookup when the operation creates or persists data?
- Does one domain concept have conflicting names across boundaries?
- Does a generic operation combine different policies that callers must distinguish?
- Does moving a method place required state, configuration, and policy under the correct owner?

Show a small before-and-after example when it explains a recommendation. Explain the specific misuse, repeated maintenance work, or contract conflict. Do not rank a naming preference as a defect. Preserve established framework conventions unless they cause a demonstrated problem.

## Test Removal Before Addition

Before proposing new machinery, test deletion, consolidation, derivation, or an existing language or library capability.

- Can callers use the underlying operation without a forwarding layer?
- Can one authoritative rule replace implementations that must change together?
- Can a value be derived instead of stored and synchronized?
- Do configuration options and extension mechanisms serve actual callers?
- After a feature is removed, which types, settings, tests, and documents have no remaining purpose?

For each removal, identify what disappears, what remains, and why required behavior survives. Check callers and external or persisted contracts. Name behavior checks for accepted fixes. Preserve authorization, transactions, retries, resource cleanup, and other useful boundaries.

Prefer fewer concepts to maintain. Do not optimize for line count. Keep similar code separate when the policies differ or change independently. Do not replace readable code with dense expressions or a helper with many mode flags.

## Conditional Examples

### Another Export Format

Evidence: the roadmap names a second format. The current function selects records and encodes CSV.

Before:

```python
export_csv(query, destination)
```

Possible correction inside the existing workflow:

```python
records = select_records(query)
write_csv(records, destination)
```

This separation gives encoding a clear location. Keep a streaming iterator when the current implementation streams records. Preserve snapshot and resource lifetime requirements. Do not add a registry or plugin discovery for an unimplemented format.

Retain the current function if selection is specific to CSV and the split would only forward arguments. A planned format does not prove that all selection behavior is shared.

### A Misleading Mutation

Before:

```typescript
const account = await accounts.get(email);
```

The implementation inserts an account when no match exists. Callers use it for read-only eligibility checks.

Possible correction:

```typescript
const account = await accounts.findByEmail(email);
```

Keep creation in an explicit operation for callers that need it. A rename to `getOrCreate` alone does not repair a read-only caller that still creates data. Verify both the caller contract and the behavior.

Retain `get` when the established interface defines it as lookup and the implementation only retrieves data. Do not impose a universal verb list on framework APIs.

### Forwarding Layers

Before: `ExportService.run` calls `ExportManager.run`, which calls `write_csv`. Neither wrapper adds policy, state, instrumentation, or an external contract.

After: the workflow calls `write_csv` directly. The forwarding classes and tests that only assert forwarding can disappear. Preserve tests for exported content and failures.

Retain a layer that enforces authorization or owns a transaction. Similar syntax does not make that boundary unnecessary.

### Repeated Policy or Separate Policy

Before: three checkout paths independently calculate the same documented discount rule.

After: those paths call one `calculate_discount` function. A policy change has one implementation location.

Retain separate functions for a tax rate and a discount rate even when their arithmetic matches today. They have different authorities and reasons to change. Combining them behind a mode flag hides that distinction.

### Derived State

Before: an in-memory batch stores both `items` and `item_count`. Several mutation paths must update both.

After: callers use `len(batch.items)`. The count field and its update paths disappear.

Retain a stored count when it represents a historical snapshot or a justified aggregate over unloaded records. Verify meaning and access cost before recommending derivation.
