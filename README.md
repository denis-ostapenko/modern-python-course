# Modern Python

**From First Run to Reviewed Change · By Denis Ostapenko**

A practical English-language course for adult beginners. Run Python in the browser, move into VS Code and a prepared uv workspace, build a tested local application, and review changes with people and coding agents.

[Open the course](https://denis-ostapenko.github.io/modern-python-course/) · [Read the lessons](course/index.md) · [Local setup](course/setup.md)

## Included

- 17 milestones, full lessons, 14 independent exercise packages and 30 recovery checkpoints.
- First-run editor with a local Pyodide worker, fresh namespaces, current-source checks, timeout and recovery.
- Complete Daybook CLI, tests, JSON storage and typed records.
- Isolated Git conflict/review lab, deterministic agent proposals and capstone assessment starter.
- Optional CSV, API, notebook and agent practice, compact references and offline reading.
- Portable progress export/import and a complete downloadable workspace.

Local milestone records are learner attestations backed by checks run in their own project. Simulated review is labelled separately from live human review. The course does not issue an accredited certificate.

## Run locally

Use Node.js 24, Python 3.12 or later, and uv for learner verification.

```sh
cd app
npm ci
npm run build
npm run preview
```

Prebuild creates the catalog and downloads and copies the pinned Python runtime from npm. No live AI provider or API key is needed. Relative assets and hash-based lesson links support GitHub Pages.

## Verify

```sh
python3 scripts/validate_course.py
cd app
npm test
npm run build
cd ../learner-repo
uv sync --frozen
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```

GitHub Actions also checks exercise solutions and checkpoints and runs the learner suite across supported Python versions and operating systems. Deliberately incomplete answers are excluded from the stable reference suite.

## Files

course/ contains lessons and the manifest; app/ contains the site and runner; learner-repo/ contains downloadable practice; instructor/ contains authoring templates and an assessment reference; scripts/ contains build and validation tools.

Copyright 2026 Denis Ostapenko. Third-party components retain their own licenses.

Topics: python, beginner-course, programming-education, pytest, uv, git, coding-agents.
