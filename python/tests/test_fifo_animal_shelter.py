import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter


def test_enqueue():
    a = AnimalShelter()
    a.enqueue("dog")
    actual = a.dogs.front.value
    expected = "dog"
    assert actual == expected


def test_dequeue():
    a = AnimalShelter()
    a.enqueue("cat")
    actual = a.dequeue("cat")
    expected = "cat"
    assert actual == expected


def test_dequeue_when_empty():
    a = AnimalShelter()
    with pytest.raises(InvalidOperationError) as e:
        a.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"


@pytest.mark.skip("pending")
def test_dequeue_when_full():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


@pytest.mark.skip("pending")
def test_enqueue_two():
    a = AnimalShelter()
    a.enqueue("dog")
    q.enqueue("dog")
    # actual =
    # expected =
    assert actual == expected


@pytest.mark.skip("pending")
def test_peek_post_dequeue():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.first_on_top.top.value
    expected = "bananas"
    assert actual == expected
