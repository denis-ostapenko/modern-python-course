# Files that survive a run

2.2 · 60 to 75 minutes · Local workspace

Save records and recover expected file failures.

## Try

Predict what loading a missing file, valid JSON list and malformed JSON will do. The independent check creates temporary files, so it cannot alter your real reading list.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-2.2-start lesson-2.2-attempt
uv run python work/lesson-2.2-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-2.2-complete/`.


## Understand

A path identifies a file. A relative path is resolved from the process working directory, which may differ from the script folder. `Path(__file__).resolve().parent` identifies the script's folder; the early checkpoint keeps practice data there. The final CLI accepts an explicit data path.

`read_text(encoding="utf-8")` reads text; `write_text` replaces a file's contents. JSON is a text representation of lists, dictionaries, strings, numbers, booleans and null. `json.loads` turns JSON text into Python data. `json.dumps` does the reverse. A Python object is not itself a saved file.

A missing file can reasonably mean a first run. Malformed JSON means existing data cannot be interpreted, so report it without overwriting it. Valid JSON can still have the wrong shape: `{}` is a dictionary, not the required list. Validate the shape after parsing.

The low-level equivalent uses `with path.open(encoding="utf-8") as file:`; the with block closes the file when it ends, including during an exception. For small files, read_text is simpler. The final reference uses a temporary file and replacement for safer writes; that helper is explained in [storage patterns](../reference/patterns/index.md).

```python
import json
text = json.dumps([{"title": "Água", "pages": 12}], ensure_ascii=False)
restored = json.loads(text)
print(restored[0]["title"])
print(restored == [{"title": "Água", "pages": 12}])
```

Expected output:

```text
Água
True
```

## Build

Use the 2.2 working copy to load entries, append a sample entry and save. Run twice and observe the count increase. Back up entries.json, replace it with malformed text, and confirm a useful error without automatic deletion. Restore your backup.

Keep the independent reading-list exercise focused on loading. Round-trip behavior belongs to the guided storage code and its reference tests.

## Independent practice

load_books(path) reads UTF-8 JSON and returns its list. A missing file is an empty list. Malformed JSON and non-list data must raise ValueError without changing the file.

Open `exercises/2.2/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 2.2
uv run python tools/check_exercise.py 2.2 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Handle the absent file separately from parsing an existing file.

</details>
<details><summary>Hint 2: narrow the change</summary>

Catch FileNotFoundError only. After json.loads, reject anything that is not a list.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/2.2/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the reading-list checks. Explain how a missing file differs from damaged data. Demonstrate that a failed load leaves its original bytes unchanged.

## Bring it back later

Before the CLI lesson, describe where a relative path would point if the terminal started in a different folder.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/2.2.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
