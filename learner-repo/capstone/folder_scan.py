from pathlib import Path


def scan(folder: Path) -> tuple[list[dict], list[str]]:
    records = []
    errors = []
    for path in sorted(folder.iterdir()):
        if path.is_symlink():
            continue
        try:
            if path.is_file():
                records.append({"name": path.name, "extension": path.suffix, "size": path.stat().st_size})
        except OSError as error:
            errors.append(f"{path.name}: {error.strerror}")
    return records, errors
