# Node based data structure

class Node:
    ''' We need to point to two other nodes ina a Binary Tree so the Node must have two pointers
        Traditionally they are called 'left' and 'right'
    '''
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """Binary Tree Class"""
    def __init__(self, root = None):
      """[instantiates a binary tree]

      Args:
          root ([type], optional): [root node]. Defaults to None.
      """
        self.root = root

    def pre_order(self):
      """[summary]
      """
        def traverse(root):
          """[summary]

          Args:
              root ([type]): [description]
          """
            # if there is no node here then exit
            if not root: # base case
                return
            # print root first
            print(root.value)
            # traverse left
            traverse(root.left)
            # traverse right
            traverse(root.right)
        traverse(self.root)

    def in_order(self):
      """[summary]
      """
        def traverse(root):
          """[summary]

          Args:
              root ([type]): [description]
          """
            # traverse left first
            if root.left:
                traverse(root.left)
            # operate on root second
            print(root.value)
            # traverse right last
            if root.right:
                traverse(root.right)
        traverse(self.root)

    def post_order(self):
      """[summary]
      """
        def traverse(root):
          """[summary]

          Args:
              root ([type]): [description]
          """
            # traverse left first
            if root.left:
                traverse(root.left)
            # traverse right last
            if root.right:
                traverse(root.right)
            # operate on last
            print(root.value)
        traverse(self.root)

class BinarySearchTree(BinaryTree):
    def add(self, value):
        # find the correct spot to add this value and add it there
        pass

    def contains(self,value):
        # return true if the value is in the tree or false otherwise
        pass
