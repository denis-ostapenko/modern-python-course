from dataclasses import dataclass


@dataclass
class Book:
    title: str
    pages: int


def book_dict(title: str, pages: int) -> dict:
    book = Book(title, pages)
    return {"title": book.title}
