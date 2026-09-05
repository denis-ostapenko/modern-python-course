# Review and recover a change

3.2 · 60 to 75 minutes · Local workspace

Save one focused change and recover an unwanted edit.

## Try

Run git status --short and git diff from the learner repository. Identify the current branch with git branch --show-current. Do not discard files during inspection.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-3.2-start lesson-3.2-attempt
uv run python work/lesson-3.2-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-3.2-complete/`.


## Understand

The working tree contains current files. Staging chooses content for the next commit. A commit is a named snapshot of staged content. Untracked files are not yet in history; modified files differ from the current snapshot. `git diff` shows unstaged changes and `git diff --staged` shows the proposed commit.

A branch names a line of work. A small branch and a focused commit make review and recovery easier. A green test run does not justify including unrelated files.

`git restore -- file` replaces an unstaged file with its index version. When nothing is staged for that file, that is normally the current committed baseline. Inspect status first. `git restore --staged -- file` changes the staging area while keeping the working edit. Avoid broad reset and clean commands in this course.

```python
original = " Reading "
normalized = original.strip().lower()
print(normalized)
```

Expected output:

```text
reading
```

## Build

1. Complete the label exercise and run its checks.
2. If needed, set a local exercise identity: `git config user.name "Course Learner"` and `git config user.email "learner@example.invalid"`. Use your chosen identity for a public project later.
3. Run `git switch -c practice/label`.
4. Create an unrelated notes.txt file in the root. Keep it untracked for this exercise.
5. Inspect `git diff -- exercises/3.2/answer.py`, then stage only that file with `git add exercises/3.2/answer.py`.
6. Inspect `git diff --staged`, rerun the exercise check, and commit with `git commit -m "Normalize display labels"`.
7. Make a separate unwanted edit in answer.py. Inspect it, then `git restore -- exercises/3.2/answer.py`.
8. Verify your label still works and notes.txt still exists.

If the branch name already exists, choose a new practice name. Keep the commit hash from `git log -1 --oneline` in your evidence.

## Independent practice

Return trimmed lowercase text. Complete the Git recovery exercise in the lesson as separate evidence. Passing this behavior check alone does not establish Git competence.

Open `exercises/3.2/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 3.2
uv run python tools/check_exercise.py 3.2 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Inspect what strip and lower each change independently.

</details>
<details><summary>Hint 2: narrow the change</summary>

Chain the two text transformations and return the resulting string.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/3.2/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass behavior checks and demonstrate the actual Git recovery. Record the commit, reviewed files, recovery command and survival of notes.txt. A course checkbox cannot substitute for these observations.

## Bring it back later

At the next session, inspect a diff before reading a lesson. Explain what would enter a commit and what would remain outside it.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/3.2.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
