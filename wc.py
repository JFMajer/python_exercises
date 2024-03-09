from pathlib import Path


def wc(filename: str):
    path = Path(filename)
    numOfChars = 0
    numOfWords = 0
    numOfLines = 0
    wordCount = {}
    uniqueWords = set()

    try:
        with path.open(mode='r') as file:
            for line in file:
                numOfChars += len(line)
                # increment number of lines
                numOfLines += 1
                # count number of words in each line
                words = line.split()
                numOfWords += len(words)
                # put distinct words in dictionary as keys and count amount of times they appear
                # for word in words:
                #     wordCount[word] = wordCount.get(word, 0) + 1
                # # this value represents amount of distinct words in a file
                # distinctWordCount = len(wordCount)
                # below better way to count distinct words
                uniqueWords.update(words)

    except FileNotFoundError:
        print("Provided filename could not be found")
        return None

    return numOfChars, numOfWords, numOfLines, len(uniqueWords)


# Example usage
filename = "files/wcfile.txt"
try:
    chars, words, lines, distinct_words = wc(filename)
    print(f"Number of characters: {chars}")
    print(f"Number of words: {words}")
    print(f"Number of lines: {lines}")
    print(f"Distinct words: {distinct_words}")
except ValueError as e:
    print(f"Error unpacking return values from wc function: {e}")
