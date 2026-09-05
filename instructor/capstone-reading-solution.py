import json
import os
import tempfile
from datetime import date as calendar_date
from pathlib import Path


def make_record(date: str, title: str, pages: int) -> dict:
    if not isinstance(date, str) or calendar_date.fromisoformat(date).isoformat() != date:
        raise ValueError("Use an actual date in YYYY-MM-DD form")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title must contain text")
    if type(pages) is not int or pages <= 0:
        raise ValueError("Pages must be a positive whole number")
    return {"date": date, "title": title.strip(), "pages": pages}


def summarize(records: list[dict]) -> dict[str, int]:
    totals = {}
    for record in records:
        totals[record["title"]] = totals.get(record["title"], 0) + record["pages"]
    return totals


def filter_records(records: list[dict], title: str) -> list[dict]:
    return [dict(record) for record in records if record["title"] == title]


def validate(records):
    if not isinstance(records, list):
        raise ValueError("Expected a list")
    validated = []
    for record in records:
        if not isinstance(record, dict) or set(record) != {"date", "title", "pages"}:
            raise ValueError("Expected date, title and pages")
        validated.append(make_record(record["date"], record["title"], record["pages"]))
    return validated


def load_records(path: Path) -> list[dict]:
    try:
        return validate(json.loads(path.read_text(encoding="utf-8")))
    except FileNotFoundError:
        return []


def save_records(path: Path, records: list[dict]) -> None:
    text = json.dumps(validate(records), ensure_ascii=False, indent=2) + "\n"
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as file:
            temporary = Path(file.name)
            file.write(text)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
