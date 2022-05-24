from file_sistem import *

test_fs = r"C:\Users\HP\PycharmProjects\pythonProject24\oskon\test\.zeon_fs"


def helper_del(command):
    os.rmdir(command)


def helper_add(expected):
    my_file = open(expected, "a+")
    my_file.close()


def helper_add2(command):
    os.mkdir(command)


# ---

def test_init():
    assert init(test_fs) == test_fs
    helper_del(test_fs)


def test_delete():
    expected = 'BabyFile.txt'
    helper_add(expected)
    assert delete(expected) == False


def test_all_file():
    # test_list = ['oskon', 'Meta.py', 'aman']
    assert all_file() == type(list())


def test_copy():
    varible = 'index.html'
    varible_2 = 'test_file'

    helper_add(varible)
    helper_add2(varible_2)

    assert copy(varible, varible_2) == fr'{varible_2}\{varible}'
    os.remove(varible)
    os.remove(fr'{varible_2}\{varible}')
    helper_del(varible_2)
