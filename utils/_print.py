import typer


def _print(book):
    """
    helper function to print the book passed int
    book: Book
    """
    typer.secho(f"\n> Title: {book.get('title')}", fg=typer.colors.YELLOW)
    typer.secho(f"- Author: {book.get('author')}", fg=typer.colors.BRIGHT_BLUE)
    typer.secho(f"- Page: {book.get('page')}", fg=typer.colors.BRIGHT_BLUE)
    typer.secho(f"- ISBN: {book.get('isbn')}", fg=typer.colors.BRIGHT_BLUE)
    typer.secho(f"- Completed: {book.get('completed')}", fg=typer.colors.BRIGHT_BLUE)
    typer.secho(f"- Date Added: {book.get('date_added')}", fg=typer.colors.BRIGHT_BLUE)
    typer.secho(
        f"- Date Completed: {book.get('date_completed')}",
        fg=typer.colors.BRIGHT_BLUE,
    )
    typer.secho("\n")
