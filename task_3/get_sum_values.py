def get_sum_values(node):
    """
    Calculate the sum of all values in a AVL-tree.

    This function traverses the entire tree, recursively summing the 
    values of all nodes. It considers the current node's key and 
    includes the sums from the left and right subtrees.

    Parameters:
        node (TreeNode): The root node of the AVL-tree or a subtree. 
                         If the node is None, the function 
                         returns 0.

    Returns:
        int: The total sum of all node values in the BST.
    """
    if node is None:
        return 0
    
    return get_sum_values(node.left) + node.key + get_sum_values(node.right)