from linked_list.DoublyLinked.LinkedList import DoublyLinkedList


class Deque:
    def __init__(self, data):
        self.deque = DoublyLinkedList(data)

    def peek_top(self):
        return self.deque.head.value

    def peek_bottom(self):
        return self.deque.tail.value

    def pop_top(self):
        x = self.deque[0].value
        del self.deque[0]
        return x

    def pop_bottom(self):
        x = self.deque[len(self) - 1].value
        del self.deque[len(self) - 1]
        return x

    def add_top(self, data):
        self.deque.reverse_append(data)

    def add_bottom(self, data):
        self.deque.append(data)

    def __len__(self):
        return len(self.deque)
