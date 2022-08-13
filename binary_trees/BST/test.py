from BST import BST


def test_empty_tree():
    void = BST()
    assert void.root.value is None


def test_initializing_with_elements():
    tree = BST(5, 2, 3, 1, 7, 6, 8)
    assert tree.level_order == [5, 2, 7, 1, 3, 6, 8]
    assert tree.in_order == [1, 2, 3, 5, 6, 7, 8]
    linear_tree = BST(1, 2, 3, 4, 5, 6, 7, 8)
    assert linear_tree.level_order == [1, 2, 3, 4, 5, 6, 7, 8] == linear_tree.in_order


def test_adding_elements():
    tree = BST()
    # adding a single element
    tree.add_new_elements(2)
    assert tree.in_order == [2] == tree.level_order

    # adding multiple elements
    tree.add_new_elements(1, 3)
    assert tree.in_order == [1, 2, 3]
    assert tree.level_order == [2, 1, 3]


def test_deleting_leaf():
    tree = BST(5, 2, 3, 1, 7, 6, 8)
    tree.root.left.right.delete()
    tree.root.left.left.delete()
    assert tree.in_order == [2, 5, 6, 7, 8]


def test_deleting_sub_root():
    tree = BST(5, 2, 3, 1, 7, 6, 8)
    tree.root.left.delete()
    assert tree.in_order == [1, 3, 5, 6, 7, 8]


def test_deleting_node_with_one_child():
    tree = BST(5, 2, 3, 1, 7, 6)
    tree.root.right.delete()
    assert tree.in_order == [1, 2, 3, 5, 6]


def test_finding_elements():
    tree = BST(15, 10, 20, 25, 5, 2, 3, 1, 7, 6, 8)
    assert tree.find(5) is tree.root.left.left

