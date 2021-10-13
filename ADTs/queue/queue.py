from ..deque.Deque import Deque


class Queue:
    def __init__(self, value):
        self.__queue = Deque(value)

    def add(self, value):
        self.__queue.add_front(value)

    def pop(self):
        self.__queue.pop_back()

    def peek(self):
        return self.__queue.peek_back()
