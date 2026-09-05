# CSV as an exchange format

Optional · After files and JSON · 30 to 45 minutes

A CSV file is a table of text fields. A header names columns; quoting allows a field to contain commas. Use the csv module rather than splitting each line on commas.

## Try

Predict how a title containing a comma should be quoted, then run:

```python
import csv
import io

buffer = io.StringIO(newline="")
writer = csv.DictWriter(buffer, fieldnames=["title", "pages"])
writer.writeheader()
writer.writerow({"title": "Rain, then sun", "pages": 12})
rows = list(csv.DictReader(io.StringIO(buffer.getvalue())))
assert rows == [{"title": "Rain, then sun", "pages": "12"}]
print(rows[0]["title"])
```

The pages field returns as text. Convert and validate it deliberately.

## Build

Export three reading records to a file opened with encoding="utf-8" and newline="". On import, require exactly the title and pages headers. Validate each row with the same positive-pages rule as the project. Keep valid rows and collect a line-numbered error for each invalid row; do not silently invent a number.

## Verify

Test a comma inside a quoted title, Unicode text, an empty file, a missing header and a non-numeric page count. Export the valid rows again and compare the documented field values, not platform newline bytes. Write pytest assertions for these cases.

If stuck, first round-trip a single in-memory row with the example, then add the file boundary. [Python csv documentation](https://docs.python.org/3/library/csv.html) describes quoting and newline handling.
