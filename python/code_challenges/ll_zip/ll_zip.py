from linked_list.linked_list import LinkedList, Node


def zip_lists(list1, list2):
  """[summary]

  Args:
      list1 ([type]): [description]
      list2 ([type]): [description]
  """
  ll1_current = list1.head
  ll2_current = list2.head
  temp = ll2_current.next

  while ll1_current is not None:
    if ll1_current == None or ll2_current == None:
      ll2_current.next = ll1_current.next
      ll1_current.next = ll2_current
      return  list1
    else:
      temp = temp.next
      ll2_current.next = ll1_current.next
      ll1_current.next = ll2_current

      ll1_current = ll1_current.next.next
      ll2_current = ll2_current.next

  return list1

      
