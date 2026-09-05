# Debug from evidence

2.1 · 60 to 75 minutes · Local workspace

Find the cause of a failure before changing the program.

## Try

Run `uv run python tools/check_exercise.py 2.1 --extended` before editing. Record the hello input and its exception. Open the answer in VS Code and place a breakpoint on int(raw). Use Run and Debug > Debug current Python file; use a scratch caller if necessary to call parse_count("hello").

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-2.1-start lesson-2.1-attempt
uv run python work/lesson-2.1-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-2.1-complete/`.


## Understand

A syntax error prevents Python from parsing source. An exception interrupts a running operation. A wrong result can occur with no exception at all. These failures require different observations.

A traceback lists the chain of calls leading to failure. Read the final exception type and message, then find the nearest relevant source line in your own code. Do not edit an internal library just because it appears first.

At a breakpoint, the highlighted line is about to execute. Variables shows current values; Call Stack shows how this call was reached. Step Over executes the current line. Continue runs until the next breakpoint or completion. In the Debug Console, inspect raw and type(raw).

Use a repeatable loop: reproduce, form two possible explanations, observe a value that distinguishes them, repair, and rerun the original failing case. Catch an exception only where the program can respond meaningfully. Broad `except Exception` can hide programming defects.

```python
try:
    number = int("hello")
except ValueError:
    print("Enter a whole number")
```

Expected output:

```text
Enter a whole number
```

## Build

Create a scratch caller containing `from answer import parse_count` and `print(parse_count("hello"))` beside the exercise answer. Observe raw before conversion. Record why the input cannot become an integer. Add precise ValueError handling, then reject negative integers separately.

In Daybook, put numeric conversion in parse_minutes. Keep positive-minutes policy explicit. Restore a new checkpoint folder if experimental edits become confusing.

## Independent practice

Return a non-negative integer for valid text, including surrounding whitespace; return None for negatives or non-numeric text. Before repairing, record the failing input, exception, inspected value, and hypothesis in evidence/2.1.md.

Open `exercises/2.1/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 2.1
uv run python tools/check_exercise.py 2.1 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Distinguish int failing from int succeeding with a negative result.

</details>
<details><summary>Hint 2: narrow the change</summary>

Catch ValueError around the conversion, then test the converted integer.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/2.1/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass all parse_count cases. Keep your before-repair observation, not just the final working code. Explain which hypothesis the observed value ruled out.

## Bring it back later

At the start of tests, recreate one failing input from this lesson without looking at your notes and name the observation you would inspect.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/2.1.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
