from linked_list.DoublyLinked.LinkedList import DoublyLinkedList


class Deque:
    def __init__(self, data):
        self.deque = DoublyLinkedList(data)

    def peek_front(self):
        return self.deque.head.value

    def peek_back(self):
        return self.deque.tail.value

    def pop_front(self):
        x = self.deque[0].value
        del self.deque[0]
        return x

    def pop_back(self):
        x = self.deque[len(self) - 1].value
        del self.deque[len(self) - 1]
        return x

    def add_front(self, data):
        self.deque.reverse_append(data)

    def add_back(self, data):
        self.deque.append(data)

    def __len__(self):
        return len(self.deque)
