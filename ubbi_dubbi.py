import string


def ubbi_dubbi(word: string) -> string:
    word = word.lower()
    word = word.strip()
    word_ubbi_dubbi = ""
    for l in word:
        if l in "aeiou":
            word_ubbi_dubbi = word_ubbi_dubbi + "ub" + l
        else:
            word_ubbi_dubbi += l

    return word_ubbi_dubbi


ubi_dubi1 = ubbi_dubbi("program")
print(ubi_dubi1)
ubi_dubi2 = ubbi_dubbi("milk")
print(ubi_dubi2)
ubi_dubi3 = ubbi_dubbi("elephant")
print(ubi_dubi3)