def flip_a_dict(dictionary: dict) -> dict:
    return {v: k for k, v in dictionary.items()}


d = {'a': 1, 'b': 2, 'c': 3}
print(flip_a_dict(d))
