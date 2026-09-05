import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(
        description="Create an independent project in a new work folder"
    )
    parser.add_argument("name")
    args = parser.parse_args()
    if Path(args.name).name != args.name or args.name in {".", ".."}:
        parser.error("Choose a new single folder name")
    work = ROOT / "work"
    if work.is_symlink():
        parser.error("work must not be a symlink")
    work.mkdir(exist_ok=True)
    target = work / args.name
    if target.exists():
        parser.error("Destination exists; choose another name")
    shutil.copytree(ROOT / "capstone", target)
    for name in ("uv.lock", ".python-version", ".gitignore"):
        shutil.copy2(ROOT / name, target / name)
    config = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    config = config.replace('testpaths = ["tests"]', 'testpaths = ["."]')
    config = config.replace(
        'include = ["main.py", "tests", "tools", "daybook"]', 'include = ["."]'
    )
    (target / "pyproject.toml").write_text(config, encoding="utf-8")
    print(f"Created work/{args.name}. Open that folder and read README.md.")


if __name__ == "__main__":
    main()
