# Independent Reading Log

Implement reading.py. The supplied tests intentionally fail until you build the behavior. Do not copy Daybook line by line. Use the supplied cli.py as the interface scaffold and add at least three additional tests: a normal case, a boundary and a damaged-data case.

## Exact contract

- make_record(date, title, pages): return date, trimmed title and pages in a dictionary. Date must be an actual calendar date in YYYY-MM-DD form; title must contain text; pages must be a positive integer, excluding bool. Invalid input raises ValueError. Use datetime.date.fromisoformat for calendar validation and compare date.isoformat with the input to enforce the exact form.
- summarize(records): return total pages per title; empty input returns an empty dictionary.
- filter_records(records, title): exact title match in original order, without mutating the input list.
- load_records(path): UTF-8 JSON list, each record validated; missing file returns []; malformed JSON or invalid shape raises ValueError, preserving the original file.
- save_records(path, records): validate before saving; save an equivalent JSON list. Use a temporary file beside the destination and replacement so a failed write does not partly overwrite an existing file.

Run from this project folder:

```text
uv sync --frozen
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```

The first run is expected to fail. Record one failure, implement its behavior, and work in small steps. The prepared tests cover the domain and storage contract. Add CLI subprocess tests for help, valid add/list/filter/summary, invalid input and meaningful exit status. Add the CLI help and example commands to this README.

## Handoff evidence

Record your independently implemented behavior, design decisions, data location, test results, Git recovery, agent-proposal decision and collaboration route. Use live human review or label the local simulation. The course rubric is in the offline course reading archive.

## Other project choices

For Inventory Notes, replace pages with signed quantity changes and define stock policy. For Expense Ledger, use integer minor units and define display formatting separately. For Folder Report, use the supplied read-only scan helper and add tests for file errors and skipped symlinks. Adapt tests to the contract before implementation, preserving equivalent empty, boundary, persistence and CLI cases.

## Run the interface

After implementing reading.py:

```text
uv run python cli.py --data records.json add 2026-09-05 "A book" 12
uv run python cli.py --data records.json list
uv run python cli.py --data records.json list --title "A book"
uv run python cli.py --data records.json summary
```

The supplied test_cli.py checks help, add, list, filter, summary and failure paths. Add a journey that is not already covered.

Start a separate local history with git init -b main, set your chosen local identity, then stage only the project source, tests, README and environment files. Create a focused baseline commit. Never add .venv or private data. Use the workflow from the completed collaboration lesson when publishing your chosen capstone.
