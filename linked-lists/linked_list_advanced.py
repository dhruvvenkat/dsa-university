"""
LINKED LISTS - Advanced
=======================

Advanced linked list techniques:
1. Two-pointer patterns (fast-slow)
2. Dummy node pattern
3. Pointer manipulation
4. List partitioning and merging
"""


def reverse_linked_list(head):
    """
    TODO: Reverse linked list iteratively
    - Return new head of reversed list
    - O(1) space complexity
    
    Hint:
    - Use three pointers: prev, curr, next
    - Reverse links as you traverse
    - Return prev as new head
    """
    pass


def reverse_linked_list_recursive(head):
    """
    TODO: Reverse linked list recursively
    - Return new head of reversed list
    
    Hint:
    - Base case: empty list or single node
    - Recursively reverse rest of list
    - Reverse current node's link
    """
    pass


def partition_list(head, x):
    """
    TODO: Partition list around value x
    - Nodes < x come before nodes >= x
    - Maintain relative order within partitions
    
    Hint:
    - Create two separate lists: less and greater/equal
    - Traverse original list, add nodes to appropriate list
    - Connect the two lists
    """
    pass


def intersection_of_lists(headA, headB):
    """
    TODO: Find intersection node of two linked lists
    - Return node where lists intersect, or None
    
    Hint:
    - Calculate lengths of both lists
    - Move longer list's pointer forward by difference
    - Move both pointers until they meet or reach end
    """
    pass


def copy_random_list(head):
    """
    TODO: Deep copy linked list with random pointers
    - Each node has next and random pointer
    - Return deep copy of list
    
    Hint:
    - Two passes: create nodes, then set random pointers
    - Use hash map to map original to copy nodes
    - Or use interleaving technique (no extra space)
    """
    pass


# Practice Problems:
# 1. reverse_nodes_k_group(head, k) - Reverse in groups
# 2. flatten_multilevel_list(head) - Flatten nested structure
# 3. rotate_list(head, k) - Rotate list right by k places

