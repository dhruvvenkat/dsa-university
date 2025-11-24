"""
LINKED LISTS - Basics
=====================

A linked list is a linear data structure where elements are stored in nodes.
Each node contains data and a reference to the next node.

Key Concepts:
- Node: Contains data and next pointer
- Head: First node in the list
- Tail: Last node in the list (points to None/null)
- Advantages: Dynamic size, efficient insertion/deletion
- Disadvantages: No random access, extra memory for pointers

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(1) if tail pointer maintained
- Delete: O(1) if node reference known, O(n) to find node
"""


class ListNode:
    """
    TODO: Implement ListNode class
    - data: value stored in node
    - next: reference to next node (None for last node)
    
    Hint: Simple class with __init__ method
    """
    pass


class LinkedList:
    """
    TODO: Implement Singly Linked List with:
    
    1. __init__(self): Initialize empty list
    2. append(self, data): Add node at end
    3. prepend(self, data): Add node at beginning
    4. insert_after(self, prev_node, data): Insert after given node
    5. delete(self, data): Delete first occurrence of data
    6. search(self, data): Return node with data, or None
    7. length(self): Return number of nodes
    8. display(self): Print all nodes
    9. reverse(self): Reverse the linked list
    
    Hints:
    - Maintain head pointer
    - Optionally maintain tail pointer for O(1) append
    - For reverse: use iterative (three pointers) or recursive approach
    - Handle edge cases: empty list, single node, etc.
    """
    pass


def find_middle(head):
    """
    TODO: Find middle node of linked list
    - If even number of nodes, return second middle
    - Use fast-slow pointer technique
    
    Hint:
    - Slow pointer moves 1 step, fast moves 2 steps
    - When fast reaches end, slow is at middle
    """
    pass


def detect_cycle(head):
    """
    TODO: Detect if linked list has cycle
    - Return True if cycle exists, False otherwise
    - Use Floyd's cycle detection (tortoise and hare)
    
    Hint:
    - Use two pointers: slow and fast
    - If they meet, cycle exists
    - If fast reaches None, no cycle
    """
    pass


def merge_sorted_lists(list1, list2):
    """
    TODO: Merge two sorted linked lists
    - Return merged sorted list
    - Use dummy node pattern
    
    Hint:
    - Create dummy node to simplify edge cases
    - Compare nodes from both lists
    - Attach smaller node to result
    - Handle remaining nodes
    """
    pass


# Practice Problems:
# 1. remove_nth_from_end(head, n) - Remove nth node from end
# 2. is_palindrome(head) - Check if linked list is palindrome
# 3. reverse_k_group(head, k) - Reverse nodes in groups of k

