from pathlib import Path


def final_line(filename: str) -> str:
    """
    Return the last line of a file.

    Reads the specified file and returns its last line. The function assumes
    that the file is encoded in UTF-8 and that it is small enough to be read
    into memory comfortably.

    Parameters:
    filename (str): The path to the file.

    Returns:
    str: The last line of the file.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    """

    path = Path(filename)
    final_line = ''
    try:
        with path.open(mode="r", encoding="utf-8") as file:
            for line in file:
                final_line = line
    except FileNotFoundError:
        print("Provided filename could not be found")

    return final_line


last_line = final_line("don-quixote.txt")
print(f"Last line of Don Quixote is: {last_line}")

last_log = final_line("files/nginx_json_logs")
print(f"last line in nginx logs is {last_log}")
