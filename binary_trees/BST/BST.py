from collections import deque


class Node:
    def __init__(self, value=None):
        self.parent = None
        self.right = None
        self.left = None
        self.value = value

    def push_node(self, parent):
        """Pushes the node at hand to the parent node given."""
        self.parent = parent

        if self.value > self.parent.value:
            self.parent.right = self
        else:
            self.parent.left = self

    @property
    def successor(self):
        """Gets the node's successor"""
        if self.right:
            curr = self.right
            while curr.left:
                curr = curr.left

            return curr
        else:
            curr = self

            while curr.parent:
                if curr.parent.value > curr.value:
                    return curr.parent

                if curr == curr.parent.left:
                    return curr.parent
                else:
                    curr = curr.parent

    def delete(self):
        if not (self.left or self.right):
            new_leaf = self.parent
            if new_leaf.right == self:
                new_leaf.right = None
                del self
            else:
                new_leaf.left = None
                del self
        elif self.left and not self.right:
            self.__remove_node_with_single_child(self.left)
        elif self.right and not self.left:
            self.__remove_node_with_single_child(self.right)
        else:
            successor = self.successor
            if successor is successor.parent.left:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right

            successor.parent = self.parent
            successor.left = self.left
            successor.right = self.right

            if self is self.parent.left:
                self.parent.left = successor
            else:
                self.parent.right = successor

    def __remove_node_with_single_child(self, node):
        if self is self.parent.left:
            self.parent.left = node
        else:
            self.parent.right = node

        node.parent = self.parent

        return self

    def __repr__(self):
        return str(self.value)


class BST:
    def __init__(self, *elements):
        if elements:
            self.root = Node(elements[0])
            self.add_new_elements(*elements[1::])
        else:
            self.root = Node()

    def add_new_elements(self, *elements: iter):
        if self.root.value is None:
            self.root = Node(elements[0])
            elements = elements[1::]

        for value in elements:
            curr = self.__go_to_leaf(self.root, value)

            new_node = Node(value)
            new_node.push_node(curr)

    def find(self, element):
        curr = self.root

        while curr:
            if curr.value == element:
                return curr
            elif curr.value < element:
                curr = curr.right
            else:
                curr = curr.left

    def remove(self, element):
        element_node = self.find(element)
        if element_node:
            element_node.delete()

    @staticmethod
    def __go_to_leaf(curr, value):
        while curr.left or curr.right:
            if value <= curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    break
        return curr

    @property
    def in_order(self):
        result = []
        tree = deque()  # Stack
        tree.append(self.root)
        curr = self.root.left

        while tree or curr:
            if curr:
                tree.append(curr)
                curr = curr.left
            else:
                curr = tree.pop()
                result.append(curr.value)
                curr = curr.right
        else:
            return result

    @property
    def level_order(self):
        result = []
        tree = deque()  # Queue
        tree.append(self.root)

        while tree:
            curr = tree.popleft()
            result.append(curr.value)
            if curr.left:
                tree.append(curr.left)
            if curr.right:
                tree.append(curr.right)
        else:
            return result
