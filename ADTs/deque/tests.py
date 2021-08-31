from .Deque import Deque


def test_initalization():
    x = Deque(1)

    assert x.peek_top(), x.peek_bottom() == (1, 1)


def test_addition_and_deletion():
    x = Deque(1)
    x.add_top(0)
    x.add_bottom(2)

    values = x.pop_top(), x.pop_bottom(), x.peek_bottom(), x.peek_top()
    required_values = 0, 2, 1, 1

    assert values == required_values
