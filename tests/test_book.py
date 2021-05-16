from toread.book import Book
import datetime


def test_book_default():
    b1 = Book("Atomic Habits", "James Clear", 499)
    assert b1.completed == False
    assert b1.isbn == None


def test_book_eq():
    b1 = Book("Atomic Habits", "James Clear", 499)
    b2 = Book("Atomic Habits", "Mark Manson", 300)
    assert b1 == b2


def test_book_not_eq():
    b1 = Book("Atomic Habits", "James Clear", 499)
    b2 = Book("TSAOTGAF", "Mark Manson", 300)
    assert b1 != b2


def test_book_asdict():
    b1 = Book("Atomic Habits", "James Clear", 499).asdict()
    expected = {
        "title": "Atomic Habits",
        "author": "James Clear",
        "page": 499,
        "isbn": None,
        "completed": False,
        "date_added": str(datetime.date.today()),
        "date_completed": None,
    }
    assert b1 == expected


def test_book_repr():
    b1 = Book("Atomic Habits", "James Clear", 499)
    expected = "Book(title=Atomic Habits, author=James Clear, page=499, isbn=None)"
    assert repr(b1) == expected
