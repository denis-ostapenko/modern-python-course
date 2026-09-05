import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "main.py",
    "pyproject.toml",
    "uv.lock",
)
EXPECTED_OUTPUT = "reading: 25 minutes"


def check(condition: bool, success: str, failure: str) -> bool:
    print(f"{'PASS' if condition else 'FAIL'}: {success if condition else failure}")
    return condition


def main() -> int:
    results: list[bool] = []
    version = sys.version_info

    results.append(
        check(
            (3, 12) <= version[:2] < (3, 15),
            f"Python {version.major}.{version.minor} is supported",
            "Use Python 3.12, 3.13, or 3.14",
        )
    )
    results.append(
        check(
            Path.cwd().resolve() == PROJECT_ROOT,
            "the terminal is open at the project root",
            f"open the terminal in {PROJECT_ROOT.name}",
        )
    )

    for relative_path in REQUIRED_FILES:
        results.append(
            check(
                (PROJECT_ROOT / relative_path).is_file(),
                f"{relative_path} is available",
                f"{relative_path} is missing",
            )
        )

    results.append(
        check(
            shutil.which("uv") is not None,
            "uv is available",
            "uv is not available in this terminal",
        )
    )
    results.append(
        check(
            shutil.which("git") is not None,
            "Git is available",
            "Git is not available in this terminal",
        )
    )

    baseline = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )
    has_root = (
        baseline.returncode == 0
        and Path(baseline.stdout.strip()).resolve() == PROJECT_ROOT
    )
    head = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )
    results.append(
        check(
            has_root and head.returncode == 0,
            "local repository and initial commit are ready",
            "run uv run python tools/start_git.py in the extracted starter",
        )
    )

    run = subprocess.run(
        [sys.executable, "main.py"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )
    results.append(
        check(
            run.returncode == 0 and run.stdout.strip() == EXPECTED_OUTPUT,
            "Daybook produces the expected first output",
            "restore main.py from checkpoints/lesson-0.2-start",
        )
    )

    if all(results):
        print("READY: the Daybook workspace is ready for the course")
        return 0

    print("NOT READY: repair each FAIL item, then run this check again")
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired:
        print(
            "NOT READY: a command exceeded five seconds. Check for an unfinished loop."
        )
        raise SystemExit(1)
    except OSError as error:
        print(f"NOT READY: required command could not start: {error.strerror}")
        raise SystemExit(1)
