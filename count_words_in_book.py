import sys
from pathlib import Path

from colorama import Fore


def count_words(filename):
    path = Path(filename)

    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(Fore.RED + f"Couldn't read file content, file {path} not exists")
        sys.exit(1)

    words = content.split()
    num_of_words = len(words)

    print(f"Book {path} contains about {num_of_words} words, it will take on average {num_of_words / 13000:.2f} hours")


count_words("don-quixote.txt")
