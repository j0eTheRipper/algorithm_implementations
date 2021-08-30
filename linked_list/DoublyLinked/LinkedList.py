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

    def insert(self, index, data):
        data = DoubleNode(data)
        data_before = self[index - 1]
        data_after = data_before.next

        data.back = data_before
        data.next = data_after

        data_after.back = data
        data_before.next = data

        self.__len += 1

    def __len__(self):
        return self.__len

    def __getitem__(self, item):
        mid = len(self) // 2

        if item <= mid:
            return self.__get_item_near_head(item)
        else:
            return self.__get_item_near_tail(item)

    def __get_item_near_tail(self, item):
        node = self.tail
        item = len(self) - item - 1
        for _ in range(item):
            node = node.back
        return node

    def __get_item_near_head(self, item):
        node = self.head
        for _ in range(item):
            node = node.next
        return node
