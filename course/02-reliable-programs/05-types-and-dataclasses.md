# Clear records and useful types

2.5 · 65 to 80 minutes · Local workspace

Give a record named fields and clarify function boundaries.

## Try

Compare entry["minutes"] with entry.minutes in the completed checkpoints. Identify which information an Entry annotation tells a reader, then identify which input rule it does not enforce.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-2.5-start lesson-2.5-attempt
uv run python work/lesson-2.5-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-2.5-complete/`.


## Understand

A class defines a kind of object. An instance is one object of that class; attributes are named values on it. `@dataclass` generates routine initialization and representation from field declarations. It avoids writing repetitive constructor code for a simple data record.

`category: str` and `minutes: int` are annotations. Python does not automatically reject an invalid value just because its annotation says int. The final make_entry function validates runtime data separately. A frozen dataclass prevents ordinary field reassignment, but it is not a general security mechanism.

`list[Entry]` describes a list of Entry objects; `dict[str, int]` maps strings to integers. A return annotation follows `->`. Pyright checks these relationships without running your example. Correct types do not guarantee the right business rule.

JSON does not directly encode an arbitrary dataclass instance. Convert it with asdict when saving; validate external dictionaries and construct Entry objects when loading. Keep those conversions at the storage boundary.

```python
from dataclasses import asdict, dataclass

@dataclass
class Entry:
    category: str
    minutes: int

print(asdict(Entry("reading", 25)))
```

Expected output:

```text
{'category': 'reading', 'minutes': 25}
```

## Build

Use the 2.5 checkpoint to replace dictionary field lookups with Entry attributes. Trace the JSON conversion in storage.py. Run the reference suite before and after reviewing the change.

The storage helper's temporary-file replacement is supplied infrastructure, not a new class exercise. Read its explanation in the patterns reference. In your independent task, use a small Book record and return its JSON-compatible dictionary.

## Independent practice

Return a dictionary containing title and pages from a Book dataclass. Inputs are already validated. Type hints do not validate runtime inputs.

Open `exercises/2.5/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 2.5
uv run python tools/check_exercise.py 2.5 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Which declared field disappears in the current returned dictionary?

</details>
<details><summary>Hint 2: narrow the change</summary>

asdict converts all dataclass fields into a dictionary.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/2.5/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the Book checks. Run `uv run pyright` on the reference. Explain the difference between an annotation, dataclass construction, and runtime validation.

## Bring it back later

Before the agent exercise, point to one invalid value a type checker can catch and one domain rule that still needs a runtime check.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/2.5.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
