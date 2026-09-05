import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def main():
    if (ROOT / ".git").exists():
        print("A repository already exists. Inspect git status; no changes were made.")
        return
    git("init", "-b", "main")
    git(
        "add",
        "main.py",
        "README.md",
        ".gitignore",
        "pyproject.toml",
        "uv.lock",
        ".python-version",
        "AGENTS.md",
        "tools",
        "tests",
        "exercises",
        "checkpoints",
        "daybook",
        "capstone",
        ".vscode",
        ".github",
    )
    git(
        "-c",
        "user.name=Course Learner",
        "-c",
        "user.email=learner@example.invalid",
        "commit",
        "-m",
        "Start the course workspace",
    )
    print(
        "Created a local baseline. This did not create an account or publish anything."
    )


if __name__ == "__main__":
    main()
