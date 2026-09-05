orders = [{"status": "sent", "count": 3}, {"status": "waiting", "count": 7}]
total = 0
for order in orders:
    total = 0
    if order["status"] == "sent":
        total += order["count"]
print(total)
