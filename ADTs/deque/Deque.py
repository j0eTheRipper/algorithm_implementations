from linked_list.DoublyLinked.LinkedList import DoublyLinkedList


class Deque:
    def __init__(self, data):
        self.__deque = DoublyLinkedList(data)

    def peek_front(self):
        return self.__deque.head.value

    def peek_back(self):
        return self.__deque.tail.value

    def pop_front(self):
        x = self.__deque[0].value
        del self.__deque[0]
        return x

    def pop_back(self):
        x = self.__deque[len(self) - 1].value
        del self.__deque[len(self) - 1]
        return x

    def add_front(self, data):
        self.__deque.reverse_append(data)

    def add_back(self, data):
        self.__deque.append(data)

    def __len__(self):
        return len(self.__deque)
