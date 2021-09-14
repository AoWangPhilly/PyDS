import pytest
from PyDS.LinkedList.DoublyLinkedList import DoublyLinkedList
from PyDS.Error import Empty

NUM_OF_ELEMENTS = 10


@pytest.fixture
def setup():
    empty = DoublyLinkedList()
    doubly_linked_list = DoublyLinkedList()
    for i in range(NUM_OF_ELEMENTS):
        doubly_linked_list.append(i)
    return empty, doubly_linked_list


def test_ll_is_empty(setup):
    empty, _ = setup
    assert empty.is_empty()


def test_ll_is_not_empty(setup):
    _, ll = setup
    assert ll.is_empty() == False


def test_str_with_empty_ll(setup):
    empty, _ = setup
    assert str(empty) == 'DoublyLinkedList([])'


def test_str_after_prepend(setup):
    empty, _ = setup
    for i in range(NUM_OF_ELEMENTS):
        empty.prepend(i)

    assert str(empty) == 'DoublyLinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])'


def test_str_after_append(setup):
    _, ll = setup
    assert str(ll) == 'DoublyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_str_with_prepend_and_append(setup):
    _, ll = setup
    ll.prepend(100)
    assert str(ll) == 'DoublyLinkedList([100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_len_of_ll(setup):
    _, ll = setup
    assert len(ll) == NUM_OF_ELEMENTS


def test_len_of_empty_ll(setup):
    empty, ll = setup
    assert len(empty) == 0


def test_len_after_append(setup):
    _, ll = setup
    ll.append(11)
    assert len(ll) == NUM_OF_ELEMENTS + 1


def test_len_after_prepend(setup):
    _, ll = setup
    ll.prepend(11)
    assert len(ll) == NUM_OF_ELEMENTS + 1


def test_search_for_first_in_full_ll(setup):
    _, ll = setup
    assert ll.search(0) == 0


def test_search_for_last_in_full_ll(setup):
    _, ll = setup
    assert ll.search(NUM_OF_ELEMENTS - 1) == NUM_OF_ELEMENTS - 1


def test_search_for_middle_in_ll(setup):
    _, ll = setup
    assert ll.search(5) == 5


def test_search_for_element_not_in_ll(setup):
    _, ll = setup
    assert ll.search(100) == -1


def test_search_in_empty_ll(setup):
    empty, _ = setup
    assert empty.search(100) == -1
