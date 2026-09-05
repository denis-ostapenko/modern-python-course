# Build a project of your own

4.1 · Plan 8 to 12 active hours, then allow time for review · New local repository

Choose a problem you can explain in one paragraph. The goal is to transfer the workflow, not rename Daybook variables line by line.

## Try: write journeys before source

Write three terminal journeys: add a valid record, reject invalid input, and produce a grouped summary. Include exact input, output, exit status, and whether data changes. Choose a data location. List one empty, one boundary and one failure case.

## Choose a brief

| Project | Three fields | Grouped result | Extra boundary |
| --- | --- | --- | --- |
| Reading Log | date, title, pages | Pages per title | Empty title or non-positive pages |
| Inventory Notes | date, category, quantity change | Net quantity per category | Decide and document whether negative stock is allowed |
| Expense Ledger | date, category, integer minor units | Minor units per category | Store money as integers; formatting is a separate step |
| Folder Report | relative name, extension, size | Bytes per extension | Read-only scan; skip symlinks and report unreadable files |

Reading Log has the closest transfer distance from Daybook. Folder Report adds filesystem concerns, so use its supplied scan helper and allow extra time. An original proposal is acceptable if it provides equivalent observable behavior.

## Understand the shared contract

Each project validates at least three meaningful fields, adds a record or observation, lists records in a documented order, filters by one field, totals by a group, and stores JSON locally. A missing file starts empty. Malformed JSON or invalid data produces a useful error without silently replacing the file.

Provide help and meaningful exit status. Keep calculation independent from command parsing and file access. Include useful type annotations. Use a dataclass if it clarifies your chosen record; if a dictionary is clearer, explain that choice rather than adding a class solely for points.

The executable assessment kit lives in `capstone/`. Copy it into a NEW folder with the provided helper:

```text
uv run python tools/new_capstone.py reading-project
```

The helper creates work/reading-project with its own instructions. It does not overwrite an existing project. Its starter is a Reading Log adaptation contract, with deliberate unimplemented functions. You may use its CLI and schema or adapt the tests to another chosen brief. Read the README before editing.

## Build: one independent behavior

Implement one input-to-result behavior yourself before accepting generated source. Add a failing test first, implement the behavior, and run the test. Record the data flow and the one part you found difficult.

Then add validation, persistence, filtering, summary and the CLI in small changes. [Milestones](02-milestones.md) gives the order. [The rubric](03-rubric.md) defines completion evidence.

## Verify

Run the assessment kit's tests against YOUR implementation, not the supplied reference project. Add at least one new normal, boundary and malformed-data case of your own. Run pytest, Ruff and Pyright. Reproduce the project from an extracted copy without copying .venv.

Complete one bounded agent-proposal review, using the stored flawed proposal if you do not have an agent. Use either live collaboration with another person or the labelled local review simulation. Save the exact scope, diff, checks, decision and recovery evidence.

## Fresh transfer after help

If you read a solution or use generated code for a difficult part, choose a different small behavior and implement it without that support. Record what you did independently. Help can move learning forward; it does not establish independence by itself.

## Handoff

A reader should be able to find the setup command, example journeys, data location, known limitations and recovery procedure without asking you. Include your tests and review decisions. Keep credentials, real financial records and private paths out of the example data.
