# Tests that can catch a defect

2.3 · 65 to 80 minutes · Local workspace

Turn a behavioral expectation into a repeatable check.

## Try

Open exercises/2.3/test_answer.py. Predict which assertion fails before running `uv run pytest exercises/2.3/test_answer.py`. The supplied tests are a worked starting point; add one boundary case yourself before repairing answer.py.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-2.3-start lesson-2.3-attempt
uv run python work/lesson-2.3-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-2.3-complete/`.


## Understand

pytest discovers files named test_*.py and functions named test_*. An assertion compares an observed value with an expected one. A useful test arranges inputs, calls behavior, and asserts an outcome. Test the contract rather than private variable names.

A test that never fails for the intended defect is weak evidence. Observe red first, make a focused repair, and observe green. Add an empty-input case because a normal case alone can miss assumptions about the first item.

Ruff format makes layout consistent. Ruff check finds selected code issues. Neither proves the program computes the right result. Pyright checks type relationships later. Treat these as complementary evidence.

The prepared reference suite deliberately excludes incomplete exercises. Run the explicit exercise test command while learning; use `uv run pytest` for the stable Daybook reference.

```python
def subtotal(prices):
    return sum(prices)

assert subtotal([3, 4]) == 7
assert subtotal([]) == 0
print("Two behavior checks passed")
```

Expected output:

```text
Two behavior checks passed
```

## Build

Repair subtotal after recording its failing test. Add a case with zero and several prices. In a separate 2.3 checkpoint folder, isolate the reporting function and write a grouped-total test. This practice branch temporarily leaves storage aside; 2.4 brings the responsibilities together as modules.

Run `uv run ruff check exercises/2.3/answer.py` and `uv run ruff format --check exercises/2.3/answer.py`. If formatting differs, run the same command without --check to apply formatting to that file.

## Independent practice

Write tests in test_answer.py for an empty list and a normal list, observe red, then fix subtotal. Prices are non-negative integer minor units. The result is their sum. The course checker validates behavior; your red-before-green observation belongs in evidence/2.3.md.

Open `exercises/2.3/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 2.3
uv run python tools/check_exercise.py 2.3 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Compare the returned total with the mathematical sum, including empty input.

</details>
<details><summary>Hint 2: narrow the change</summary>

Remove the unconditional extra amount; preserve the test that exposed it.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/2.3/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass pytest for the exercise and both course-check modes. Record what failed before the repair. Explain one thing these tests do not prove.

## Bring it back later

At the start of modules, run this test without rereading the lesson. Explain why the same test should survive moving a calculation into another file.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/2.3.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
