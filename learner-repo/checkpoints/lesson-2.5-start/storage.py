import json
from pathlib import Path


def load_entries(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    if not isinstance(data, list):
        raise ValueError("Expected a list of entries")
    for entry in data:
        if not isinstance(entry, dict) or not isinstance(entry.get("category"), str) or type(entry.get("minutes")) is not int or not entry["category"].strip() or entry["minutes"] <= 0:
            raise ValueError("Each entry needs a category and positive whole minutes")
    return data


def save_entries(path, entries):
    path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
