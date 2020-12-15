
def insertShiftArray(array: list,n:int) -> list:
  """[Takes in an array and a number and add the number to the midpoint of the array]

  Args:
      array (list): [list of numbers]
      n (int): [number to insert]

  Returns:
      list: [returns list with number inserted at the midpoint]
  """
  midpoint = int(len(array)/ 2)
  
  if not len(array)%2:
    array.insert(midpoint, n)
    return array
  else:
    array.insert(midpoint + 1, n)
    return array

