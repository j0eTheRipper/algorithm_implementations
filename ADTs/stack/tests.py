from .stack import Stack


def test_add_elements():
    stack = make_stack()

    assert stack.peek() == 4


def test_remove_elements():
    stack = make_stack()
    stack.pop()

    assert stack.peek() == 3


def make_stack():
    stack = Stack(1)
    stack.add(2)
    stack.add(3)
    stack.add(4)

    return stack
