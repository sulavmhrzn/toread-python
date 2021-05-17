import os
import json
import typer
from pathlib import Path
from utils.api import API
from utils.custom_exceptions import BookExist, BookNotFound
from utils._print import _print

app = typer.Typer()
api = None
ERROR = typer.colors.RED
SUCCESS = typer.colors.GREEN


def configure_api() -> API:
    """
    configure API with proper database and collection
    raises FileNotFoundError if settings.json is not found.
    """
    settings_file = Path("settings.json").absolute()
    if not os.path.exists(settings_file):
        raise FileNotFoundError(
            "settings.json file was not found. The program will now terminate"
        )
    with open("settings.json") as f:
        f = json.load(f)
        db_name = f["db_name"]
        collection_name = f["collection_name"]

    global api
    api = API(db_name, collection_name)


def configure():
    configure_api()


@app.command()
def get(title: str = typer.Argument(None)):
    """
    retrieve books from database
    Optional: title
    """
    books = api.get()
    if title:
        try:
            book = api.get(title)
            return _print(book)
        except BookNotFound as err:
            typer.secho(err.args[0], fg=ERROR)
            raise typer.Exit()

    typer.secho(
        f"\n[*] Total books: {len(books)}", fg=typer.colors.BRIGHT_YELLOW, bold=True
    )

    for book in books:
        _print(book)


@app.command()
def create():
    """
    Create and save a book in database
    title: str
    author: str
    page: int
    isbn: Optional[int] = None
    """
    title = typer.prompt("Title")
    author = typer.prompt("Author")
    page = typer.prompt("Page", type=int)
    isbn = typer.prompt("ISBN", default="None")
    try:
        success = api.post(title, author, page, isbn)
        typer.secho(success, fg=SUCCESS)
    except BookExist as err:
        typer.secho(err.args[0], fg=ERROR)
        get(title)
        raise typer.Exit()


@app.command()
def completed(title: str = typer.Argument(...)):
    """
    Mark book as completed
    title: str
    """
    try:
        success = api.completed(title)
        typer.secho(success, fg=SUCCESS)
    except BookNotFound as err:
        typer.secho(err.args[0], fg=ERROR)
        raise typer.Exit()


@app.command()
def delete(title: str = typer.Argument(...)):
    """
    Delete book from database
    title; str
    """
    get(title)
    confirmation = typer.confirm("Are you sure you want to delete it?")
    if not confirmation:
        typer.secho("Not deleting")
        raise typer.Abort()
    try:
        success = api.delete(title)
        typer.secho(success, fg=SUCCESS)
    except BookNotFound as err:
        typer.secho(err.args[0], fg=ERROR)
        raise typer.Exit()


@app.command()
def update(title: str = typer.Argument(...)):
    """
    Given a book title update its value corresponding to key passed in.
    title: str
    key: str
    value: str | int
    """
    get(title)
    key = typer.prompt("What do you want to update?")
    value = typer.prompt("Enter the updated value")
    try:
        success = api.update(title, key, value)
        typer.secho(success, fg=SUCCESS)
    except KeyError as err:
        typer.secho(err.args[0], fg=ERROR)
        raise typer.Exit()


if __name__ == "__main__":
    """
    Initialize the application with proper configuration.
    """
    configure()
    app()
