import pytest
from sum import my_sum, my_sum2, my_average, minimum_number, maximum_number, words


def test_sum_of_integers():
    assert my_sum(1, 2, 3) == 6
    assert my_sum(-1, 1) == 0


def test_sum_of_floats():
    assert my_sum(1.1, 2.2, 3.3) == 6.6


def test_empty_args():
    assert my_sum() == 0


def test_sum2_of_integers():
    assert my_sum2([1, 2, 3]) == 6
    assert my_sum2([-1, 1]) == 0


def test_sum2_of_floats():
    assert my_sum2([1.1, 2.2, 3.3]) == 6.6


def test_sum2_empty_list():
    assert my_sum2([]) == 0


def test_sum2_mixed_numbers():
    assert my_sum2([1, 2.5, 3.1]) == 6.6


def test_average_empty_list():
    with pytest.raises(ValueError) as e:
        my_average([])
    assert str(e.value) == "Cannot compute the average of an empty list."


def test_minimum_number():
    assert minimum_number([3, 67, 3, 1]) == 1


def test_maximum_number():
    assert maximum_number([3, 67, 3, 1]) == 67


def test_words():
    assert words(["cat", "dog", "human"]) == (3, 5, 3.67)
