# Syntax at a glance

Read forms here after their first lesson. This is a lookup, not a second learning path.

```python
name = "reading"
minutes = 25
if minutes > 0:
    print(f"{name}: {minutes}")

entries = [{"category": name, "minutes": minutes}]
for entry in entries:
    print(entry["category"])


def doubled(value):
    return value * 2

assert doubled(3) == 6
```

A colon starts an indented block after if, for and def. Four spaces are the course convention. Quotes delimit text; square brackets create a list or select an item; braces with key-value pairs create a dictionary.

| Form | Read it as |
| --- | --- |
| `a == b` | Compare values |
| `a = b` | Assign a name |
| `x in values` | Test membership |
| `record.get("key", default)` | Read an optional field |
| `for key, value in totals.items()` | Process dictionary pairs |
| `return result` | End the call with a value |
| `try` / `except ValueError` | Attempt an operation and handle one expected failure |
| `from pathlib import Path` | Import a named object |
| `def total(values: list[int]) -> int` | Annotated function boundary |

See [program shape](01-program-shape.md) and [dictionary forms](02-dictionaries.md).
