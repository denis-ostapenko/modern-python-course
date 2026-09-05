import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(args, cwd, expected=0):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=False, timeout=45)
    if result.returncode != expected:
        raise RuntimeError(f"{' '.join(args)}\n{result.stdout}\n{result.stderr}")
    return result


def main():
    with tempfile.TemporaryDirectory() as temporary:
        learner = Path(temporary) / "learner"
        shutil.copytree(ROOT / "learner-repo", learner, ignore=shutil.ignore_patterns(".venv", "work", "evidence", "__pycache__", ".pytest_cache", ".ruff_cache", ".git"))
        # Use the calling verified interpreter while exercising a clean file tree.
        run([sys.executable, "tools/start_git.py"], learner)
        run([sys.executable, "tools/check_environment.py"], learner)
        first = run(["git", "rev-parse", "HEAD"], learner).stdout
        run([sys.executable, "tools/start_git.py"], learner)
        assert run(["git", "rev-parse", "HEAD"], learner).stdout == first
        run([sys.executable, "tools/checkpoint.py", "lesson-1.4-start", "attempt"], learner)
        run([sys.executable, "tools/checkpoint.py", "lesson-1.4-start", "attempt"], learner, expected=2)
        run([sys.executable, "tools/review_lab.py", "review"], learner)
        lab = learner / "work/review"
        merge = run(["git", "merge", "rounded-output"], lab, expected=1)
        assert "CONFLICT" in merge.stdout
        (lab / "average.py").write_text("def average(values):\n    if not values:\n        return 0\n    return round(sum(values) / len(values), 2)\n", encoding="utf-8")
        run([sys.executable, "-m", "pytest", "-q"], lab)
        run(["git", "add", "average.py"], lab)
        run(["git", "commit", "-m", "Resolve the review practice"], lab)
        run([sys.executable, "tools/new_capstone.py", "capstone"], learner)
        capstone = learner / "work/capstone"
        run([sys.executable, "-m", "pytest", "-q"], capstone, expected=1)
        shutil.copy2(ROOT / "instructor/capstone-reading-solution.py", capstone / "reading.py")
        run([sys.executable, "-m", "pytest", "-q"], capstone)
        print("PASS: clean Git baseline, non-overwriting recovery, actual conflict/merge, capstone red and reference green")


if __name__ == "__main__":
    main()
