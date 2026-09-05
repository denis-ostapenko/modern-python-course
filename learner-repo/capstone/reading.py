from pathlib import Path


def make_record(date: str, title: str, pages: int) -> dict:
    raise NotImplementedError("Validate and return one record")


def summarize(records: list[dict]) -> dict[str, int]:
    raise NotImplementedError("Total pages by title")


def filter_records(records: list[dict], title: str) -> list[dict]:
    raise NotImplementedError("Return matching records without changing input")


def load_records(path: Path) -> list[dict]:
    raise NotImplementedError("Load and validate records; missing file is empty")


def save_records(path: Path, records: list[dict]) -> None:
    raise NotImplementedError("Save UTF-8 JSON without damaging an existing file on failure")
