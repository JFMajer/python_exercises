import typer
from rich import print
from rich.console import Console

err_console = Console(stderr=True)


def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, greets formally.
    """
    err_console.print("Here is something written to standard error")
    if formal:
        print(f"Good day dearest sir/madam {name} {lastname}")
    else:
        print(f"Hello {name} {lastname}!")


if __name__ == "__main__":
    typer.run(main)
