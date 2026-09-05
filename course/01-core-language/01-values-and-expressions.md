# Values and expressions

1.1 · 50 to 65 minutes · Local workspace

Build a useful label from text and a number.

## Try

Predict the output of `print(20 + 5)`, `print("20" + "5")`, and `print(25 / 5)`. Put those statements in a saved scratch.py file and run it. Bare expressions in a file do not print their results; use print explicitly.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-1.1-start lesson-1.1-attempt
uv run python work/lesson-1.1-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-1.1-complete/`.


## Understand

An expression is evaluated to produce a value. A value has a type: `int` for whole numbers, `float` for approximate numbers with fractions, `str` for text, and `bool` for True or False. `None` represents no value, rather than the text "None".

The same symbol can have a different meaning for different types. Adding integers adds quantities. Adding strings joins text. Python will not guess how to add a string and an integer: `"Minutes: " + 25` raises TypeError. A formatted string solves this presentation problem without changing the stored number.

Assignment binds a name to a value; it is not an equation to solve. `minutes = minutes + 5` first reads the previous value, adds five, and binds the result. Prefer meaningful names in lowercase with underscores.

Multiplication precedes addition. Parentheses make grouping explicit. `/` produces a float; `//` is whole-number floor division. Convert deliberately with `int("25")` or `str(25)`. `int("hello")` fails, which the next lesson handles.

```python
print(20 + 5)
print("20" + "5")
print(25 / 5)
print(type(25).__name__)
```

Expected output:

```text
25
205
5.0
int
```

## Build

In your Daybook working copy, create a variable named summary using an f-string, then print it. Change category and minutes independently. Repair `summary = category + minutes` by expressing the intended format.

Keep quantities numeric until presentation. Do not change minutes to text just to avoid understanding the error.

## Independent practice

Print exactly TITLE: DISTANCE km. Keep the title and km assignments as the two inputs. Support zero and Unicode text. Do not hard-code the complete output.

Open `exercises/1.1/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 1.1
uv run python tools/check_exercise.py 1.1 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Read the expected punctuation. Which pieces are inputs and which are fixed text?

</details>
<details><summary>Hint 2: narrow the change</summary>

Use an f-string with the two input names inside braces.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/1.1/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the route-label checks. Explain why the text and number examples differ. Predict the result for a route with zero kilometres before running.

## Bring it back later

At the start of lesson 1.3, reconstruct a label using a different name and number without reopening this example.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/1.1.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
