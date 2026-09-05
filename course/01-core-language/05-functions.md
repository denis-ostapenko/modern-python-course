# Functions and data flow

1.5 · 65 to 80 minutes · Local workspace

Give a reusable calculation explicit inputs and a returned result.

## Try

Read the example. Predict whether format_entry prints anything by itself. Identify the moment the returned text is actually printed.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-1.5-start lesson-1.5-attempt
uv run python work/lesson-1.5-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-1.5-complete/`.


## Understand

`def` defines a function. Its name is followed by parameters in parentheses and a colon. The indented body runs when the function is called. Arguments are the actual values passed at the call.

`return` sends a result to the caller and ends that call. `print` displays text but does not provide that displayed text as a returned result. A function that reaches its end without return produces None. This distinction lets a calculation serve a terminal command, a test, or another function.

Names assigned inside a function are local to that call. Pass required data through parameters rather than depending on changing global values. One function should have a coherent responsibility you can state in a sentence.

In the checkpoint, `.items()` yields each dictionary key and value together. `for category, minutes in totals.items()` unpacks each pair. The `if __name__ == "__main__"` guard runs main only when that file is launched as the entry script; importing it for tests will leave the guarded demonstration unrun.

```python
def format_entry(category, minutes):
    return f"{category}: {minutes} minutes"

result = format_entry("reading", 25)
print(result)
```

Expected output:

```text
reading: 25 minutes
```

## Build

Extract Daybook's category total and output formatting into functions. Keep input and print at the edge. Add a small assertion such as `assert format_total("walk", 2) == "walk: 2 minutes"` in a scratch test file. An assertion that is false raises AssertionError.

Repair a function that prints its result when its caller needs a return value. Test the return directly before reconnecting output.

## Independent practice

Return zero for zero items. Otherwise return a base cost of 5 plus 2 per item. Inputs are non-negative integers. Return the result without printing.

Open `exercises/1.5/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 1.5
uv run python tools/check_exercise.py 1.5 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

What value does the caller receive when the body only prints?

</details>
<details><summary>Hint 2: narrow the change</summary>

Handle zero explicitly, then return the formula for the remaining inputs.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/1.5/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the shipping-cost checks. Follow one argument from the call through the condition to the return. Explain why printing inside shipping would fail its contract.

## Bring it back later

Before adding files, write a two-input function from memory and demonstrate its return with both print and assert.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/1.5.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
