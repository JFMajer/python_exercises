from typing import Optional

import typer
from typing_extensions import Annotated
from rich import print


def main(name: Annotated[str, typer.Argument(..., help="First Name")],
         lastname: Annotated[Optional[str], typer.Argument(help="Last Name")] = None, formal: bool = False):
    greeting = "Good day sir/madam" if formal else "Hello"
    full_name = f"{name or ''} {lastname or ''}".strip()

    if not full_name:
        print("Hello, what's your name?")
        raise typer.Exit()
    print(f"{greeting} {full_name}!")


if __name__ == "__main__":
    typer.run(main)
