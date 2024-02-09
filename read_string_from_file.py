from pathlib import Path
import re


def read_string_from_file(filename) -> str:
    data = Path(filename).read_text()
    return data


def longest_word(text: str) -> list[str]:
    longest_words = []
    res = re.findall(r'\w+', text)
    len_longest_word = 0
    for word in res:
        if len(word) > len_longest_word:
            longest_words.clear()
            longest_words.append(word)
            len_longest_word = len(word)
        elif len(word) == len_longest_word:
            longest_words.append(word)

    return longest_words


text = read_string_from_file("text1.txt")
list1 = longest_word(text)
print(list1)
