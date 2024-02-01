from sum import my_sum


def test_sum_of_integers():
    assert my_sum(1, 2, 3) == 6
    assert my_sum(-1, 1) == 0


def test_sum_of_floats():
    assert my_sum(1.1, 2.2, 3.3) == 6.6


def test_empty_args():
    assert my_sum() == 0