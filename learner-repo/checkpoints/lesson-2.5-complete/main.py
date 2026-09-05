from pathlib import Path

from reporting import totals_by_category
from storage import load_entries


def main() -> None:
    entries = load_entries(Path(__file__).resolve().parent / "entries.json")
    for category, minutes in totals_by_category(entries).items():
        print(f"{category}: {minutes} minutes")


if __name__ == "__main__":
    main()
