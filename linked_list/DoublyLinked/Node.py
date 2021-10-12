from ..SinglyLinked.Node import SingleNode


class DoubleNode(SingleNode):
    def __init__(self, data=None, next_pointer=None, previous_pointer=None):
        super().__init__(data=data, next_pointer=next_pointer)
        self.back = previous_pointer

    def __repr__(self):
        return str(self.value)
