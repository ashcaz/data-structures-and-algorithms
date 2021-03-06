def BinarySearch(sorted_array:list, search_key:int) -> int:
  """[Function takes in a sorted array and a search key and returns the index of the search key]

  Args:
      sorted_array (list): [sorted list]
      search_key (int): [the value the function searches for in the array]

  Returns:
      int: [the index of the seach key. If the search key is not found the function will return -1]
  """
  start = 0
  end = len(sorted_array)
  mid = end // 2
  print(start, mid, end, search_key)
   
  if end == 1:
    return 0
  if end == 0:
    return -1

  try:
    while mid >=1:
      if search_key == sorted_array[mid]:
        return mid
      elif search_key < sorted_array[mid]:
          end = mid -1
          mid = (end + start) // 2
      elif search_key > sorted_array[mid]:
          start = mid +1
          mid = (end + start) // 2
        
  except IndexError:
    return -1