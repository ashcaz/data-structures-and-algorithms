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


# @pytest.mark.skip("pending")
def test_bst_contains_empty():
    tree = BinarySearchTree()
    actual = tree.contains(5)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bst_contains_less(bst_example):
    actual = bst_example.contains(12)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bst_contains_greater(bst_example):
    actual = bst_example.contains(95)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bst_contains_false(bst_example):
    actual = bst_example.contains(7)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bst_add_to_empty():
    tree = BinarySearchTree()
    tree.add(5)
    actual = tree.root.value
    expected = 5
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bst_already_exists(bst_example):
    actual = bst_example.add(25)
    expected = "Value already exsits in BST"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_bst_add_to_left(bst_example, capsys):
    bst_example.add(15)
    captured = capsys.readouterr()
    assert captured.out == "25\n12\n16\n15\n"


# @pytest.mark.skip("pending")
def test_bst_add_to_right(bst_example, capsys):
    bst_example.add(72)
    captured = capsys.readouterr()
    assert captured.out == "25\n44\n95\n72\n"


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


@pytest.fixture
def bst_example():
    a = Node(25)
    b = Node(3)
    c = Node(16)
    d = Node(12)
    e = Node(32)
    f = Node(44)
    g = Node(95)

    d.left = b
    d.right = c
    f.left = e
    f.right = g

    tree = BinarySearchTree(a)
    tree.root.left = d
    tree.root.right = f

    return tree


@pytest.fixture
def bt_max():
    a = Node(2)
    b = Node(7)
    c = Node(5)
    d = Node(2)
    e = Node(6)
    f = Node(5)
    g = Node(11)
    h = Node(9)
    i = Node(4)

    b.left = d
    b.right = e
    e.left = f
    e.right = g
    c.left = h
    h.left = i

    tree = BinarySearchTree(a)
    tree.root.left = b
    tree.root.right = c

    return tree