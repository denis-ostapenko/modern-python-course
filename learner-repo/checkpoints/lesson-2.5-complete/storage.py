import json
import os
import tempfile
from dataclasses import asdict
from pathlib import Path

from model import Entry, make_entry


def load_entries(path: Path) -> list[Entry]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    if not isinstance(raw, list):
        raise ValueError("Expected a JSON list")
    entries = []
    for row in raw:
        if not isinstance(row, dict) or set(row) != {"category", "minutes"}:
            raise ValueError("Each entry needs category and minutes")
        entries.append(make_entry(row["category"], row["minutes"]))
    return entries


def save_entries(path: Path, entries: list[Entry]) -> None:
    text = json.dumps([asdict(entry) for entry in entries], ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as file:
            temporary = Path(file.name)
            file.write(text)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
