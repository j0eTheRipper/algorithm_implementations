from binary_search import search

arr = [i + 1 for i in range(0, 10)]


def test_1():
    assert search(arr, 4) == 3

def test_2():
    assert search(arr, 7) == 6
