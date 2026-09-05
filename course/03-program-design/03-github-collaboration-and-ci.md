# An issue, a review and a merge

3.3 · 90 to 120 minutes · Local workspace

Make intent, evidence and a decision visible to another reader.

## Try

Read exercises/3.3/README.md. Write an issue: average([]) fails, but the contract requires zero. Acceptance criteria include empty, one-item and multi-item input. Decide whether you will use a live human reviewer or the local simulation below.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-3.3-start lesson-3.3-attempt
uv run python work/lesson-3.3-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-3.3-complete/`.


## Understand

A remote repository is a shared copy. Clone obtains a local copy; fetch updates your knowledge of remote history; push sends commits; pull fetches and integrates changes. A pull request proposes merging a branch and presents its diff for review.

CI runs checks on a separate machine. A green status means those configured checks passed on that revision. It does not establish that someone reviewed the behavior. After a revision, wait for checks on the new commit.

A conflict occurs when Git cannot automatically combine changes. The marked regions show the competing versions; they are not valid final source. Read both intentions, edit a coherent result, remove conflict markers, run checks, stage the resolution and finish the merge.

There are two distinct records: **live collaboration**, which requires another person's review, and **local review simulation**, which develops workflow skills without claiming another person participated. Either can complete the course practice route; only the first earns the live-collaboration evidence designation.

```python
def average(values):
    if not values:
        return 0
    return sum(values) / len(values)

print(average([]))
print(average([2, 4]))
```

Expected output:

```text
0
3.0
```

## Build

### Live route

Create your own GitHub repository and push the learner branch using GitHub's displayed instructions. Use your chosen public commit identity. Enable Actions. In .github/workflows/checks.yml, add the command `uv run python tools/check_exercise.py 3.3 --extended` so CI checks the changed exercise as well as the reference.

Create a new branch, fix average, commit, push, and open a pull request linked to your issue. Ask a colleague or study partner to review the diff and the empty-input rule. Respond to one comment with a revision or a reasoned explanation. Wait for checks on the final commit before merging. Save the issue, PR, review decision and final commit links.

### Local simulation

Run `uv run python tools/review_lab.py review-attempt`. It creates a NEW isolated repository in work/review-attempt with two conflicting branches, a failing test and a stored review. Open its REVIEW.md and follow it. The helper never merges into your learner repository and refuses an existing destination.

The stored comment asks you to combine empty-input handling with rounding to two decimals. Resolve the conflict, run its tests, commit, and record why both behaviors remain. Run the learner reference suite too. Label your evidence **local review simulation**.

### Independent behavior

Repair average in exercises/3.3/answer.py and run both check modes. This task keeps its original contract: no rounding is required there.

## Independent practice

Return the arithmetic mean, or zero for an empty list. Complete live review or the explicitly labelled local simulation as described in the lesson. Behavior alone is not collaboration evidence.

Open `exercises/3.3/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 3.3
uv run python tools/check_exercise.py 3.3 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

What operation is invalid when the list length is zero?

</details>
<details><summary>Hint 2: narrow the change</summary>

Return zero before attempting division.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/3.3/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Keep either the live artifacts or the local simulation commit, resolved file and stored-review decision. Explain the final combined behavior. Never label stored comments as an actual human review.

## Bring it back later

In the capstone, write the issue and tests before opening an agent. Name which evidence requires another human and which you can produce independently.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/3.3.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
