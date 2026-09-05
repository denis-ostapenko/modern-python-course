import json
from pathlib import Path


def load_books(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))
