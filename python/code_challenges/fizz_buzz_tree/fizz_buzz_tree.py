class Node:
    """We need to point to two other nodes ina a Binary Tree so the Node must have two pointers
    Traditionally they are called 'left' and 'right'
    """

    def __init__(self, value=None):
        self.value = value
        self.children = []


class KTree:
    """K-ary Tree Class"""

    def __init__(self, root=None):
        """[construtor funtion for instantiation of a binary tree]

        Args:
            root ([type], optional): [root node]. Defaults to None.
        """
        self.root = root


def fizzbuzz_tree(ktree):

    new_ktree = ktree
    tree_list = []

    def traverse(root):

        nonlocal tree_list

        if not root:
            return

        print(root.value)

        if not root.value % 15:
            root.value = "FizzBuzz"
        elif not root.value % 5:
            root.value = "Buzz"
        elif not root.value % 3:
            root.value = "Fizz"
        else:
            root.value = str(root.value)

        tree_list.append(root.value)
        print(tree_list)

        for i in range(len(root.children)):
            traverse(root.children[i])

        return

    traverse(new_ktree.root)

    return tree_list