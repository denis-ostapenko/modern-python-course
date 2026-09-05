entries = [{"category": "reading", "minutes": 25}, {"category": "walking", "minutes": 40}, {"category": "reading", "minutes": 15}]
totals = {}
for entry in entries:
    category = entry["category"]
    totals[category] = totals.get(category, 0) + entry["minutes"]
for category in totals:
    print(f"{category}: {totals[category]} minutes")
