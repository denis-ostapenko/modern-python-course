from dataclasses import asdict, dataclass


@dataclass
class Book:
    title: str
    pages: int


def book_dict(title: str, pages: int) -> dict:
    return asdict(Book(title, pages))
