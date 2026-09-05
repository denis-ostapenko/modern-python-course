# Small problem-solving patterns

## Validate, then calculate

Convert external text at the input boundary. Handle the expected conversion failure there, then pass a validated value to a calculation. Avoid repeating input prompts inside reusable functions.

```python
def positive_minutes(raw):
    try:
        value = int(raw)
    except ValueError:
        return None
    return value if value > 0 else None

assert positive_minutes(" 3 ") == 3
assert positive_minutes("bad") is None
```

The conditional expression in the return selects one of two values. In early lessons you can write the same rule as an ordinary if block.

## Accumulate by category

Initialize the result once. Read the previous group total with a zero fallback. Store its new value.

```python
totals = {}
for category, minutes in [("read", 2), ("walk", 3), ("read", 4)]:
    totals[category] = totals.get(category, 0) + minutes
assert totals == {"read": 6, "walk": 3}
```

## Keep calculation independent

A reporting function accepts records and returns a result. Its caller chooses whether to print, save, or test that result. A report that writes an unexpected file is harder to reuse and test.

## Safer storage replacement

The final Daybook storage helper validates input, serializes it before touching the destination, writes a temporary file beside that destination, closes it, then calls os.replace. The finally block removes a leftover temporary file if replacement fails. Creating the temporary file in the same directory avoids a cross-filesystem rename.

This reduces the chance of replacing useful data with a partly written JSON document. It does not coordinate concurrent writers or guarantee survival of every hardware failure. The course application supports one writer at a time.

## Focused change

Write expected behavior, observe a failing check, save a Git checkpoint, make the smallest sufficient change, inspect the whole diff, and rerun relevant checks. Keep unrelated work outside the commit.

## Search without mutation

Loop over records and select matches into a new list. Do not remove items from the collection currently being iterated. Test empty input, no match and repeated matches.
