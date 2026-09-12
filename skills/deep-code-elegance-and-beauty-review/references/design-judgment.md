# Naming, Likely Change, and Subtraction

Use these questions on representative code. These are decision aids, not a requirement to find a problem in every area.

## Read the Complete Expression

Read names with the receiver, arguments, return value, and module context. Inspect actual callers as well as declarations. Include internal APIs, tests, and documentation.

- Identify the action, the affected concept, and each argument's role.
- Check whether the receiver already supplies words that the name repeats.
- Distinguish lookup, creation, conversion, mutation, and external effects. Check whether the name suggests behavior that the implementation does not provide.
- Use one term for one concept. Preserve established domain and framework terms.
- Check ownership before recommending a method move. Identify the state, policy, and lifecycle that the operation needs.
- Prefer natural expressions where the language supports them. Do not imitate English at the expense of local conventions or precise meaning.

For a meaningful naming recommendation, show a small before-and-after call. Explain the comprehension benefit. State when the current form remains appropriate. A shorter name is not sufficient evidence of improvement.

## Design for Likely Change

Assess whether the next maintainer can locate and express a likely change using the existing concepts.

1. Use a roadmap, recent changes, existing variants, or unresolved requirements to identify one or two plausible changes. Label reviewer assumptions. If there is no useful evidence, state that limit and assess current responsibilities.
2. Trace each change through the current design. Identify affected modules, repeated rules, hidden dependencies, and knowledge required from callers.
3. Distinguish normal coordinated edits from scattered responsibility. A new provider can reasonably require an adapter, registration, and tests. Changes to unrelated business rules can indicate that provider details have spread too far.
4. Compare the current design with a small adjustment. Assess comprehension now, expected change effort, and reversal cost. Do not count files or lines as a substitute for this reasoning.
5. Recommend a present improvement, retain the design, or name a concrete condition for a later change. Do not add mechanisms for unsupported possibilities.

Example: A roadmap requests another export format. The current CSV export function selects records and encodes them. Separate record selection from encoding if that gives both current responsibilities clear locations. Keep a plain encoding function. A registry and plugin discovery have no demonstrated benefit. Retain the combined function if selection is format-specific and separating it would obscure that relationship.

Aesthetic guidance can identify a clearer location for future work without claiming a defect. Do not present a hypothetical change as a documented requirement.

## Remove Unnecessary Concepts

Before proposing new code, consider deletion, consolidation, or an existing capability. Preserve required behavior and useful boundaries.

- Can a caller use the underlying operation directly instead of passing through a wrapper?
- Can a value be derived instead of stored and synchronized? Check snapshot semantics and measured computation cost first.
- Can one authoritative rule replace competing implementations? Similar text alone does not establish a shared rule.
- Can a language or library feature replace custom machinery?
- Does an option or abstraction serve a current requirement or an evidenced compatibility boundary?
- After removing a feature, which types, settings, tests, and documents lose their purpose?

For a subtraction recommendation, identify what disappears, what remains, and why the remaining design preserves required behavior. Identify the relevant callers and behavior checks. Do not remove a public interface, audit record, lifecycle boundary, or required extension point only to reduce code size.

Example: Three internal classes only forward an export call and add no policy or lifecycle behavior. Replace the forwarding chain with a call to the encoding function. The classes and forwarding tests disappear; encoding behavior tests remain. Retain a boundary that enforces authorization or translates provider errors. Do not combine tax and shipping rules only because their current arithmetic matches.

Prefer fewer concepts to maintain. Do not replace clear code with dense expressions, flag-driven generic helpers, or abstractions that make common calls harder to read.

## Source and Scope

The [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/) provide a useful principle: assess clarity at the point of use. Apply that principle without copying Swift syntax into another language. The likely-change and subtraction criteria here are review guidance for this skill, not official language rules.
