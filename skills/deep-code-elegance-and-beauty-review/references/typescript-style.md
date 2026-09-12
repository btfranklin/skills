# TypeScript Review Examples

Use these examples when the project contains TypeScript. Follow established project and framework conventions. Treat alternatives as conditional design choices, not universal rewrite rules.

## Arguments and Complete Calls

Before:

```typescript
sendReport(report, recipient, true, false);
```

After:

```typescript
sendReport(report, recipient, { archive: true, notify: false });
```

Reason: Named options make the two Boolean roles visible. Retain positional arguments for a few clear operands or an established external signature. Do not replace every parameter list with an options object.

## Functions, Methods, and Modules

Before:

```typescript
const label = new LabelFormatter().formatLabel(record);
```

After:

```typescript
const label = formatLabel(record);
```

Reason: A stateless operation can use a module function. A single named export can remove a class and repeated receiver context. Retain the class when it owns configuration, participates in a framework lifecycle, or fulfills a useful contract. Do not move system-dependent behavior onto a domain object merely to shorten calls. Use domain-specific modules instead of moving every function into a generic utility module.

## Domain States

Before:

```typescript
type Result = { loading: boolean; value?: Report; error?: Error };
```

After:

```typescript
type Result =
  | { status: "loading" }
  | { status: "ready"; value: Report }
  | { status: "failed"; error: Error };
```

Reason: A discriminated union makes the supported states explicit and helps callers narrow their data. Retain a simpler shape when fields are independent, stale data can coexist with loading or failure, or an external response contract requires it. Inspect actual states before recommending the union. Do not require classes for structural data.

## Asynchronous Effects

Before:

```typescript
function saveReport(report: Report): void {
  client.save(report);
}
```

After:

```typescript
function saveReport(report: Report): Promise<void> {
  return client.save(report);
}
```

Reason: When `client.save` returns `Promise<void>`, returning it lets callers observe completion and failure. If the wrapper adds no policy or useful boundary, consider deleting it and calling the client directly. Retain an intentional background operation when an owner handles its errors and lifetime. Preserve framework handler signatures. Do not add an `Async` suffix where return types and local conventions already communicate the operation.

## Sources and Scope

The TypeScript Handbook explains [object types](https://www.typescriptlang.org/docs/handbook/2/objects.html) and [narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html). Use those sources for language behavior. The API and structure examples here are conditional review guidance, not an official TypeScript style standard.
