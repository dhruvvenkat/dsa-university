"""
TREES - Binary Trees & Traversals
==================================

Tree: Hierarchical data structure
- Node: Contains data and references to children
- Root: Topmost node
- Leaf: Node with no children
- Height: Longest path from root to leaf
- Depth: Distance from root to node

Binary Tree: Each node has at most 2 children
- Left child and right child

Tree Traversals:
1. Inorder: Left -> Root -> Right
2. Preorder: Root -> Left -> Right
3. Postorder: Left -> Right -> Root
4. Level-order: Level by level (BFS)

TODO: Implement tree structure and traversals
"""


class TreeNode:
    """
    TODO: Implement TreeNode class
    - val: Value stored in node
    - left: Reference to left child
    - right: Reference to right child
    
    Hint: Simple class with __init__ method
    """
    pass


def inorder_traversal(root):
    """
    TODO: Inorder Traversal (Left -> Root -> Right)
    - Return list of values in inorder
    - Implement both recursive and iterative versions
    
    Hint:
    - Recursive: traverse left, visit root, traverse right
    - Iterative: use stack, go left until None, then pop and go right
    """
    pass


def preorder_traversal(root):
    """
    TODO: Preorder Traversal (Root -> Left -> Right)
    - Return list of values in preorder
    
    Hint:
    - Recursive: visit root, traverse left, traverse right
    - Iterative: use stack, push right then left
    """
    pass


def postorder_traversal(root):
    """
    TODO: Postorder Traversal (Left -> Right -> Root)
    - Return list of values in postorder
    
    Hint:
    - Recursive: traverse left, traverse right, visit root
    - Iterative: use two stacks or reverse approach
    """
    pass


def level_order_traversal(root):
    """
    TODO: Level Order Traversal (BFS)
    - Return list of lists, each inner list is a level
    - Use queue for BFS
    
    Hint:
    - Use queue, start with root
    - Process level by level
    - Add children to queue
    """
    pass


def max_depth(root):
    """
    TODO: Maximum Depth of Binary Tree
    - Return height/depth of tree
    - Use recursive approach
    
    Hint:
    - Base case: None node returns 0
    - Recursive: 1 + max(left_depth, right_depth)
    """
    pass


def same_tree(p, q):
    """
    TODO: Check if two trees are identical
    - Return True if same structure and values
    
    Hint:
    - Base cases: both None -> True, one None -> False
    - Check values and recursively check subtrees
    """
    pass


def symmetric_tree(root):
    """
    TODO: Check if tree is symmetric
    - Mirror image of itself
    
    Hint:
    - Helper function to compare two subtrees
    - Check if left of one equals right of other
    """
    pass


# Practice Problems:
# 1. invert_tree(root) - Invert/mirror binary tree
# 2. binary_tree_paths(root) - All root-to-leaf paths
# 3. sum_of_left_leaves(root) - Sum of left leaf nodes

