class Node:
    """We need to point to two other nodes ina a Binary Tree so the Node must have two pointers
    Since this is a K-ary Tree a node can have more then one child. So the children are placed into an list named self.children
    """

    def __init__(self, value=None):
        self.value = value
        self.children = []


class KTree:
    """K-ary Tree Class"""

    def __init__(self, root=None):
        """[construtor funtion for instantiation of a k-ary Tree]

        Args:
            root ([type], optional): [root node]. Defaults to None.
        """
        self.root = root


def fizzbuzz_tree(ktree):
    """[Takes in a k-ary Tree and applies FizzBuzz to the values of the tree]

    Args:
        ktree ([type]): [K-ary Tree]

    Returns:
        [type]: [K-ary Tree]
    """

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