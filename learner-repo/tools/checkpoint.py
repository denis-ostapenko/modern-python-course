import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    choices = sorted(p.name for p in (ROOT / "checkpoints").iterdir() if p.is_dir())
    parser = argparse.ArgumentParser(
        description="Copy a course checkpoint into a NEW work folder"
    )
    parser.add_argument("checkpoint", choices=choices)
    parser.add_argument("destination", help="New folder name inside work/")
    args = parser.parse_args()
    if (
        not args.destination
        or Path(args.destination).name != args.destination
        or args.destination in {".", ".."}
    ):
        parser.error("Use one new folder name, without slashes")
    work = ROOT / "work"
    if work.is_symlink():
        parser.error("work must be a real directory, not a symbolic link")
    work.mkdir(exist_ok=True)
    target = work / args.destination
    if target.exists():
        parser.error(
            "Destination exists. Choose a new name; your work will not be overwritten"
        )
    shutil.copytree(ROOT / "checkpoints" / args.checkpoint, target)
    print(f"Copied to work/{args.destination}. Your existing files are unchanged.")
    print(f"Run: uv run python work/{args.destination}/main.py")


if __name__ == "__main__":
    main()
