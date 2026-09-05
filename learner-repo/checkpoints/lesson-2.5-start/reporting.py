def totals_by_category(entries):
    totals = {}
    for entry in entries:
        category = entry["category"]
        totals[category] = totals.get(category, 0) + entry["minutes"]
    return totals
