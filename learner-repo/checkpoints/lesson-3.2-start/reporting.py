from model import Entry


def totals_by_category(entries: list[Entry]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for entry in entries:
        totals[entry.category] = totals.get(entry.category, 0) + entry.minutes
    return totals
