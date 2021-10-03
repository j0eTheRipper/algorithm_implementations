class SingleNode:
    def __init__(self, data=None, next_pointer=None):
        self.value = data
        self.next = next_pointer

    def __repr__(self):
        return str(self.value)
