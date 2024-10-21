def get_min_value(node):
    """
    Returns the smallest key in a binary search tree (BST).

    This function moves down the left side of the tree to find the smallest key, 
    since the smallest values in a BST are located in the leftmost nodes.

    Parameters:
        node (TreeNode): The starting node of the tree where the search begins.

    Returns:
        key (any): The key of the smallest node.
    """
    while node.left:
        node = node.left
    return node.key
