import datetime
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    page: int
    isbn: int = None
    completed: bool = False
    date_added: str = str(
        datetime.date.today()
    )  # convert it to str because datetime.date is not part of the bson Encoders
    date_completed: str = "Not completed yet."
