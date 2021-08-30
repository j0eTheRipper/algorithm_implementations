from .LinkedList import DoublyLinkedList


def test_initialization():
    x = DoublyLinkedList(1)
    head = x.head
    tail = x.tail

    values = head.value, tail.value, head.next, tail.next, head.back, tail.back

    assert values == (1, 1, None, None, None, None)


def test_head_insertion():
    x = DoublyLinkedList(1)

    x.reverse_append(0)

    values = x.head.value, x.head.next.value, x.tail.value, x.tail.back.value, x.tail.next, x.head.back

    assert values == (0, 1, 1, 0, None, None)


def test_tail_insertion():
    x = DoublyLinkedList(1)
    x.append(2)

    values = x.head.value, x.tail.value, x.head.next.value, x.tail.back.value

    assert values == (1, 2, 2, 1)


def test_len_getter():
    x = DoublyLinkedList(1)
    x.append(2)
    x.reverse_append(0)

    assert len(x) == 3
