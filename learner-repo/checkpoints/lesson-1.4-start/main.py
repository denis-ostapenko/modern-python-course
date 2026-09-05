entries = [{"category": "reading", "minutes": 25}, {"category": "walking", "minutes": 40}]
entries.append({"category": "reading", "minutes": 15})
entries[0]["minutes"] = 30
print(entries[0]["category"], entries[0]["minutes"])
