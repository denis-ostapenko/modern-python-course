category = input("Category: ").strip()
raw = input("Minutes: ")
try:
    minutes = int(raw)
except ValueError:
    minutes = 0
if category and minutes > 0:
    print(f"{category}: {minutes} minutes")
else:
    print("Use a category and positive whole minutes.")
