import pytest
from PyDS.Stack import Stack
from PyDS.Error import Empty

NUM_OF_ELEMENTS = 10


@pytest.fixture
def stack():
    s = Stack()
    for i in range(NUM_OF_ELEMENTS):
        s.push(i)
    return s


def test_has_correct_size(stack):
    assert len(stack) == NUM_OF_ELEMENTS


def test_size_after_push(stack):
    test_value = 10
    stack.push(test_value)
    assert len(stack) == NUM_OF_ELEMENTS + 1


def test_size_after_multiple_push(stack):
    test_value1, test_value2 = 99, 100
    stack.push(test_value1)
    stack.push(test_value2)
    assert len(stack) == NUM_OF_ELEMENTS + 2


def test_size_after_pop(stack):
    stack.pop()
    assert len(stack) == NUM_OF_ELEMENTS - 1


def test_size_after_multiple_pop(stack):
    stack.pop()
    stack.pop()
    assert len(stack) == NUM_OF_ELEMENTS - 2


def test_top_value(stack):
    assert stack.top() == NUM_OF_ELEMENTS - 1


def test_top_value_after_push(stack):
    random_top = 99
    stack.push(random_top)
    assert stack.top() == random_top


def test_top_value_after_pop(stack):
    stack.pop()
    assert stack.top() == NUM_OF_ELEMENTS - 2


def test_pop_return_value(stack):
    assert stack.pop() == NUM_OF_ELEMENTS - 1


def test_stack_not_empty(stack):
    assert not stack.is_empty()


def test_empty_stack_with_pop():
    s = Stack()
    with pytest.raises(Empty):
        s.pop()


def test_empty_stack_with_top():
    s = Stack()
    with pytest.raises(Empty):
        s.top()


def test_stack_is_empty():
    s = Stack()
    assert s.is_empty()


def test_stack_is_empty_after_pop(stack):
    for _ in range(NUM_OF_ELEMENTS):
        stack.pop()
    assert stack.is_empty()


def test_stack_is_empty_after_too_many_pop(stack):
    with pytest.raises(Empty):
        for _ in range(NUM_OF_ELEMENTS + 1):
            stack.pop()


def test_str_with_empty_stack():
    s = Stack()
    assert str(s) == 'Stack([])'


def test_str_with_full_stack(stack):
    assert str(stack) == 'Stack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_str_after_pop(stack):
    for _ in range(5):
        stack.pop()
    assert str(stack) == 'Stack([0, 1, 2, 3, 4])'


def test_eq_with_full_stack(stack):
    s = Stack()
    for i in range(NUM_OF_ELEMENTS):
        s.push(i)
    assert s == stack


def test_eq_with_two_empty_stacks():
    s1, s2 = Stack(), Stack()
    assert s1 == s2


def test_eq_after_push(stack):
    s = Stack()
    for i in range(NUM_OF_ELEMENTS):
        s.push(i)

    stack.push(11)
    assert s != stack


def test_eq_after_pop(stack):
    s = Stack()
    for i in range(NUM_OF_ELEMENTS):
        s.push(i)

    stack.pop()
    assert s != stack


def test_capacity_limit():
    s = Stack()
    for i in range(64):
        s.push(i)
    assert s._Stack__capacity == 64


def test_capacity_over_limit():
    s = Stack()
    for i in range(65):
        s.push(i)
    assert s._Stack__capacity == 64 * 2


def test_len_after_resizing():
    s = Stack()
    for i in range(100):
        s.push(i)
    assert len(s) == 100


def test_cap_after_pop():
    s = Stack()
    for i in range(64):
        s.push(i)

    for i in range(50):
        s.pop()

    assert s._Stack__capacity == 32


def test_cap_after_multiple_pops():
    s = Stack()
    for i in range(10):
        s.push(i)

    s.pop()
    s.pop()
    s.pop()
    s.pop()

    assert s._Stack__capacity == 16
