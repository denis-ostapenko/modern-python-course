# Specify a subtotal

Write tests in test_answer.py for an empty list and a normal list, observe red, then fix subtotal. Prices are non-negative integer minor units. The result is their sum. The course checker validates behavior; your red-before-green observation belongs in evidence/2.3.md.

Edit answer.py. Run the visible checks from the repository root:

```text
uv run python tools/check_exercise.py 2.3
uv run python tools/check_exercise.py 2.3 --extended
```

The first case is visible practice. Additional cases test the same stated rules with different data. These files are available locally, so they are not secret examinations. The checker substitutes only the declared input assignments in a temporary copy, or calls the named function. Your file remains unchanged.

If stuck, use the hints in the lesson. Open solution.py only after trying. Compare one decision, close it, and solve a fresh input without copying.
