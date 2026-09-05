# A command another person can use

3.1 · 65 to 80 minutes · Local workspace

Turn tested behavior into a discoverable command-line program.

## Try

Run `uv run python daybook/main.py --help`. Before running add, list and summary, predict whether each command changes a file. Use the explicit demo data path in all examples.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-3.1-start lesson-3.1-attempt
uv run python work/lesson-3.1-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-3.1-complete/`.


## Understand

A CLI accepts arguments after a command. A positional argument is identified by position; an option has a name such as --data. argparse generates help, converts declared argument types, and rejects malformed command syntax.

Standard output carries normal results. Standard error carries diagnostics. Exit status zero signals success; nonzero signals failure to a calling script. argparse uses 2 for invalid command syntax. Daybook uses 1 for invalid data or file errors.

Keep parsing separate from decisions. main parses and routes commands, make_entry validates data, reporting calculates totals, and storage handles JSON. This lets tests exercise each boundary independently.

Daybook lists records in insertion order and prints summaries in sorted category order. It does not merge similar category spellings or handle concurrent writers. State limits so another person can predict behavior.

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
args = parser.parse_args(["3"])
print(args.number * 2)
```

Expected output:

```text
6
```

## Build

Run these from the learner repository root:

```text
uv run python daybook/main.py --data work/demo.json add reading 25
uv run python daybook/main.py --data work/demo.json add walking 40
uv run python daybook/main.py --data work/demo.json list
uv run python daybook/main.py --data work/demo.json summary
```

The --data option belongs before the subcommand. Repeating add creates another record. Try add with zero minutes and verify that the existing data remains unchanged. On macOS/Linux, inspect the last command status with `echo $?`; in PowerShell use `$LASTEXITCODE` immediately after the command.

Build the same interface in the 3.1 working copy, using the complete checkpoint only to compare decisions.

## Independent practice

Print twice the supplied integer. Keep argparse help. Invalid text must return status 2 and put an error on stderr; help returns status 0.

Open `exercises/3.1/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 3.1
uv run python tools/check_exercise.py 3.1 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Keep parsing intact and inspect the final arithmetic expression.

</details>
<details><summary>Hint 2: narrow the change</summary>

Multiply the parsed integer by two; let argparse handle help and invalid integers.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/3.1/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass all double-command cases. Demonstrate help, success and invalid input for Daybook. Explain why an error message alone is not enough for another program to detect failure.

## Bring it back later

Before collaboration, write one success and one failure journey without inspecting source. Use them as review acceptance criteria.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/3.1.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
