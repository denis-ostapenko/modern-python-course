# Modules and a reproducible project

2.4 · 65 to 80 minutes · Local workspace

Split responsibilities without changing behavior.

## Try

Assign calculation, file loading and terminal output to three named files. Then copy the 2.4 checkpoint. Read its imports before running it. Missing entries.json is an empty first run, so no output is expected until you supply records.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-2.4-start lesson-2.4-attempt
uv run python work/lesson-2.4-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-2.4-complete/`.


## Understand

A module is an importable Python file. `from reporting import totals_by_category` imports a named function. Imports normally execute the module's top-level code once per process, which is why demonstration code belongs under an entry guard.

Keep dependency direction simple: main calls storage and reporting; reporting does not call main. A circular design makes initialization harder to follow. Use names such as storage.py rather than json.py, which would shadow the standard library.

`pyproject.toml` declares the project's requirements. `uv.lock` records the resolved versions. `.python-version` selects the prepared Python series. `.venv` is generated and should not be committed. `uv sync --frozen` installs from the lock and refuses to silently update it.

A clean reproduction starts from the declared files, not your existing environment. Extract a second starter copy, run frozen sync there, and run the reference checks. Keep the first copy intact.

```python
from pathlib import Path

path = Path("notes") / "entries.json"
print(path.name)
print(path.suffix)
```

Expected output:

```text
entries.json
.json
```

## Build

Create entries.json beside the 2.4 working main.py with `[{"category": "reading", "minutes": 25}]`. Run the script and expect reading: 25 minutes. Inspect which module reads the path and which computes the total.

For the independent task, remove the unwanted file write from a calculation. Then put your own total_pages function in a reporting module in a new scratch folder and import it from a small caller. No extra dependency is needed.

## Independent practice

Return the sum of page counts without printing or writing a file. The checker executes in an isolated empty folder and rejects filesystem side effects. In the guided project, put this kind of calculation in reporting.py, not storage.py.

Open `exercises/2.4/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 2.4
uv run python tools/check_exercise.py 2.4 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

A total function should return its result without creating a file.

</details>
<details><summary>Hint 2: narrow the change</summary>

Remove the I/O and its unused import. File storage belongs to a caller or separate boundary.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/2.4/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass the pure-calculation checks and reproduce the prepared reference from a second extracted copy. Explain why copying .venv is unnecessary.

## Bring it back later

Before type annotations, draw main, storage and reporting with arrows for actual imports. Check that no arrow returns to main.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/2.4.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
