import json

# Node based data structure


class Node:
    """We need to point to two other nodes ina a Binary Tree so the Node must have two pointers
    Traditionally they are called 'left' and 'right'
    """

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """Binary Tree Class"""

    def __init__(self, root=None):
        """[construtor funtion for instantiation of a binary tree]

        Args:
            root ([type], optional): [root node]. Defaults to None.
        """
        self.root = root

    def pre_order(self):
        """[Method that traverses binary tree root first ex. root >> left >> right]"""

        def traverse(root):
            """[helper function used to recursive traverse the binary tree]

            Args:
                root ([type]): [root you want to traverse]
            """
            # if there is no node here then exit
            if not root:  # base case
                return
            # print root first
            print(root.value)
            # traverse left
            traverse(root.left)
            # traverse right
            traverse(root.right)

        traverse(self.root)

    def in_order(self):
        """[Method that traverses binary tree from left to right root second ex. left >> root >> right]"""

        def traverse(root):
            """[helper function used to recursive traverse the binary tree]

            Args:
                root ([type]): [root you want to traverse]
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
        """[Method that traverses binary tree from left to right root last ex. left >> right >> root]"""

        def traverse(root):
            """[helper function used to recursive traverse the binary tree]

            Args:
                root ([type]): [root you want to traverse]
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
    def add(self, value: int):
        # find the correct spot to add this value and add it there
        pass

    def contains(self, value: int) -> bool:
        """[return true if the value is in the tree]

        Args:
            value (int): [vaule you want to search for]

        Returns:
            bool: [Returns true is value is found in the tree]
        """

        def traverse(root, value):
            """[helper function used to recursively traverse the binary tree]

            Args:
                root ([type]): [root you want to traverse]
            """

            if root is not None:  # base case

                # if values is equal to root return true
                if root.value == value:
                    return True
                # if value is less than root traverse left
                if value < root.value:
                    return traverse(root.left, value)
                # if value is greater than root then traverse right
                if value > root.value:
                    return traverse(root.right, value)
            # if there is no node here then exit
            return False

        return traverse(self.root, value)
