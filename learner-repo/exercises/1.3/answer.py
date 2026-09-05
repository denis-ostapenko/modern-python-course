items = [{"name": "pen", "count": 3}, {"name": "book", "count": 5}]
selected = 1
items[0]["count"] = 9
print(items[selected]["name"], items[selected]["count"], items[selected].get("shelf", "unassigned"))
