def pig_latin(word: str) -> str:
    if not word:
        return ""

    word = word.lower()
    if word[0] in "aeiou":
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


word1 = pig_latin("air")
print(word1)
word2 = pig_latin("eat")
print(word2)
word3 = pig_latin("python")
print(word3)
word4 = pig_latin("computer")
print(word4)
