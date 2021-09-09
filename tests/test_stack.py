import pytest
from PyDS.Stack import Stack

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

def test_length_after_pop(stack):
    stack.pop()
    assert len(stack) == NUM_OF_ELEMENTS - 1

def test_stack_not_empty(stack):
    assert not stack.is_empty()

def test_stack_is_empty():
    s = Stack()
    assert s.is_empty()

def test_stack_is_empty_after_pop(stack):
    for _ in range(NUM_OF_ELEMENTS):
        stack.pop()
    assert stack.is_empty()

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