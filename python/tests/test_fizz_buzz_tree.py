import pytest
from code_challenges.fizz_buzz_tree.fizz_buzz_tree import Node, KTree, fizzbuzz_tree

# @pytest.mark.skip("pending")
def test_fb_empty():
    tree = KTree()
    actual = fizzbuzz_tree(tree)
    expected = []
    assert actual == expected


# @pytest.mark.skip("pending")
def test_fb_one(ktree_example):
    actual = fizzbuzz_tree(ktree_example)
    expected = ["1", "2", "Buzz", "Fizz", "Fizz", "7", "Buzz", "4", "FizzBuzz", "41"]
    assert actual == expected


#######################
# Fixtures
#######################


@pytest.fixture
def ktree_example():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(10)
    i = Node(30)
    j = Node(41)

    b.children.append(e)
    b.children.append(f)

    c.children.append(g)
    c.children.append(h)

    d.children.append(i)
    d.children.append(j)

    tree = KTree(a)
    tree.root.children.append(b)
    tree.root.children.append(c)
    tree.root.children.append(d)

    return tree