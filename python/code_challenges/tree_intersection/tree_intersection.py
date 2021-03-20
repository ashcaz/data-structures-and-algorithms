def numbers_in_common(tree_1, tree_2) -> list:

    if not tree_2.root or not tree_1.root:
        return []

    tree_1_list = []
    common_values = []

    def traverse(root):
        """[helper function used to recursively traverse the binary tree]

        Args:
            root ([type]): [root you want to traverse]
        """
        # if there is no node here then exit
        if not root:  # base case
            return
        # print root first
        tree_1_list.append(root.value)
        # traverse left
        traverse(root.left)
        # traverse right
        traverse(root.right)

    traverse(tree_1.root)

    def traverse_2(root):
        """[helper function used to recursively traverse the binary tree]

        Args:
            root ([type]): [root you want to traverse]
        """
        # if there is no node here then exit
        if not root:  # base case
            return

        if root.value in tree_1_list:
            common_values.append(root.value)

        # traverse left
        traverse_2(root.left)
        # traverse right
        traverse_2(root.right)

    traverse_2(tree_2.root)

    return common_values