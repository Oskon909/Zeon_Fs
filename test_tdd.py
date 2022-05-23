

from tdd import *

list_man = ['Иман', 'Бермет', 'Нурс', 'Нурзат']


def test_list_sort():
    assert list_sort(list_man) == ['Бермет', 'Нурзат']

