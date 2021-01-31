import pytest
from code_challenges.tree.tree import Node, BinaryTree, BinarySearchTree


# @pytest.mark.skip("pending")
def test_instantiate_empty_bt():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bt_one_node():
    tree = BinaryTree(Node("A"))
    actual = tree.root.value
    expected = "A"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bt_one_node_plus_left():
    tree = BinaryTree(Node("A", Node("B")))
    actual = tree.root.left.value
    expected = "B"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bt_one_node_plus_left_and_right():
    tree = BinaryTree(Node("A", Node("B"), Node("C")))
    actual = tree.root.right.value
    expected = "C"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bt_pre_order(binary_tree_example, capsys):
    binary_tree_example.pre_order()
    captured = capsys.readouterr()
    assert captured.out == "A\nB\nD\nE\nC\nF\n"


# @pytest.mark.skip("pending")
def test_bt_in_order(binary_tree_example, capsys):
    binary_tree_example.in_order()
    captured = capsys.readouterr()
    assert captured.out == "D\nB\nE\nA\nF\nC\n"


# @pytest.mark.skip("pending")
def test_bt_post_order(binary_tree_example, capsys):
    binary_tree_example.post_order()
    captured = capsys.readouterr()
    assert captured.out == "D\nE\nB\nF\nC\nA\n"


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

    tree = BinaryTree(a)
    tree.root.left = b
    tree.root.right = c

    return tree
