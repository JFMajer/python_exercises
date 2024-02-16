from collections import Counter


def most_repeting_word(seq):
    max_repeats = 0
    word_with_max_repeats = None
    for word in seq:
        repeats = Counter(word).most_common(1)[0][1]
        if repeats > max_repeats:
            max_repeats = repeats
            word_with_max_repeats = word

    return word_with_max_repeats






words = ['this', 'is', 'an', 'elementary', 'test', 'example']
print(most_repeting_word(words))