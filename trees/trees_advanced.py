"""
TREES - Advanced Topics
=======================

Advanced tree problems:
1. Path problems
2. Tree construction
3. Tree diameter and height
4. Lowest Common Ancestor
5. Tree serialization
"""


def path_sum(root, target_sum):
    """
    TODO: Path Sum
    - Check if root-to-leaf path exists with given sum
    - Return True if exists, False otherwise
    
    Hint:
    - Subtract current value from target
    - Base case: leaf node and sum == 0
    - Recursively check left and right
    """
    pass


def path_sum_ii(root, target_sum):
    """
    TODO: Path Sum II
    - Find all root-to-leaf paths with given sum
    - Return list of paths
    
    Hint:
    - Use backtracking
    - Add current node to path
    - When leaf reached and sum matches, add path to result
    - Remove node when backtracking
    """
    pass


def max_path_sum(root):
    """
    TODO: Binary Tree Maximum Path Sum
    - Path can start and end anywhere
    - Return maximum path sum
    
    Hint:
    - For each node, calculate:
      1. Max path through node (can split at node)
      2. Max path ending at node (for parent)
    - Update global maximum
    """
    pass


def build_tree(preorder, inorder):
    """
    TODO: Construct Binary Tree from Preorder and Inorder
    - Given two traversals, build the tree
    
    Hint:
    - First element of preorder is root
    - Find root in inorder to split left/right
    - Recursively build left and right subtrees
    """
    pass


def lca_binary_tree(root, p, q):
    """
    TODO: Lowest Common Ancestor in Binary Tree (not BST)
    - Return LCA of nodes p and q
    
    Hint:
    - If root is None or p or q, return root
    - Recursively find LCA in left and right
    - If both return non-None, root is LCA
    - Otherwise return non-None result
    """
    pass


def diameter_of_tree(root):
    """
    TODO: Diameter of Binary Tree
    - Longest path between any two nodes
    - May or may not pass through root
    
    Hint:
    - For each node, calculate:
      - Height of left subtree
      - Height of right subtree
      - Diameter through this node
    - Track maximum diameter
    """
    pass


def serialize_tree(root):
    """
    TODO: Serialize Binary Tree
    - Convert tree to string representation
    - Use preorder traversal with None markers
    
    Hint:
    - Use preorder traversal
    - Represent None as special marker (e.g., "#")
    - Join values with delimiter
    """
    pass


def deserialize_tree(data):
    """
    TODO: Deserialize Binary Tree
    - Reconstruct tree from string
    - Reverse of serialization
    
    Hint:
    - Split string into list
    - Use iterator or index to track position
    - Reconstruct recursively
    """
    pass


# Practice Problems:
# 1. vertical_order_traversal(root) - Vertical traversal
# 2. boundary_traversal(root) - Boundary nodes
# 3. binary_tree_cameras(root) - Minimum cameras needed

