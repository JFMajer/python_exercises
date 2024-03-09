import glob
import pathlib
from pathlib import Path


def find_longest_word(filename: str) -> str | None:
    path = Path(filename)
    longest_word = ""

    try:
        with path.open(mode='r') as file:
            for line in file:
                for word in line.split():
                    if len(word) > len(longest_word):
                        longest_word = word
    except FileNotFoundError:
        print("Provided filename could not be found")
        return None

    return longest_word


def find_all_longest_words(directory: str, pattern: str = '*.txt') -> dict:
    longest_words = {}
    files = pathlib.Path(directory).rglob(pattern)
    for f in files:
        longest_words[str(f.name)] = find_longest_word(f)
    return longest_words


print(find_all_longest_words("files"))
print(find_all_longest_words("files", "*"))
