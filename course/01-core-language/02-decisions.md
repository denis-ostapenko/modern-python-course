# Input and decisions

1.2 · 55 to 70 minutes · Local workspace

Make a program choose a valid or invalid path.

## Try

Run the local input program three times, entering reading and then 30, 0, or hello as minutes. Predict which values can become positive whole numbers.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-1.2-start lesson-1.2-attempt
uv run python work/lesson-1.2-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-1.2-complete/`.


## Understand

`input("Minutes: ")` prints a prompt and returns the text typed before Enter. Even typing 30 produces text. `int(raw)` attempts numeric conversion. The supplied `try` block performs that attempt; `except ValueError` handles a conversion that cannot be made. For now, treat that small block as the prepared boundary. We will investigate exceptions directly in lesson 2.1.

A comparison produces True or False. `>` means greater than; `>=` also includes equality. `==` compares values; `=` assigns. `if` executes its indented block when the condition is true. `elif` offers another condition, and `else` handles the remaining path.

Indentation is part of Python syntax. Use four spaces for a block. `and` requires both conditions; `or` requires at least one. `.strip()` returns text with outer whitespace removed. An empty string is false in a condition, so `if category` checks whether any characters remain after trimming.

```python
minutes = 0
if minutes > 0:
    print("accepted")
else:
    print("rejected")
```

Expected output:

```text
rejected
```

## Build

Add category input and duration validation to Daybook. Use strip on category. Accept only a nonempty category and minutes greater than zero. Keep the supplied conversion handler and show one useful message for invalid input. Try a category containing only spaces.

Boundary cases surround a rule. For positive minutes, compare -1, 0 and 1. Testing only 30 cannot distinguish > from >=.

## Independent practice

Accept positive whole numbers, including surrounding whitespace. Reject zero, negatives, empty input, and non-numeric text. The conversion error handler is supplied; change the condition.

Open `exercises/1.2/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 1.2
uv run python tools/check_exercise.py 1.2 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Trace which value the supplied handler gives weight when conversion fails.

</details>
<details><summary>Hint 2: narrow the change</summary>

The boundary is strictly greater than zero, not greater than or equal to zero.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/1.2/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the parcel-weight checks. Explain why zero is rejected and how non-numeric text reaches the invalid path.

## Bring it back later

Before debugging in lesson 2.1, write down which three inputs you would choose to distinguish a conversion defect from a condition defect.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/1.2.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
