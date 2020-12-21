import pytest

from linked_list.linked_list import Node, LinkedList


def test_import():
    assert LinkedList

# @pytest.mark.skip("pending")
def test_instantiate_empty_ll():
  node = Node(1)
  LinkedList(node)
  actual = LinkedList.ll_total()
  expected = 1
  assert actual == expected

@pytest.mark.skip("pending")
def test_insert_into_ll():
  node = Node(1)
  new_ll = LinkedList(node)
  print(new_ll)
  actual = new_ll.insert(2)
  expected = -1
  assert actual == expected

# @pytest.mark.skip("pending")
def test_head_ll(linked_list_one):
  actual = linked_list_one.includes(1)
  expected = True
  assert actual == expected

@pytest.mark.skip("pending")
def test_insert_multiple_nodes_ll():
  node = Node(1)
  actual = LinkedList(node)
  expected = -1
  assert actual == expected

@pytest.mark.skip("pending")
def test_value_found_in_ll():
  node = Node(1)
  actual = LinkedList(node)
  expected = -1
  assert actual == expected

@pytest.mark.skip("pending")
def test_value_not_found_in_ll():
  node = Node(1)
  actual = LinkedList(node)
  expected = -1
  assert actual == expected

@pytest.mark.skip("pending")
def test_return_collection_of_values():
  node = Node(1)
  actual = LinkedList(node)
  expected = -1
  assert actual == expected


#######################
# Fixtures
#######################

@pytest.fixture
def linked_list_one():
    node = Node(0)
    linked_list = LinkedList(node)
    node_values = list(range(1,10))
    for num in node_values:
        linked_list.insert(num)
    
    return linked_list
        


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    LinkedList.instances = 0