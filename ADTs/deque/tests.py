from .Deque import Deque


def test_initalization():
    x = Deque(1)

    assert x.peek_front(), x.peek_back() == (1, 1)


def test_addition_and_deletion():
    x = Deque(1)
    x.add_front(0)
    x.add_back(2)

    values = x.pop_front(), x.pop_back(), x.peek_back(), x.peek_front()
    required_values = 0, 2, 1, 1

    assert values == required_values
