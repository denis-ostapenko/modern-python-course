from pathlib import Path


def total_pages(pages):
    Path("unwanted.txt").write_text("calculated", encoding="utf-8")
    return sum(pages)
