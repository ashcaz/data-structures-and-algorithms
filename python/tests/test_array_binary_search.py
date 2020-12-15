from code_challenges.array_binary_search.array_binary_search import BinarySearch

def test_empty_array():
  actual = BinarySearch([], 2)
  expected = -1
  assert actual == expected

def test_one_index_array():
  actual = BinarySearch([1], 1)
  expected = 0
  assert actual == expected

def test_search_key_at_middle():
  actual = BinarySearch([1,2,3,4,5], 3)
  expected = 2
  assert actual == expected

def test_search_key_not_found():
  actual = BinarySearch([1,2,3,4,5,6], 7)
  expected = -1
  assert actual == expected

def test_larger_array():
  actual = BinarySearch(list(range(1,41)), 16)
  expected = 15
  assert actual == expected