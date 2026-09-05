# Keep control of an agent change

3.4 · 70 to 90 minutes · Local workspace

Delegate one bounded change and verify the complete proposal.

## Try

Read exercises/3.4/proposal.md before opening its review key. Underline the requested behavior, the unrelated behavior and the extra dependency. A live account is optional.

Start from a new working copy. Run these commands in the learner repository terminal:

```text
uv run python tools/checkpoint.py lesson-3.4-start lesson-3.4-attempt
uv run python work/lesson-3.4-attempt/main.py
```

If that destination already exists, choose another final folder name. Keep earlier attempts. The completed reference is `checkpoints/lesson-3.4-complete/`.


## Understand

A useful brief states current behavior, expected behavior, allowed files, prohibited changes, acceptance cases and verification commands. Generated code is a proposal. A confident explanation is not execution evidence.

Review every changed file and every dependency change. A passing normal case can hide a changed edge case, such as replacing interior spaces. Add a test that distinguishes the requested behavior from the proposal.

Scope should grow only with your ability to inspect it. For this exercise, allow only exercises/3.4/answer.py. No network calls, package installation, stored-data migration or unrelated cleanup is needed. Keep a Git checkpoint before any generated edit.

A sensible decision can be keep, narrow, revise or reject. Do not reject a correct change merely to satisfy a ritual. The stored proposal intentionally contains defects so you can practise a justified rejection.

```python
proposal = "A B".strip().lower().replace(" ", "-")
required = "A B".strip().lower()
print(proposal)
print(required)
```

Expected output:

```text
a-b
a b
```

## Build

Write this brief in evidence/3.4.md:

> Make clean_tag trim outer whitespace and lowercase text. Preserve interior spaces. Edit only exercises/3.4/answer.py. Add no dependencies and do not access the network or stored user data. Explain the diff and run both course-check modes.

Run the checks before editing. Make a focused Git checkpoint. Then either ask an installed coding agent to propose the change or use the supplied proposal. Predict the result for `A B`, inspect the proposed replacement, and narrow it to the contract. Run checks and inspect git diff before keeping the result.

Record which proposal you rejected and the exact input that demonstrates the problem. Restore your checkpoint once as a recovery exercise, then reapply only the accepted change.

## Independent practice

Trim outer whitespace and lowercase the tag. Preserve interior spaces. Use the stored proposal in proposal.md, identify the unwanted edit, and record why you reject it.

Open `exercises/3.4/answer.py`. Work from the contract rather than the Daybook reference. From the learner repository root:

```text
uv run python tools/check_exercise.py 3.4
uv run python tools/check_exercise.py 3.4 --extended
```

Both checks must pass. The additional cases vary only the published requirements. Their source is available in the download. Passing is useful evidence of behavior, not proof of understanding.

<details><summary>Hint 1: choose an observation</summary>

Use an input containing one interior space, not just outer whitespace.

</details>
<details><summary>Hint 2: narrow the change</summary>

Preserve the interior. Remove only the transformation that the contract did not request.

</details>
<details><summary>Solution and fresh transfer</summary>

Open `exercises/3.4/solution.py`. Compare your result with it and explain one decision. Close the solution, change one input to a new value, predict the result, and solve it again. Record that you used the solution; it is a route to learning, not a penalty.

</details>


## Verify and explain

Pass behavior checks, account for every changed file, preserve the pre-change commit and record your decision. Explain each retained line without asking the agent to explain it for you.

## Bring it back later

One week later, review the same proposal without your notes and write a fresh test that distinguishes it from the contract.

## Optional agent help

Ask: "Explain the current behavior and suggest one diagnostic input. Do not rewrite the program or change files." Run the proposed input yourself. Without an agent, use Hint 1 and the example above as the complete alternative. For lessons about collaboration, follow the more specific stored proposal and scope rules in the activity.

## Save your evidence

Keep your code in the working copy or exercise folder. Write the input, observed result, and your explanation in `evidence/3.4.md` using VS Code. Create the evidence folder if needed. When recording completion on the website, paste a concise summary of those observations. Local lessons are self-recorded; the website does not secretly inspect your computer or certify a live review.
