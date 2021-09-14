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


def test_remove_front_with_empty_ll(setup):
    empty, _ = setup
    with pytest.raises(Empty):
        empty.remove_front()


def test_len_after_remove_front(setup):
    _, ll = setup
    ll.remove_front()
    assert len(ll) == NUM_OF_ELEMENTS - 1


def test_str_after_remove_front(setup):
    _, ll = setup
    ll.remove_front()
    assert str(ll) == 'DoublyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_str_after_remove_front_of_ll_with_single_element(setup):
    empty, _ = setup
    empty.append(1)
    empty.remove_front()
    assert str(empty) == 'DoublyLinkedList([])'


def test_remove_end_with_empty_ll(setup):
    empty, _ = setup
    with pytest.raises(Empty):
        empty.remove_end()


def test_str_with_remove_end_with_ll(setup):
    _, ll = setup
    ll.remove_end()
    assert str(ll) == 'DoublyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8])'


def test_len_with_remove_end_with_ll(setup):
    _, ll = setup
    ll.remove_end()
    assert len(ll) == NUM_OF_ELEMENTS - 1


def test_str_with_remove_end_with_ll_of_only_one_element(setup):
    empty, _ = setup
    empty.append(1)
    empty.remove_end()
    assert str(empty) == 'DoublyLinkedList([])'


def test_remove_element_from_empty(setup):
    empty, _ = setup
    with pytest.raises(Empty):
        empty.remove(0)


def test_len_remove_element_non_existent_in_ll(setup):
    _, ll = setup
    ll.remove(100)
    assert len(ll) == NUM_OF_ELEMENTS


def test_len_remove_element_from_front_ll(setup):
    _, ll = setup
    ll.remove(0)
    assert len(ll) == NUM_OF_ELEMENTS - 1


def test_len_remove_element_from_end_ll(setup):
    _, ll = setup
    ll.remove(9)
    assert len(ll) == NUM_OF_ELEMENTS - 1


def test_len_remove_element_from_middle_ll(setup):
    _, ll = setup
    ll.remove(5)
    assert len(ll) == NUM_OF_ELEMENTS - 1


def test_str_remove_elements_from_front_ll(setup):
    _, ll = setup
    ll.remove(0)
    assert str(ll) == 'DoublyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_str_remove_element_from_end_ll(setup):
    _, ll = setup
    ll.remove(9)
    assert str(ll) == 'DoublyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8])'


def test_str_remove_element_from_middle_ll(setup):
    _, ll = setup
    ll.remove(5)
    assert str(ll) == 'DoublyLinkedList([0, 1, 2, 3, 4, 6, 7, 8, 9])'


def test_str_free_for_all(setup):
    _, ll = setup
    ll.remove_front()
    ll.remove_end()
    ll.remove(3)
    ll.remove(6)
    ll.prepend(99)
    ll.append(100)
    assert str(ll) == 'DoublyLinkedList([99, 1, 2, 4, 5, 7, 8, 100])'
