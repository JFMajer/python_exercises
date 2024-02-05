def pig_latin(word: str) -> str:
    if not word:
        return ""

    word = word.lower()
    if word[0] in "aeiou":
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


def pl_sentence(sentence: str) -> str:
    words = sentence.split()
    pig_latin_words = [pig_latin(word) for word in words]
    return ' '.join(pig_latin_words)


sentence1 = pl_sentence('this is a test translation')
print(sentence1)
