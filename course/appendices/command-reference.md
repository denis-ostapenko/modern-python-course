# Commands and where to run them

Commands below run in the learner repository root unless otherwise stated. In a terminal, the displayed working folder must contain pyproject.toml.

| Command | Purpose / expected result |
| --- | --- |
| `uv --version` | Show the installed uv version |
| `uv sync --frozen` | Install the declared locked environment |
| `uv run python main.py` | Print reading: 25 minutes from the baseline |
| `uv run python tools/start_git.py` | Create a local baseline if none exists |
| `uv run python tools/check_environment.py` | Verify tools, root, initial Git commit and starter output |
| `uv run python tools/checkpoint.py lesson-1.1-start values-attempt` | Copy into a new work/values-attempt folder; refuse overwrite |
| `uv run python tools/check_exercise.py 1.1 --extended` | Check your independent answer against all published cases |
| `uv run pytest` | Run stable reference tests |
| `uv run ruff check .` | Check configured source quality |
| `uv run ruff format --check .` | Inspect formatting without changing files |
| `uv run pyright` | Check the configured typed boundaries |
| `git status --short` | Inspect changed/untracked/staged state |
| `git diff` | Inspect unstaged changes |
| `git diff --staged` | Inspect the proposed commit |
| `git log -1 --oneline` | Show the current commit |

Run `uv run python daybook/main.py --help` for the complete application. Put --data before its add, list or summary subcommand.

Recovery and publication commands belong in their lessons because their safe meaning depends on the exact repository and file. Use a new checkpoint destination to preserve previous attempts. If uv is unavailable, follow [setup](../setup.md); do not remove your source to repair a tool installation.
