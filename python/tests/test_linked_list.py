import pytest

from linked_list.linked_list import Node, LinkedList


def test_import():
    assert LinkedList

# @pytest.mark.skip("pending")
def test_instantiate_empty_ll():
  empty_linked_list = LinkedList()
  actual = empty_linked_list.length
  expected = 0
  assert actual == expected

# @pytest.mark.skip("pending")
def test_insert_into_ll(long_linked_list):
  length = long_linked_list.length
  long_linked_list.insert(22)
  actual = long_linked_list.length
  expected = length+1
  assert actual == expected

# @pytest.mark.skip("pending")
def test_head_ll(short_linked_list):
  short_linked_list.insert(27)
  actual = short_linked_list.head.value
  expected = 27
  assert actual == expected
  

# @pytest.mark.skip("pending")
def test_insert_multiple_nodes_ll():
  node = Node(1)
  ll = LinkedList(node)
  ll.insert(2)
  ll.insert(25)
  ll.insert(102)
  actual = ll.length
  expected = 4
  assert actual == expected

# @pytest.mark.skip("pending")
def test_value_found_in_ll(long_linked_list):
  actual = long_linked_list.includes(1)
  expected = True
  assert actual == expected

# @pytest.mark.skip("pending")
def test_value_not_found_in_ll(long_linked_list):
  actual = long_linked_list.includes(22)
  expected = False
  assert actual == expected

# @pytest.mark.skip("pending")
def test_return_collection_of_values(short_linked_list):
  actual = short_linked_list.create_collection()
  expected = [2,1,0]
  assert actual == expected


#######################
# Fixtures
#######################

@pytest.fixture
def long_linked_list():
    node = Node(0)
    linked_list = LinkedList(node)
    node_values = list(range(1,10))
    for num in node_values:
        linked_list.insert(num)
    
    return linked_list

@pytest.fixture
def short_linked_list():
    node = Node(0)
    linked_list = LinkedList(node)
    node_values = list(range(1,3))
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