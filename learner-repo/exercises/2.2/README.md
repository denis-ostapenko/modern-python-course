# Load a reading list

load_books(path) reads UTF-8 JSON and returns its list. A missing file is an empty list. Malformed JSON and non-list data must raise ValueError without changing the file.

Edit answer.py. Run the visible checks from the repository root:

```text
uv run python tools/check_exercise.py 2.2
uv run python tools/check_exercise.py 2.2 --extended
```

The first case is visible practice. Additional cases test the same stated rules with different data. These files are available locally, so they are not secret examinations. The checker substitutes only the declared input assignments in a temporary copy, or calls the named function. Your file remains unchanged.

If stuck, use the hints in the lesson. Open solution.py only after trying. Compare one decision, close it, and solve a fresh input without copying.
