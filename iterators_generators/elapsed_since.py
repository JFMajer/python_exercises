import time
from typing import Iterable


def elapsed_since(items: Iterable):
    last_time = None
    for ele in items:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield delta, ele


for i, x in elapsed_since([1, 3, 5, 2, 5]):
    print(f"first element is {i}, second returned is {x}")
