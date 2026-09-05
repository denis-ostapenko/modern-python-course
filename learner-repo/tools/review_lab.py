import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(
        description="Create an isolated Git conflict and review lab"
    )
    parser.add_argument("name")
    args = parser.parse_args()
    if Path(args.name).name != args.name or args.name in {".", ".."}:
        parser.error("Use a new folder name without slashes")
    work = ROOT / "work"
    if work.is_symlink():
        parser.error("work must not be a symlink")
    work.mkdir(exist_ok=True)
    folder = work / args.name
    if folder.exists():
        parser.error("Destination exists. Choose a new name")
    folder.mkdir()

    def git(*values):
        return subprocess.run(
            ["git", *values], cwd=folder, check=True, capture_output=True, text=True
        )

    def code(text):
        (folder / "average.py").write_text(text, encoding="utf-8")

    git("init", "-b", "main")
    git("config", "user.name", "Course Learner")
    git("config", "user.email", "learner@example.invalid")
    code("def average(values):\n    return sum(values) / len(values)\n")
    (folder / "test_average.py").write_text(
        "from average import average\n\ndef test_empty():\n    assert average([]) == 0\n\ndef test_rounded():\n    assert average([1, 1, 2]) == 1.33\n",
        encoding="utf-8",
    )
    (folder / ".gitignore").write_text(
        "__pycache__/\n.pytest_cache/\n", encoding="utf-8"
    )
    git("add", ".")
    git("commit", "-m", "Add an average and its desired behavior")
    git("switch", "-c", "empty-input")
    code(
        "def average(values):\n    if not values:\n        return 0\n    return sum(values) / len(values)\n"
    )
    git("add", "average.py")
    git("commit", "-m", "Handle empty input")
    git("switch", "main")
    git("switch", "-c", "rounded-output")
    code("def average(values):\n    return round(sum(values) / len(values), 2)\n")
    git("add", "average.py")
    git("commit", "-m", "Round displayed averages")
    git("switch", "empty-input")
    instructions = """# Local review simulation

This is a prepared local repository. No remote PR or human review has occurred.
From the learner root, run:

    git -C work/NAME merge rounded-output

A conflict in average.py is expected. Open it in VS Code. The stored review asks:
'Please preserve the empty-list behavior and the rounded nonempty result. Show
an input proving each behavior before merging.'

Resolve the marked block into a function with an early return of zero and a
rounded result for nonempty input. Remove every conflict marker. Then run:

    uv run pytest work/NAME/test_average.py
    git -C work/NAME add average.py
    git -C work/NAME commit -m "Combine empty-input and rounding behavior"
    git -C work/NAME status --short
    git -C work/NAME log -1 --oneline

If you want to abandon this uncommitted merge, git -C work/NAME merge --abort
returns to its pre-merge state. Use it only in this isolated exercise repository.
Record the comment, both behaviors, final test results and merge commit. Label
it local review simulation. For a fresh attempt, generate a different folder.
""".replace("NAME", args.name)
    (folder / "REVIEW.md").write_text(instructions, encoding="utf-8")
    print(f"Created work/{args.name}. Open REVIEW.md there.")


if __name__ == "__main__":
    main()
