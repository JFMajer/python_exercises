import itertools
import sys
from collections import deque
from pathlib import Path
import re

from colorama import Fore, Style


def highlight_keyword(line, keyword):
    highlighted = re.sub(f"({keyword})", f"{Fore.BLUE}\\1{Style.RESET_ALL}", line, flags=re.IGNORECASE)
    return highlighted


def word_in_book(filename, word):
    path = Path(filename)
    try:
        prev_lines = deque(maxlen=5)
        with path.open('r') as f:
            for line in f:
                stripped_line = line.strip()
                if word in line:
                    for prev_line in prev_lines:
                        print(prev_line, end='')
                    print(highlight_keyword(line, word), end='')
                    next_lines = (next_line.strip() for next_line in f if next_line.strip())
                    print('\n'.join(itertools.islice(next_lines, 5)), end='\n---\n\n')
                    prev_lines.clear()
                elif stripped_line:
                    prev_lines.append(line.strip())

    except FileNotFoundError:
        print(Fore.RED + f"Couldn't read file content, file {path} not exists")
        sys.exit(1)


word_in_book("./files/don-quixote.txt", "garlic")
word_in_book("./files/don-kichot-z-la-manchy.txt", "czosnkiem")
