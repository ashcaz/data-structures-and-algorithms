import pytest

from code_challenges.tree_intersection.tree_intersection import numbers_in_common
from code_challenges.tree.tree import BinaryTree, Node


def test_empty_tree(bt_1, bt_empty):
    actual = numbers_in_common(bt_1, bt_empty)
    expected = []
    assert actual == expected


def test_common_values(bt_1, bt_2):
    actual = numbers_in_common(bt_1, bt_2)
    expected = ["A", "B"]
    assert actual == expected


def test_common_values_fail(bt_1, bt_2):
    actual = numbers_in_common(bt_1, bt_2)
    expected = ["A", "F"]
    assert actual != expected


#######################
# Fixtures
#######################


@pytest.fixture
def bt_1():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree(a)
    tree.root.left = b
    tree.root.right = c

    return tree


@pytest.fixture
def bt_2():
    a = Node("A")
    b = Node("B")
    c = Node("G")
    d = Node("H")
    e = Node("I")
    f = Node("J")

    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree(a)
    tree.root.left = b
    tree.root.right = c

    return tree


@pytest.fixture
def bt_empty():

    return BinaryTree()