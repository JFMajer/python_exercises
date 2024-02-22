from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('bob', 'dylan')
    assert formatted_name == 'Bob Dylan'


def test_with_middle_name():
    assert get_formatted_name('bob', 'dylan', 'tom') == 'Bob Tom Dylan'