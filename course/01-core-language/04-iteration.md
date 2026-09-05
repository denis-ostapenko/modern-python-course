# Loops and running totals

1.4 · 60 to 75 minutes · Local workspace

Process each record and keep a running result.

## Try

Trace a list of durations 25, 40 and 15 on paper. Start total at zero. Write its value after each item before executing the example.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-1.4-start lesson-1.4-attempt
uv run python work/lesson-1.4-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-1.4-complete/`.


## Understand

A `for` loop binds one item at a time to a name and executes the indented block. The sequence may be empty; then the block runs zero times. A running total, or accumulator, begins before the loop so each iteration can build on the previous value.

| Item | Previous total | New total |
| --- | --- | --- |
| 25 | 0 | 25 |
| 40 | 25 | 65 |
| 15 | 65 | 80 |

`total += minutes` means update total by adding minutes. Resetting total inside the loop destroys the earlier accumulation. A condition inside the loop can filter which items contribute.

For grouped totals, use a dictionary. Read `totals.get(category, 0)` to obtain the current total or zero for a new category, then assign the increased value. A second loop prints the groups. `range(3)` supplies 0, 1 and 2 when repetition is based on a count rather than existing records.

```python
total = 0
for minutes in [25, 40, 15]:
    total += minutes
    print(total)
```

Expected output:

```text
25
65
80
```

## Build

First total all Daybook minutes. Then group by category using a dictionary. Keep the initial empty dictionary outside the loop. Test no entries, one entry, and two entries with the same category.

Read the complete checkpoint only after your overall total works. It shows the two loops separately.

## Independent practice

Sum count only for sent orders. Empty input totals zero. Keep the accumulator across iterations.

Open `exercises/1.4/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 1.4
uv run python tools/check_exercise.py 1.4 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Use two matching orders; one order can hide an accumulator reset.

</details>
<details><summary>Hint 2: narrow the change</summary>

Remove the assignment that resets total inside the repeated block.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/1.4/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the dispatched-order checks. Explain what happens for an empty list and why the initial value belongs outside the loop.

## Bring it back later

At the next session, trace a filtered total for [2, 5, 3], counting only numbers greater than 2. Explain each intermediate value.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/1.4.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
