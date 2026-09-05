raw = " 3 "
try:
    weight = int(raw)
except ValueError:
    weight = 0
if weight > 0:
    print("accepted")
else:
    print("rejected")
