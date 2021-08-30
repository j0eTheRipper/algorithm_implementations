from .Node import DoubleNode
from ..SinglyLinked.LinkedList import SinglyLinkedList as LinkedList


class DoublyLinkedList(LinkedList):
    def __init__(self, data=None):
        super().__init__(data)
        self.__len = 0

        if data is not None:
            self.head = DoubleNode(data)
            self.tail = self.head
            self.__len += 1

    def append(self, data):
        data = DoubleNode(data)
        self.tail.next = data
        data.back = self.tail
        self.tail = data
        self.__len += 1

    def reverse_append(self, data):
        data = DoubleNode(data)
        data.next = self.head
        self.head.back = data
        self.head = data
        self.__len += 1

    def __len__(self):
        return self.__len
