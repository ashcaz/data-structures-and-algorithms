# Stack
# Only the top node is accessible
# both read and write

# Adding an item to the stack O(1)

# Retrieving an item form the stack also

class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack():
  """ Stack Class """
    # FILO
  def __init__(self, node = None):
    """[Stack Constrctor function. Takes in a node. Instantiate an empty stack by not providing a node]

    Args:
        node ([type], optional): [description]. Defaults to None.
    """
    self.top = node
    
  def push(self, value):
    """[Adds a new node to the stack]

    Args:
        value ([type]): [description]
    """
    # create node from value
    node = Node(value)
    # point new node to top
    node.next = self.top
    # assign node to top
    self.top = node
  
  def pop(self):
    """[Removes the top node from the stack]

    Raises:
        InvalidOperationError: [raises exception if you try to perform this method on an empty stack]

    Returns:
        [type]: [Returns the value of the node removed]
    """
    if self.is_empty():
        raise InvalidOperationError("Method not allowed on empty collection")
    # create temp node
    # assign top to the temp node
    node = self.top
    # top reassign it to top.next
    self.top = self.top.next
    # return value of temp node
    return node.value
  
  def peek(self):
    """[Check the value of the top node in the stack]

    Raises:
        InvalidOperationError: [raises exception if you try to perform this method on an empty stack]

    Returns:
        [type]: [Returns the value of the top node]
    """
    #check if stack is empty
    if self.is_empty():
        raise InvalidOperationError("Method not allowed on empty collection")

    return self.top.value
  
  def is_empty(self) -> bool:
    """[Checks if stack is empty]

    Returns:
        bool: [If stack is empty]
    """
    if not self.top:
      return True
    
    return False


    

class Queue():
      # FIFO
      # LILO
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, value):
    # create node from value
    node = Node(value)
    #Check to see if node is empty
    if self.is_empty():
      # if empty add assign to front and rear
      self.front, self.rear = node, node
    else:
      #if queue has a front add the node to the rear
      self.rear.next = node
      self.rear = node

  def dequeue(self):
    #Check if empty
    if self.is_empty():
      raise InvalidOperationError("Method not allowed on empty collection")

    # create temp node
    # assign top to the temp node
    node = self.front
    # top reassign it to top.next
    self.front = self.front.next

    # return value of temp node
    return node.value

  def is_empty(self):
    if not self.front:
      return True
    
    return False