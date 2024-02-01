from typing import Union, List, Tuple


def my_sum(*nums: Union[int, float]) -> float:
    sum_to_return = 0
    for num in nums:
        sum_to_return += num
    return sum_to_return


def my_sum2(numbers: List[Union[int, float]]) -> float:
    sum_to_return = 0
    for num in numbers:
        sum_to_return += num
    return sum_to_return


def my_average(numbers: List[Union[int, float]]) -> float:
    if not numbers:
        raise ValueError("Cannot compute the average of an empty list.")
    average = my_sum2(numbers) / len(numbers)
    return round(average, 2)


def minimum_number(numbers: List[Union[int, float]]) -> float:
    min_num = numbers[0]
    for n in numbers:
        if n < min_num:
            min_num = n
    return min_num


def maximum_number(numbers: List[Union[int, float]]) -> float:
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num


def words(list_of_words: List[str]) -> Tuple[float, float, float]:
    if not list_of_words:
        raise ValueError("The list of words cannot be empty.")

    list_of_word_lengths = [len(w) for w in list_of_words]
    min_letters = minimum_number(list_of_word_lengths)
    max_letters = maximum_number(list_of_word_lengths)
    avg_letters = my_average(list_of_word_lengths)

    return min_letters, max_letters, avg_letters
