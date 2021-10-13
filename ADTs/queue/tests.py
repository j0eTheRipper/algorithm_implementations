from .queue import Queue


def test_add_elements():
    queue = make_queue()

    assert queue.peek() == 1


def test_remove_elements():
    queue = make_queue()
    queue.pop()

    assert queue.peek() == 2


def make_queue():
    queue = Queue(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)

    return queue
