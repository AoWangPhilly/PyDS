import pytest
from PyDS.LinkedList.LinkedList import LinkedList
from PyDS.Error import Empty

NUM_OF_ELEMENTS = 10


@pytest.fixture
def linked_list():
    ll = LinkedList()
    for i in range(NUM_OF_ELEMENTS):
        ll.append(i)

    return ll


def test_size_of_ll(linked_list):
    assert len(linked_list) == NUM_OF_ELEMENTS


def test_size_of_ll_after_prepend():
    ll = LinkedList()
    for i in range(NUM_OF_ELEMENTS):
        ll.prepend(i)
    assert len(ll) == NUM_OF_ELEMENTS


def test_size_of_empty_ll():
    ll = LinkedList()
    assert len(ll) == 0


def test_size_of_ll_after_append(linked_list):
    test_value = 11
    linked_list.append(test_value)
    assert len(linked_list) == NUM_OF_ELEMENTS + 1


def test_size_with_append_and_prepend():
    ll = LinkedList()
    for i in range(5):
        ll.append(i)

    for i in range(5):
        ll.prepend(i)
    assert len(ll) == NUM_OF_ELEMENTS


def test_search_element_in_ll(linked_list):
    target = 5
    assert linked_list.search(target) == target


def test_search_non_existent_element_in_ll(linked_list):
    target = 99
    assert linked_list.search(target) == -1


def test_search_in_empty_ll():
    ll, target = LinkedList(), 0
    assert ll.search(target) == -1


def test_str_of_empty_ll():
    assert str(LinkedList()) == 'LinkedList([])'


def test_str_of_full_ll(linked_list):
    assert str(linked_list) == 'LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_str_using_prepend():
    ll = LinkedList()
    for i in range(NUM_OF_ELEMENTS):
        ll.prepend(i)
    assert str(ll) == 'LinkedList([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])'


def test_str_with_append_and_prepend():
    ll = LinkedList()
    for i in range(5):
        ll.append(i)

    for i in range(5):
        ll.prepend(i)
    assert str(ll) == 'LinkedList([4, 3, 2, 1, 0, 0, 1, 2, 3, 4])'


def test_get_element_of_first_index_of_ll(linked_list):
    assert linked_list.get_at(0) == 0


def test_get_element_of_last_index_of_ll(linked_list):
    assert linked_list.get_at(NUM_OF_ELEMENTS - 1) == NUM_OF_ELEMENTS - 1


def test_get_element_of_middle_index_of_ll(linked_list):
    assert linked_list.get_at(4) == 4


def test_get_element_of_index_of_empty_ll():
    ll = LinkedList()
    with pytest.raises(Empty):
        ll.get_at(0)


def test_get_element_of_max_index_in_ll(linked_list):
    with pytest.raises(IndexError):
        linked_list.get_at(100)


def test_get_element_of_negative_index_in_ll(linked_list):
    with pytest.raises(IndexError):
        linked_list.get_at(-1)


def test_len_after_remove_front_of_full_ll(linked_list):
    linked_list.remove_front()
    assert len(linked_list) == NUM_OF_ELEMENTS - 1


def test_len_after_multiple_removes_from_front_ll(linked_list):
    linked_list.remove_front()
    linked_list.remove_front()
    assert len(linked_list) == NUM_OF_ELEMENTS - 2


def test_len_after_remove_last_of_full_ll(linked_list):
    linked_list.remove_last()
    assert len(linked_list) == NUM_OF_ELEMENTS - 1


def test_len_after_multiple_removes_from_last_ll(linked_list):
    linked_list.remove_last()
    linked_list.remove_last()
    assert len(linked_list) == NUM_OF_ELEMENTS - 2


def test_str_after_remove_front_of_full_ll(linked_list):
    linked_list.remove_front()
    assert str(linked_list) == 'LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_str_after_multiple_removes_from_front_ll(linked_list):
    linked_list.remove_front()
    linked_list.remove_front()
    assert str(linked_list) == 'LinkedList([2, 3, 4, 5, 6, 7, 8, 9])'


def test_front_remove_with_empty_ll():
    ll = LinkedList()
    with pytest.raises(Empty):
        ll.remove_front()


def test_str_front_remove_with_single_ll():
    ll = LinkedList()
    ll.prepend(1)
    ll.remove_front()
    assert str(ll) == 'LinkedList([])'


def test_prepend_after_remove_from_front(linked_list):
    linked_list.remove_front()
    linked_list.prepend(100)
    assert str(linked_list) == 'LinkedList([100, 1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_append_after_remove_from_front(linked_list):
    linked_list.remove_front()
    linked_list.append(100)
    assert str(linked_list) == 'LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])'


def test_str_remove_last_with_full_ll(linked_list):
    linked_list.remove_last()
    assert str(linked_list) == 'LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8])'


def test_str_remove_last_multiple_times_with_full_ll(linked_list):
    linked_list.remove_last()
    linked_list.remove_last()
    assert str(linked_list) == 'LinkedList([0, 1, 2, 3, 4, 5, 6, 7])'

# def test_str_deletion_with_full_ll(linked_list):
#     linked_list.delete(0)
#     assert str(linked_list) == 'LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])'
#
#
# def test_str_deletion_of_empty_ll():
#     ll = LinkedList()
#     with pytest.raises(Empty):
#         ll.delete(0)
#
#
# def test_size_after_deletion_ll(linked_list):
#     linked_list.delete(5)
#     assert len(linked_list) == NUM_OF_ELEMENTS - 1
