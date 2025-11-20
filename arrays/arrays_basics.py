"""
ARRAYS - Basics & Operations
============================

An array is a collection of elements stored in contiguous memory locations.
Each element can be accessed directly using its index.

Key Concepts:
- Indexing: Access elements using index (0-based in most languages)
- Static vs Dynamic: Fixed size vs resizable
- Time Complexity:
  - Access: O(1)
  - Search: O(n) for unsorted, O(log n) for sorted
  - Insert: O(n) (need to shift elements)
  - Delete: O(n) (need to shift elements)

TODO: Implement the following
"""


class Array:
    """
    TODO: Implement a basic Array class with the following operations:
    
    1. __init__(self, size): Initialize array with given size
    2. get(self, index): Get element at index (return None if invalid)
    3. set(self, index, value): Set element at index
    4. insert(self, index, value): Insert value at index (shift elements)
    5. delete(self, index): Delete element at index (shift elements)
    6. search(self, value): Return index of value, or -1 if not found
    7. length(self): Return current number of elements
    8. display(self): Print all elements
    
    Hints:
    - Use a list internally to store elements
    - Check bounds before accessing indices
    - For insert/delete, shift elements right/left
    - Keep track of current size vs capacity
    """
    pass


def linear_search(arr, target):
    """
    TODO: Implement linear search
    - Iterate through array
    - Return index if found, -1 otherwise
    
    Hint: Simple loop through array elements
    """
    pass


def two_pointers_example(arr, target_sum):
    """
    TODO: Implement two-pointer technique
    - Given sorted array, find two numbers that sum to target
    - Use one pointer at start, one at end
    - Move pointers based on current sum
    
    Hint:
    - If sum < target, move left pointer right
    - If sum > target, move right pointer left
    - If sum == target, return indices
    """
    pass


# Practice Problems (implement these):
# 1. find_maximum(arr) - Find maximum element
# 2. reverse_array(arr) - Reverse array in-place
# 3. remove_duplicates_sorted(arr) - Remove duplicates from sorted array
# 4. move_zeros(arr) - Move all zeros to end, maintain relative order

