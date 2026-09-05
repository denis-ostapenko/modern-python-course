# Lists and records

1.3 · 55 to 70 minutes · Local workspace

Represent several records without inventing a variable for each one.

## Try

The starting copy is the previous input exercise. For this lesson, replace interactive input with the two sample records below, so the same data can be inspected repeatedly. Predict the second record's category and the first record's minutes.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-1.3-start lesson-1.3-attempt
uv run python work/lesson-1.3-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-1.3-complete/`.


## Understand

A list holds values in an order. Its first index is zero, the second is one. A dictionary associates keys with values, so a record can name its fields. In `entries[1]["category"]`, first select a list item, then select that dictionary's category.

Square brackets have two roles: a list literal when creating a list, and subscription when reading an existing value. Curly braces with key-value pairs create a dictionary. Colons separate keys from values; commas separate items.

`.append(...)` mutates the list by adding one item. Assigning to `entries[0]["minutes"]` mutates that dictionary. `.get("shelf", "unassigned")` reads a key with a fallback; direct brackets raise KeyError if it is missing. Use direct brackets for required fields and get when missing is an expected case.

Assigning one list to a second name does not copy its records. Keep intentional updates local and visible. [Sharp edges](../reference/sharp-edges/index.md) shows the shared-reference behavior.

```python
entries = [{"category": "reading", "minutes": 25}, {"category": "walking", "minutes": 40}]
print(entries[1]["category"])
print(entries[0]["minutes"])
```

Expected output:

```text
walking
25
```

## Build

Create a list of three Daybook records. Append a fourth. Change the minutes on one explicitly selected record and print it. Repair a lookup for a missing optional note using get.

For this exercise, selection is an index provided by the task. Searching for a matching record will use a loop in the next lesson.

## Independent practice

Set the selected index to a count of 9. Print its name, count and shelf separated by spaces; use unassigned when shelf is missing. The selected index is always valid. Index selection is supplied, so no search loop is needed yet.

Open `exercises/1.3/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 1.3
uv run python tools/check_exercise.py 1.3 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Print selected and inspect which record that index identifies.

</details>
<details><summary>Hint 2: narrow the change</summary>

Update items[selected], and use get with the stated fallback for shelf.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/1.3/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the inventory checks, including reordered items and a missing shelf. Explain why the list supplies order while each dictionary supplies named fields.

## Bring it back later

Before iteration, draw two records and trace entries[1]["minutes"] through the list and dictionary separately.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/1.3.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
