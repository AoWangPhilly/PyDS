import pytest
from PyDS.Queue import Queue
from PyDS.Error import Empty

NUM_OF_ELEMENTS = 10


@pytest.fixture()
def queue():
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    return q


def test_size_of_queue(queue):
    assert len(queue) == NUM_OF_ELEMENTS


def test_size_of_queue_after_enqueue(queue):
    test_value = 11
    queue.enqueue(test_value)
    assert len(queue) == NUM_OF_ELEMENTS + 1


def test_size_of_queue_after_dequeue(queue):
    queue.dequeue()
    assert len(queue) == NUM_OF_ELEMENTS - 1


def test_queue_is_empty():
    q = Queue()
    assert q.is_empty()


def test_empty_queue_after_dequeue():
    q = Queue()
    with pytest.raises(Empty):
        q.dequeue()


def test_empty_queue_after_front():
    q = Queue()
    with pytest.raises(Empty):
        q.front()


def test_front_with_queue(queue):
    assert queue.front() == 0


def test_empty_queue_with_dequeue(queue):
    for _ in range(NUM_OF_ELEMENTS):
        queue.dequeue()

    assert queue.is_empty()


def test_return_value_from_dequeue(queue):
    assert queue.dequeue() == 0


def test_str_with_full_queue(queue):
    assert str(queue) == 'Queue([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_str_with_empty_queue():
    q = Queue()
    assert str(q) == 'Queue([])'


def test_str_after_enqueue(queue):
    test_value = 11
    queue.enqueue(test_value)
    assert str(queue) == 'Queue([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11])'


def test_str_after_dequeue(queue):
    queue.dequeue()
    assert str(queue) == 'Queue([1, 2, 3, 4, 5, 6, 7, 8, 9])'


def test_capacity_with_size_below_cap(queue):
    assert queue._Queue__capacity == 64


def test_capacity_with_size_at_cap():
    q = Queue()
    for i in range(64):
        q.enqueue(i)
    assert q._Queue__capacity == 64


def test_capacity_with_size_beyond_cap():
    q = Queue()
    for i in range(65):
        q.enqueue(i)
    assert q._Queue__capacity == 128
