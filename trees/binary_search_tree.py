"""
TREES - Binary Search Trees
===========================

Binary Search Tree (BST) Properties:
- Left subtree: all values < root
- Right subtree: all values > root
- Both subtrees are also BSTs
- No duplicate values (typically)

Operations:
- Search: O(log n) average, O(n) worst
- Insert: O(log n) average, O(n) worst
- Delete: O(log n) average, O(n) worst

TODO: Implement BST operations
"""


class BSTNode:
    """
    TODO: BST Node class
    - val: Value
    - left: Left child
    - right: Right child
    """
    pass


class BinarySearchTree:
    """
    TODO: Implement Binary Search Tree
    
    Methods:
    1. __init__(self): Initialize empty BST
    2. insert(self, val): Insert value maintaining BST property
    3. search(self, val): Search for value, return node or None
    4. delete(self, val): Delete node with value
    5. find_min(self): Return minimum value
    6. find_max(self): Return maximum value
    7. inorder(self): Return inorder traversal
    
    Hints:
    - Insert: Find correct position, create new node
    - Search: Compare and go left/right
    - Delete: Handle 3 cases (no child, one child, two children)
    - For delete with two children: replace with inorder successor
    """
    pass


def validate_bst(root):
    """
    TODO: Validate Binary Search Tree
    - Check if tree satisfies BST properties
    - Use bounds approach
    
    Hint:
    - Each node must be within valid range
    - Pass min and max bounds recursively
    - Update bounds when going left/right
    """
    pass


def kth_smallest(root, k):
    """
    TODO: Kth Smallest Element in BST
    - Return kth smallest value
    - Use inorder traversal (gives sorted order)
    
    Hint:
    - Inorder traversal visits nodes in sorted order
    - Count nodes during traversal
    - Return when count equals k
    """
    pass


def lca_bst(root, p, q):
    """
    TODO: Lowest Common Ancestor in BST
    - Return LCA of nodes p and q
    - Use BST property
    
    Hint:
    - If both values < root, go left
    - If both values > root, go right
    - Otherwise, root is LCA
    """
    pass


def sorted_array_to_bst(nums):
    """
    TODO: Convert Sorted Array to BST
    - Create balanced BST from sorted array
    - Use middle element as root
    
    Hint:
    - Middle element becomes root
    - Recursively build left and right subtrees
    - This creates balanced BST
    """
    pass


# Practice Problems:
# 1. range_sum_bst(root, low, high) - Sum values in range
# 2. delete_node_bst(root, key) - Delete node
# 3. inorder_successor(root, p) - Find inorder successor

