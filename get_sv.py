import sys
from pathlib import Path

vowels = {'a', 'e', 'i', 'o', 'u'}


def get_sv(filepath: str = './files/words.txt') -> set:
    path = Path(filepath)
    try:
        with path.open('r') as f:
            s = {line for line in f if vowels.issubset(line.lower().strip())}
    except FileNotFoundError:
        sys.exit(1)

    return s


print(get_sv())
