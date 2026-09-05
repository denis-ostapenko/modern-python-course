# Daybook Course Instructions

## Purpose

This repository supports an adult-beginner Python course. Keep examples direct, readable, and limited to concepts already introduced by the current lesson.

## Scope

- Change only files named by the current lesson or task.
- Do not add a dependency unless the task explicitly requires and justifies it.
- Do not use network access for core Daybook behavior.
- Do not read or write outside this repository.
- Do not place credentials, personal paths, or private data in source, tests, output, or documentation.

## Commands

```text
uv sync
uv run python main.py
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```

## Definition of done

- Requested behavior is observable.
- Relevant tests pass.
- Ruff checks pass.
- Pyright passes after type hints are introduced.
- The complete diff contains no unrelated change.
- A beginner can explain every retained line.
