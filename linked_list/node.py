class Node:
    def __init__(self, data=None, next_pointer=None):
        self.value = data
        self.next = next_pointer


class DoubleNode(Node):
    def __init__(self, data=None, next_pointer=None, previous_pointer=None):
        super().__init__(data=data, next_pointer=next_pointer)
        self.previous_pointer = previous_pointer
