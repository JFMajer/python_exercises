from typing import List


def different_numbers(numbers: List) -> int:
    return len(set(numbers))


numbers = [1, 2, 3, 1, 2, 3, 4, 1]
unique_nums = different_numbers(numbers)
print(unique_nums)
