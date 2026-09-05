# Repair a boundary conversion

Return a non-negative integer for valid text, including surrounding whitespace; return None for negatives or non-numeric text. Before repairing, record the failing input, exception, inspected value, and hypothesis in evidence/2.1.md.

Edit answer.py. Run the visible checks from the repository root:

```text
uv run python tools/check_exercise.py 2.1
uv run python tools/check_exercise.py 2.1 --extended
```

The first case is visible practice. Additional cases test the same stated rules with different data. These files are available locally, so they are not secret examinations. The checker substitutes only the declared input assignments in a temporary copy, or calls the named function. Your file remains unchanged.

If stuck, use the hints in the lesson. Open solution.py only after trying. Compare one decision, close it, and solve a fresh input without copying.
