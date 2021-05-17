import datetime


class Book:
    def __init__(self, title: str, author: str, page: int, isbn: int = None) -> None:
        self.title = title
        self.author = author
        self.page = page
        self.isbn = isbn
        self.completed = False
        self.date_added = datetime.date.today()
        self.date_completed = "Not completed yet."

    def asdict(self):
        return {
            "title": self.title,
            "author": self.author,
            "page": self.page,
            "isbn": self.isbn,
            "completed": self.completed,
            "date_added": str(self.date_added),
            "date_completed": "Not completed yet.",
        }

    def __eq__(self, other) -> bool:
        if not isinstance(self, other.__class__):
            return NotImplemented
        return self.title == other.title

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title={self.title}, author={self.author}, page={self.page}, isbn={self.isbn})"
