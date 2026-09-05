def totals_by_category(entries):
    totals = {}
    for entry in entries:
        category = entry["category"]
        totals[category] = totals.get(category, 0) + entry["minutes"]
    return totals


def format_total(category, minutes):
    return f"{category}: {minutes} minutes"


def main():
    entries = [{"category": "reading", "minutes": 25}, {"category": "walking", "minutes": 40}]
    for category, minutes in totals_by_category(entries).items():
        print(format_total(category, minutes))


if __name__ == "__main__":
    main()
