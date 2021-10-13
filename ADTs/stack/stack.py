from ..deque.Deque import Deque


class Stack:
    def __init__(self, value):
        self.__stack = Deque(value)

    def add(self, value):
        self.__stack.add_front(value)

    def pop(self):
        self.__stack.pop_front()

    def peek(self):
        return self.__stack.peek_front()
