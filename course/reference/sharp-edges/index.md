# Behaviors that can surprise you

## Names do not copy objects

```python
first = [1, 2]
second = first
second.append(3)
assert first == [1, 2, 3]
```

Both names refer to the same list. A shallow copy with list.copy creates a new outer list, but nested dictionaries may still be shared. Prefer explicit ownership and intentional updates before adding copying as a reflex.

## Text is not a number

`"20" + "5"` is `"205"`; `20 + 5` is 25. Convert deliberately. `input` always returns text.

## Empty loops still need a result

A loop over [] executes zero times. Initialize totals before it. Do not rely on a loop variable existing afterward.

## No return means None

```python
def announce():
    pass

assert announce() is None
```

pass is an empty statement, useful while scaffolding a block. Printing a result also does not return that displayed value to the caller.

## Approximate arithmetic

```python
assert 0.1 + 0.2 != 0.3
```

Binary floating-point cannot represent every decimal fraction exactly. For the capstone Expense Ledger, use integer minor units. For measured float results in tests, pytest.approx can express a justified tolerance.

## Other boundaries

- Relative paths depend on the terminal's working directory.
- Importing a module executes its top-level statements once per process.
- Mutable default arguments are created once at function definition, not anew for every call. Use None and create a fresh collection inside when necessary.
- Type annotations and dataclasses do not automatically validate external data.
- bool is a subclass of int. When the contract requires a whole quantity and excludes true/false, use an explicit validation rule such as type(value) is int.
- Catching every exception can turn a programming error into misleading success.

Read the original exception and choose one diagnostic observation before changing source.
