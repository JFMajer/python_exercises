from pathlib import Path
from typing import Callable


def pig_latin(word: str) -> str:
    if not word:
        return ""

    word = word.lower()
    if word[0] in "aeiou":
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


# def pl_sentence(sentence: str) -> str:
#     words = sentence.split()
#     pig_latin_words = [pig_latin(word) for word in words]
#     return ' '.join(pig_latin_words)


def pl_file(filename: str, func: Callable[[str], str]) -> str:
    path = Path(filename)
    with path.open('r') as f:
        return ' '.join((func(word) for line in f for word in line.split()))


print(pl_file("files/buddenbrooks.txt", pig_latin))
