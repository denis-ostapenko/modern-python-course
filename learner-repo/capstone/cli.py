import argparse
import sys
from pathlib import Path

from reading import filter_records, load_records, make_record, save_records, summarize


def main(argv=None):
    parser = argparse.ArgumentParser(description="Save and summarize reading sessions")
    parser.add_argument("--data", type=Path, required=True)
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("date")
    add.add_argument("title")
    add.add_argument("pages", type=int)
    listing = commands.add_parser("list")
    listing.add_argument("--title")
    commands.add_parser("summary")
    args = parser.parse_args(argv)
    try:
        records = load_records(args.data)
        if args.command == "add":
            records.append(make_record(args.date, args.title, args.pages))
            save_records(args.data, records)
            print("Reading session added")
        elif args.command == "list":
            if args.title is not None:
                records = filter_records(records, args.title)
            for record in records:
                print(f"{record['date']} | {record['title']} | {record['pages']} pages")
        else:
            for title, pages in sorted(summarize(records).items()):
                print(f"{title}: {pages} pages")
    except (ValueError, OSError) as error:
        print(f"Reading Log: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
