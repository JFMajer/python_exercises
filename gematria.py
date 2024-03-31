import string
import sys
from pathlib import Path
from typing import Generator

letters = list(string.ascii_lowercase)

dict1 = {}
i = 1
for index, letter in enumerate(letters, 1):
    dict1[letter] = index

dict2 = {k: v for (v, k) in enumerate(letters, 1)}

print(dict2)


def gematria_for(word: str) -> int:
    score = 0
    for letter in word.lower().strip():
        if letter not in string.ascii_lowercase:
            continue
        score += dict2[letter]
    return score


def gematria_equal_words(word: str) -> list:
    score = gematria_for(word)
    print(f"Score for word {word} is {score}, here a list of words with same score")
    print('==============================')
    filepath = './files/words.txt'
    path = Path(filepath)
    try:
        with path.open('r') as f:
            same_score_words = [line.strip() for line in f if gematria_for(line.strip().lower()) == score]
    except FileNotFoundError:
        sys.exit(1)
    return same_score_words


print(gematria_for("cat"))
print(gematria_equal_words("cat"))