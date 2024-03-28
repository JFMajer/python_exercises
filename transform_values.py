from typing import Callable


def transform_values(func: Callable, d: dict) -> dict:
    return {k: func(v) for k, v in d.items()}


d = {'a': 1, 'b': 2, 'c': 3}
print(transform_values(lambda x: x * x, d))
