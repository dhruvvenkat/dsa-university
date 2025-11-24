"""
SORTING ALGORITHMS
==================

Sorting: Arrange elements in order (ascending/descending)

Comparison-based sorts:
- Bubble Sort: O(n²) - Simple but slow
- Selection Sort: O(n²) - Find min, swap
- Insertion Sort: O(n²) - Insert in sorted portion
- Merge Sort: O(n log n) - Divide and conquer
- Quick Sort: O(n log n) average - Partition and sort

Non-comparison sorts (for specific cases):
- Counting Sort: O(n+k) - For small range integers
- Radix Sort: O(d*(n+k)) - For integers with fixed digits

TODO: Implement all comparison-based sorts
"""


def bubble_sort(arr):
    """
    TODO: Bubble Sort
    - Compare adjacent elements, swap if wrong order
    - Largest elements "bubble" to end
    - O(n²) time, O(1) space
    
    Hint:
    - Outer loop: n-1 passes
    - Inner loop: compare adjacent, swap if needed
    - Optimize: stop if no swaps in pass
    """
    pass


def selection_sort(arr):
    """
    TODO: Selection Sort
    - Find minimum, swap with first
    - Repeat for remaining unsorted portion
    - O(n²) time, O(1) space
    
    Hint:
    - Outer loop: for each position
    - Inner loop: find minimum in unsorted portion
    - Swap minimum with current position
    """
    pass


def insertion_sort(arr):
    """
    TODO: Insertion Sort
    - Build sorted array one element at a time
    - Insert each element in correct position
    - O(n²) time, O(1) space, good for small arrays
    
    Hint:
    - For each element, insert in sorted portion
    - Shift elements to make room
    - Like sorting playing cards
    """
    pass


def merge_sort(arr):
    """
    TODO: Merge Sort
    - Divide array in half, sort halves, merge
    - O(n log n) time, O(n) space
    - Stable sort
    
    Hint:
    - Base case: array of size 1 is sorted
    - Recursively sort left and right halves
    - Merge two sorted halves
    """
    pass


def merge(left, right):
    """
    TODO: Merge two sorted arrays
    - Helper function for merge sort
    - Combine two sorted arrays into one
    
    Hint:
    - Use two pointers, one for each array
    - Compare and add smaller element
    - Add remaining elements
    """
    pass


def quick_sort(arr, low, high):
    """
    TODO: Quick Sort
    - Choose pivot, partition, sort recursively
    - O(n log n) average, O(n²) worst, O(log n) space
    - In-place, but not stable
    
    Hint:
    - Base case: low >= high
    - Partition array around pivot
    - Recursively sort left and right of pivot
    """
    pass


def partition(arr, low, high):
    """
    TODO: Partition function for Quick Sort
    - Place pivot in correct position
    - Elements < pivot on left, > pivot on right
    - Return pivot index
    
    Hint:
    - Choose pivot (last element or random)
    - Use two pointers: i (smaller), j (current)
    - Swap elements to maintain partition
    """
    pass


def quickselect(arr, k):
    """
    TODO: Quickselect (Kth smallest element)
    - Use partition from quick sort
    - O(n) average time
    
    Hint:
    - Partition array
    - If pivot is kth, return it
    - Otherwise recurse on appropriate side
    """
    pass


# Practice Problems:
# 1. sort_colors(nums) - Sort array of 0s, 1s, 2s (Dutch flag)
# 2. merge_sorted_arrays(nums1, m, nums2, n) - Merge in-place
# 3. sort_list(head) - Sort linked list (merge sort)

