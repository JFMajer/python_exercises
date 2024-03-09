import pathlib
import re


def is_url(s):
    # This is a simple pattern and might need to be adjusted based on the URLs you're encountering
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.match(pattern, s) is not None


def find_longest_word(filename: str) -> str | None:
    path = pathlib.Path(filename)
    longest_word = ""

    try:
        # print(f"Opening file {path}")
        with path.open(mode='r') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    if len(word) > len(longest_word) and not is_url(word):
                        longest_word = word
    except FileNotFoundError:
        print("Provided filename could not be found")
        return None

    return longest_word


def find_all_longest_words(directory: str, pattern: str = '*.txt') -> dict:
    longest_words = {}
    files = pathlib.Path(directory).rglob(pattern)
    for f in files:
        longest_words[str(f.name)] = find_longest_word(str(f))
    return longest_words


print(find_all_longest_words("files"))
print(find_all_longest_words("files", "*"))
