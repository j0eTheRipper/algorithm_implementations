from .LinkedList import SinglyLinkedList


def test_initialization():
    ll = SinglyLinkedList(1)
    assert ll.head.value, ll.tail.value == (1, 1)


def test_appending():
    ll = SinglyLinkedList(1)
    ll.append(2)
    ll.append(3)
    check = ll.head.value, ll.tail.value, ll.head.next.value

    assert check == (1, 3, 2)


def test_reverse_appending():
    ll = SinglyLinkedList(1)
    ll.reverse_append(0)

    check = ll.head.value, ll.tail.value, ll.head.next.value

    assert check == (0, 1, 1)


def test_get_item():
    x = [2, 3, 4]
    ll = SinglyLinkedList(1)
    for i in x:
        ll.append(i)

    assert ll[2].value == 3


def test_set_item():
    ll = mkll()

    ll[0] = 3

    assert ll[0].value == 3


def test_delitem():
    ll = mkll()
    del ll[2]

    assert ll[2].value == 4


def test_get_len():
    ll = mkll()
    assert len(ll) == 4


def test_add_in_index():
    ll = mkll()
    ll.insert(1, 1)

    assert ll[1].value == 1


def mkll():
    x = [2, 3, 4]
    ll = SinglyLinkedList(1)
    for i in x:
        ll.append(i)

    return ll
