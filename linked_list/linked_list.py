from node import Node


class LinkedList:
    def __init__(self, data=None):
        self.__len = 0
        self.tail = None

        if data is not None:
            self.head = Node(data)
            self.head.next = self.tail
            self.tail = self.head
            self.__len += 1
        else:
            self.head = None

        self.__node = None

    def append(self, data):
        """Adds to the end of the list"""

        node = Node(data)

        self.tail.next = node
        self.tail = self.tail.next

        self.__len += 1

    def reverse_append(self, data):
        """Adds to the beginning of the list"""

        node = Node(data)
        node.next = self.head
        self.head = node

        self.__len += 1

    def insert(self, index, data):
        if index >= len(self) or index < 0:
            raise IndexError
        else:
            node_before = self[index - 1]
            node_after = self[index]
            node = Node(data)

            node.next = node_after
            node_before.next = node

            self.__len += 1

    def find(self, data):
        node = self.head
        index = 0

        while node is not None:
            if node.value == data:
                return index
            else:
                index += 1
                node = node.value

    def __getitem__(self, item):
        if item < 0 or item > len(self):
            raise IndexError
        else:
            node = self.head

            for _ in range(item):
                node = node.next

            return node

    def __setitem__(self, key, value):
        item = self[key]
        item.value = value

    def __delitem__(self, key):
        previous_item = self[key - 1]
        next_item = previous_item.next.next

        previous_item.next = next_item

    def __len__(self):
        return self.__len
