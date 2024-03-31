import sys
from pathlib import Path

vowels = {'a', 'e', 'i', 'o', 'u'}


def get_sv(filepath: str = './files/words.txt') -> set:
    path = Path(filepath)
    vocalic = set()
    try:
        with path.open('r') as f:
            content = f.read()
            for line in content.splitlines():
                if vowels.issubset(line.lower().strip()):
                    vocalic.add(line)
    except FileNotFoundError:
        sys.exit(1)

    return vocalic


print(get_sv())
