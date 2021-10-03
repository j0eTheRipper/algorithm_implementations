from .Node import SingleNode


class SinglyLinkedList:
    def __init__(self, data=None):
        self.__len = 0
        self.tail = None
        self.head = None

        if data is not None:
            self.head = SingleNode(data)
            self.tail = self.head
            self.__len += 1

    def append(self, data):
        """Adds to the end of the list"""

        node = SingleNode(data)

        self.tail.next = node
        self.tail = node

        self.__len += 1

    def reverse_append(self, data):
        """Adds to the beginning of the list"""

        node = SingleNode(data)
        node.next = self.head
        self.head = node

        self.__len += 1

    def insert(self, index, data):
        if index >= len(self) or index < 0:
            raise IndexError
        else:
            node_before = self[index - 1]
            node_after = self[index]
            node = SingleNode(data)

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
                node = node.next

    def reverse(self):
        temp_head = self.head
        node = self.head.next

        while temp_head.next is not None:
            temp_head.next = node.next
            node.next = self.head
            self.head, node = node, self.head
            node = node.next

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

        self.__len -= 1

    def __len__(self):
        return self.__len
