import json
from code_challenges.stacks_and_queues.stacks_and_queues import Queue

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

    def find_maximun_value(self):
        max_value = 0

        def traverse(root):
            """[helper function used to recursively traverse the binary tree]

            Args:
                root ([type]): [root you want to traverse]
            """
            nonlocal max_value

            # if there is no node here then exit
            if not root:  # base case
                return max_value
            # check if root value is > max_value
            print(f"root: {root.value}")
            print(f"max: {max_value}")

            if root.value > max_value:
                max_value = root.value
            # traverse left
            traverse(root.left)
            # traverse right
            traverse(root.right)

        traverse(self.root)
        return max_value

    def breadth_first(self):

        breadth_first_list = []

        if not self.root:
            return breadth_first_list

        breadth_queue = Queue()
        breadth_queue.enqueue(self.root)

        while breadth_queue.front is not None:

            current = breadth_queue.dequeue()

            if current.left is not None:
                breadth_queue.enqueue(current.left)

            if current.right is not None:
                breadth_queue.enqueue(current.right)

            breadth_first_list.append(current.value)

        return breadth_first_list


class BinarySearchTree(BinaryTree):
    """Binary Search Tree Class"""

    def add(self, add_value: int):
        """[adds node to BST]

        Args:
            add_value (int): [Value you want to add]

        Returns:
            [type]: [Return string if value already exists]
        """

        if not self.root:
            self.root = Node(add_value)
            return

        def traverse(root, value):
            """[helper function used to recursively traverse the binary search tree]

            Args:
                root ([type]): [root you want to traverse]
                value ([type]): [Value you want to add]
            """
            # if value already exists
            if root.value == value:
                return "Value already exsits in BST"
            print(root.value)

            if value > root.value:
                if not root.right:
                    root.right = Node(value)
                    print(root.right.values)
                else:
                    traverse(root.right, value)

            if value < root.value:
                if not root.left:
                    root.left = Node(value)
                    print(root.left.value)
                else:
                    traverse(root.left, value)

        return traverse(self.root, add_value)

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
