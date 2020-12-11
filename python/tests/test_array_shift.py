from array_shift.array_shift import insertShiftArray

def test_insert_shift_array_empty_array():
  actual = insertShiftArray([],1)
  expected = [1]
  assert actual == expected

def test_insert_shift_array_one_index_array():
  actual = insertShiftArray([0],1)
  expected = [0,1]
  assert actual == expected

def test_insert_shift_array_float():
  actual = insertShiftArray([1,1,2],1.5)
  expected = [1,1,1.5,2]
  assert actual == expected

def test_insert_shift_array_larger_array():
  actual = insertShiftArray([1,2,3,4,5,7,8,9,10],6)
  expected = [1,2,3,4,5,6,7,8,9,10]
  assert actual == expected

# def test_insert_shift_array_not_array():
#   actual = insertShiftArray((1,2,3), 1)
#   expected = 
#   assert actual == expected