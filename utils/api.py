import datetime
import pymongo
from typing import List
from utils.book import Book
from utils.db import setup
from utils.custom_exceptions import BookExist, BookNotFound
from dataclasses import asdict


class API:
    def __init__(
        self,
        db_name: str,
        collection_name: str,
        *,
        domain: str = None,
        port: int = None,
    ) -> None:
        """setup mongodb client."""
        self.db = setup(db_name, collection_name, domain=domain, port=port)

    def get(self, book_title: str = None) -> Book:
        """
        queries database and retrieves all the books
        if book title is not passed
        return: Book
        """
        if book_title:
            if not self._search_book(book_title):
                raise BookNotFound("Book with that title was not found.")
            return self._search_book(book_title)

        return self._get()

    def _get(self) -> List[Book]:
        """helper method to retrieve all books from database."""
        books = self.db.find()
        books_list = []
        for book in books:
            books_list.append(book)
        return books_list

    def _search_book(self, book_title: str) -> Book:
        """
        helper method to retrive a book with passed in title from database.
        book_title is case sensitive.
        """

        return self.db.find_one({"title": book_title}) or False

    def post(self, title: str, author: str, page: int, isbn: int = None) -> Book:
        """
        pymongo's insert_one(). Add a book to a database
        if the book doesn't exist
        return: Book
        """
        book = Book(title, author, page, isbn)
        try:
            if self._search_book(title):
                raise BookExist("Book with that title already exist.")
            self.db.insert_one(asdict(book))
        except pymongo.errors.WriteError as err:
            raise err
        return "Successfully created."

    def update(self, book_title, key, value) -> Book:
        """
        pymongo's update_one(), update a book with book_title with given key value
        update(1, 'title', 'new title')
        """
        book = self._search_book(book_title)
        if not key in book.keys():
            raise KeyError(f"{key} not found.")

        if not book:
            raise BookNotFound("Book with that title was not found.")

        self.db.update_one({"title": book_title}, {"$set": {key: value}})
        return "Successfully updated."

    def delete(self, book_title):
        """
        delete book with passed in title if exist
        """
        book = self._search_book(book_title)
        if not book:
            raise BookNotFound("Book with that title was not found.")
        self.db.delete_one({"title": book_title})
        return "Successfully deleted"

    def completed(self, book_title):
        """
        Mark book as completed and set date_completed to current date.
        """
        book = self._search_book(book_title)
        if not book:
            raise BookNotFound("Book with that title was not found.")
        self.db.update_one(
            {"title": book_title},
            {"$set": {"completed": True, "date_completed": str(datetime.date.today())}},
        )
        return f"Marked as completed"
