# Convert a typed record

Return a dictionary containing title and pages from a Book dataclass. Inputs are already validated. Type hints do not validate runtime inputs.

Edit answer.py. Run the visible checks from the repository root:

```text
uv run python tools/check_exercise.py 2.5
uv run python tools/check_exercise.py 2.5 --extended
```

The first case is visible practice. Additional cases test the same stated rules with different data. These files are available locally, so they are not secret examinations. The checker substitutes only the declared input assignments in a temporary copy, or calls the named function. Your file remains unchanged.

If stuck, use the hints in the lesson. Open solution.py only after trying. Compare one decision, close it, and solve a fresh input without copying.
