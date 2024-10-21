def get_max_value(node):
    """
    Returns the biggest key in a AVL-tree.

    This function moves down the left side of the tree to find the biggest key, 
    since the biggest values in a AVL-tree are located in the rightmost nodes.

    Parameters:
        node (TreeNode): The starting node of the tree where the search begins.

    Returns:
        key (any): The key of the biggest node.
    """
    while node.right:
        node = node.right
    return node.key
