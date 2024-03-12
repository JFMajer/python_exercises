from typing import Optional

import typer
from typing_extensions import Annotated
from rich import print


def main(name: Annotated[Optional[str], typer.Argument()] = None, lastname: Annotated[Optional[str], typer.Argument()] = None, formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, greets formally.
    """
    greeting = "Good day sir/madam" if formal else "Hello"
    full_name = f"{name or ''} {lastname or ''}".strip()

    if not full_name:
        print("Hello, what's your name?")
        raise typer.Exit()
    print(f"{greeting} {full_name}!")


if __name__ == "__main__":
    typer.run(main)
