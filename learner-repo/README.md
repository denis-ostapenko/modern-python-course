# Modern Python: learner workspace

Start with [the course](../course/index.md) or the website accompanying this download. Python 3.14 is the prepared default; the code supports Python 3.12 through 3.14.

Open this entire folder in VS Code. In Terminal > New Terminal:

```text
uv sync --frozen
uv run python main.py
uv run python tools/start_git.py
uv run python tools/check_environment.py
```

The first program prints `reading: 25 minutes`. The Git helper creates a local baseline only if none exists. It uses a local exercise identity for that one commit and does not change your global Git settings.

## Learn

Keep main.py as the first-run checkpoint. Later Daybook work belongs in fresh folders under work/:

```text
uv run python tools/checkpoint.py lesson-1.1-start values-attempt
uv run python work/values-attempt/main.py
uv run python tools/check_exercise.py 1.1 --extended
```

Independent tasks are in exercises/LESSON/answer.py. Their checks, explained solutions, and contracts are beside them. Record your explanation and review decisions in evidence/. That folder and work/ are excluded from Git by default; add individual exercise evidence deliberately when preparing a review.

## Verify the prepared reference

```text
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run pyright
```

The reference checks exclude deliberately broken starters. Run the lesson's explicit commands when testing your answer. See daybook/README.md for the complete CLI.

## Recovery

Use tools/checkpoint.py with a NEW destination to keep previous attempts. For the initial main.py only, inspect git diff, then git restore -- main.py if you want to discard that specific edit. Do not run broad reset or clean commands on personal work.

## Offline use

After the initial uv sync has cached Python and dependencies, use uv run --offline. The ZIP includes lesson text in course/ for offline reading. First installation needs internet or a pre-provisioned Python environment. Live GitHub collaboration needs internet and an account; the local review simulation is labelled separately.
