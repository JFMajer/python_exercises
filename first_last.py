from typing import List


def firstlast(sequence):
    return sequence[:1] + sequence[-1:]


print(firstlast('abcdefgh'))
print(firstlast([1, 2, 3, 4]))

def even_odd_sums(numbers) -> List:
    sum_even = 0
    sum_odd = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return [sum_even, sum_odd]

print(even_odd_sums([1, 2, 3, 4, 5]))

def even_odd_sums_indexes(numbers) -> List:
    sum_even = 0
    sum_odds = 0
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            sum_even += num
        else:
            sum_odds += num

    return [sum_even, sum_odds]

print(even_odd_sums_indexes([10, 20, 30, 40, 50, 60]))


