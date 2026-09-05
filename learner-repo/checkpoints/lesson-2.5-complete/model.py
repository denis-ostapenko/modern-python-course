from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
    category: str
    minutes: int


def make_entry(category: str, minutes: int) -> Entry:
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must contain text")
    if type(minutes) is not int or minutes <= 0:
        raise ValueError("Minutes must be a positive whole number")
    return Entry(category.strip(), minutes)
