import argparse
import sys
from pathlib import Path

from model import make_entry
from reporting import totals_by_category
from storage import load_entries, save_entries


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Record and summarize time spent")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path.home() / ".daybook.json",
        help="JSON data file (default: home/.daybook.json)",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Add one activity")
    add.add_argument("category")
    add.add_argument("minutes", type=int)
    commands.add_parser("list", help="List activities in insertion order")
    commands.add_parser("summary", help="Total minutes by category")
    args = parser.parse_args(argv)
    try:
        entries = load_entries(args.data)
        if args.command == "add":
            entries.append(make_entry(args.category, args.minutes))
            save_entries(args.data, entries)
            print("Entry added")
        elif args.command == "list":
            for entry in entries:
                print(f"{entry.category}: {entry.minutes} minutes")
        else:
            for category, minutes in sorted(totals_by_category(entries).items()):
                print(f"{category}: {minutes} minutes")
    except (ValueError, OSError) as error:
        print(f"Daybook: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
