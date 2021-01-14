import pytest
from code_challenges.queue_with_stacks.queue_with_stacks import (
    PseudoQueue,
    InvalidOperationError,
)


def test_enqueue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.last_on_top.top.value
    expected = "apple"
    assert actual == expected


def test_dequeue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_dequeue_with_one_node():
    q = PseudoQueue()
    q.enqueue("apple")
    q.dequeue()
    actual = q.last_on_top.top
    expected = None
    assert actual == expected


# @pytest.mark.skip("pending")
def test_enqueue_two():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.last_on_top.top.value
    expected = "bananas"
    assert actual == expected


def test_dequeue_when_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError) as e:
        q.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"


def test_dequeue_when_full():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_peek_post_dequeue():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.first_on_top.top.value
    expected = "bananas"
    assert actual == expected
