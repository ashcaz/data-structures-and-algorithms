import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter
from code_challenges.stacks_and_queues.stacks_and_queues import InvalidOperationError


def test_enqueue_dog():
    a = AnimalShelter()
    a.enqueue("dog")
    actual = a.dogs.front.value
    expected = "dog"
    assert actual == expected


def test_enqueue_cat():
    a = AnimalShelter()
    a.enqueue("cat")
    actual = a.cats.front.value
    expected = "cat"
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
        a.dequeue("dog")

    assert str(e.value) == "Method not allowed on empty collection"


def test_not_cat_or_dog():
    a = AnimalShelter()
    with pytest.raises(InvalidOperationError) as e:
        a.enqueue("pig")

    assert str(e.value) == "We only have cats and dogs at this shelter!"
