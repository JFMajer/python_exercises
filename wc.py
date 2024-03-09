from pathlib import Path


def wc(filename: str):
    path = Path(filename)
    numOfChars = 0
    numOfWords = 0
    numOfLines = 0
    wordCount = {}

    try:
        with path.open(mode='r') as file:
            for line in file:
                # increment number of lines
                numOfLines += 1
                # count number of words in each line
                words = line.split()
                numOfWords += len(words)
                # put distinct words in dictionary as keys and count amount of times they appear
                for word in words:
                    wordCount[word] = wordCount.get(word, 0) + 1
                # this value represents amount of distinct words in a file
                distinctWordCount = len(wordCount)
    except FileNotFoundError:
        print("Provided filename could not be found")

    print(numOfLines, numOfWords, distinctWordCount)


wc("files/wcfile.txt")
