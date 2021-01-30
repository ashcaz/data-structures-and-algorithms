import pytest
from code_challenges.tree.tree import BinarySearchTree, BinaryTree, Node


@pytest.mark.skip("pending")
def test_instantiate_empty_ll():
    empty_linked_list = LinkedList()
    actual = empty_linked_list.length
    expected = 0
    assert actual == expected


#######################
# Fixtures
#######################


@pytest.fixture
def binary_tree_example():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree(Node(a, b, c))
    return tree
