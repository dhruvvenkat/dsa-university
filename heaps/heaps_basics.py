"""
HEAPS - Priority Queues
=======================

Heap: Complete binary tree with heap property
- Min-Heap: Parent <= Children (root is minimum)
- Max-Heap: Parent >= Children (root is maximum)

Array Representation:
- Parent at index i
- Left child at 2*i + 1
- Right child at 2*i + 2
- Parent of i at (i-1)//2

Operations:
- Insert: O(log n)
- Extract Min/Max: O(log n)
- Peek: O(1)
- Build Heap: O(n)

TODO: Implement min-heap and max-heap
"""


class MinHeap:
    """
    TODO: Implement Min-Heap
    
    Methods:
    1. __init__(self): Initialize empty heap
    2. parent(self, i): Return parent index
    3. left_child(self, i): Return left child index
    4. right_child(self, i): Return right child index
    5. insert(self, val): Insert value maintaining heap property
    6. heapify_up(self, i): Bubble up element at index i
    7. extract_min(self): Remove and return minimum
    8. heapify_down(self, i): Bubble down element at index i
    9. peek(self): Return minimum without removing
    10. is_empty(self): Check if heap is empty
    11. size(self): Return number of elements
    
    Hints:
    - Use list to store elements
    - For insert: add to end, then heapify up
    - For extract: swap root with last, remove last, heapify down
    - Heapify up: compare with parent, swap if needed
    - Heapify down: compare with children, swap with smaller
    """
    pass


class MaxHeap:
    """
    TODO: Implement Max-Heap
    - Similar to MinHeap but parent >= children
    - Extract maximum instead of minimum
    """
    pass


def heap_sort(arr):
    """
    TODO: Heap Sort
    - Sort array using heap
    - O(n log n) time, O(1) space if done in-place
    
    Hint:
    - Build max-heap from array
    - Repeatedly extract max and place at end
    - Array sorted in ascending order
    """
    pass


def kth_largest(arr, k):
    """
    TODO: Kth Largest Element
    - Find kth largest element in array
    - Use min-heap of size k
    
    Hint:
    - Maintain min-heap of size k
    - If heap size < k, add element
    - If element > heap min, replace min
    - Root is kth largest
    """
    pass


def merge_k_sorted_lists(lists):
    """
    TODO: Merge K Sorted Lists
    - Merge k sorted linked lists
    - Use min-heap
    
    Hint:
    - Add first node of each list to heap
    - Extract min, add to result
    - Add next node from same list to heap
    """
    pass


# Practice Problems:
# 1. find_median_stream() - Median from data stream
# 2. top_k_frequent(nums, k) - Top K frequent elements
# 3. last_stone_weight(stones) - Last remaining stone weight

