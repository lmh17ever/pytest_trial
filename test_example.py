import pytest


def one_more(x):
    return x + 1


def test_correct():
    print('Правильный тест')
    assert one_more(4) == 5


def test_fail():
    print('Неправильный тест')
    assert one_more(3) == 5


def division(dividend, divisor):
    return dividend / divisor


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


def get_sort_list(string):
    new_list = sorted(string.split(', '))
    return new_list


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Миша, Даша')
    assert result == ['Даша', 'Миша', 'Саша', 'Яша']


def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert isinstance(result, int)
