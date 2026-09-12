# Python Review Examples

Use these examples when the project contains Python. Follow established project and framework conventions. Treat alternatives as conditional design choices, not universal rewrite rules.

## Receiver and Ownership

Before:

```python
system.serialize_agent_input(agent, "input")
```

After, when the system owns serialization policy:

```python
system.serialize_input_for_agent(agent, "input")
```

After, when the agent owns the required behavior and state:

```python
agent.serialize_input("input")
```

Reason: The complete call communicates the argument relationship or the operation's owner. Inspect policy dependencies before selecting a receiver. Retain the original spelling when an established public contract or consistent domain term makes a rename more costly than its benefit. Report that constraint; do not invent a compatibility layer.

## Argument Roles

Before:

```python
copy_records(source, target, True)
```

After:

```python
copy_records(source, target, overwrite=True)
```

Reason: The keyword explains the Boolean at the call site. Consider a keyword-only parameter when designing the signature. Retain positional arguments for familiar, unambiguous operands. Do not add a configuration class for one option.

## Effects and Data

Before:

```python
report.contents  # Performs a network request.
```

After:

```python
report.fetch_contents()
```

Reason: An explicit operation makes remote work easier to see. Retain a property for ordinary stored or inexpensive derived data, or when a framework contract requires it. Do not infer caching or freshness from the verb alone.

## Functions and Resource Ownership

Before:

```python
result = SlugFormatter().format(title)
stream = open(path, "w")
try:
    write_result(stream, result)
finally:
    stream.close()
```

After:

```python
result = format_slug(title)
with open(path, "w") as stream:
    write_result(stream, result)
```

Reason: A stateless operation can use a plain function. A context manager makes resource lifetime local. Preserve actual modes and encoding during a real change. Retain a class when it owns reusable configuration or fulfills a required protocol. Retain explicit cleanup when resource lifetime crosses the block boundary.

Use a dataclass or typed model when named fields clarify a meaningful data shape. Keep a simple scalar or tuple when the role is already clear. Do not add types, classes, or wrappers only to demonstrate language features.

## Source and Scope

Use [PEP 8](https://peps.python.org/pep-0008/) for Python naming conventions and consistency guidance. The ownership and structure examples here are conditional review guidance. They are not additional PEP 8 requirements.
