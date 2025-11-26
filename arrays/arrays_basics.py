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

    def __init__(self, size):
        self.size = size  # Maximum capacity
        self.data = [None] * size  # Internal storage
        self.length = 0  # Current number of elements

    def get(self, index):
        """Get element at index (return None if invalid)"""
        if index < 0 or index >= self.length:
            return None
        return self.data[index]

    def set(self, index, value):
        """Set element at index"""
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of bounds for array of size {self.size}")
        
        # If setting beyond current length, update length
        if index >= self.length:
            self.length = index + 1
        
        self.data[index] = value
    
    def insert(self, index, value):
        """Insert value at index (shift elements right)"""
        # Check if array is full
        if self.length >= self.size:
            raise OverflowError("Array is full, cannot insert")
        
        # Check if index is valid
        if index < 0 or index > self.length:
            raise IndexError(f"Index {index} out of bounds")
        
        # Shift elements to the right
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
        
        # Insert the new value
        self.data[index] = value
        self.length += 1

    def delete(self, index):
        """Delete element at index (shift elements left)"""
        if index < 0 or index >= self.length:
            raise IndexError(f"Index {index} out of bounds")
        
        # Shift elements to the left
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        
        # Clear the last element and decrement length
        self.data[self.length - 1] = None
        self.length -= 1

    def search(self, value):
        """Return index of value, or -1 if not found"""
        for i in range(self.length):
            if self.data[i] == value:
                return i
        return -1

    def length(self):
        """Return current number of elements"""
        return self.length

    def display(self):
        """Print all elements"""
        print("[", end="")
        for i in range(self.length):
            print(self.data[i], end="")
            if i < self.length - 1:
                print(", ", end="")
        print("]")


def linear_search(arr, target):
    """
    TODO: Implement linear search
    - Iterate through array
    - Return index if found, -1 otherwise
    
    Hint: Simple loop through array elements
    """
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
        
    return -1


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
    # O(n^2) implementation - very basic
    # for i in range(len(arr)):
    #     for j in range(len(arr)-1):
    #         if (arr[i] + arr[j] == target_sum):
    #             return [i, j]

    #O(n) implementation - more advanced, use this
    left = 0
    right = len(arr) - 1

    while(left < right): #never introduce infinite loops
        sum = arr[left]+arr[right]
        if(sum < target_sum):
            left += 1
        elif(sum > target_sum):
            right -= 1
        else:
            return[left, right]

    pass


# Practice Problems (implement these):
# 1. find_maximum(arr) - Find maximum element
# 2. reverse_array(arr) - Reverse array in-place
# 3. remove_duplicates_sorted(arr) - Remove duplicates from sorted array
# 4. move_zeros(arr) - Move all zeros to end, maintain relative order

def find_maximum(arr):
    max = 0

    for i in arr:
        if i > max:
            max = i
    
    return max

#reversal algorithm: set a leftmost and rightmost pointer, swap them and move inwards until pointers cross
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        temp = arr[right]
        arr[right] = arr[left]
        arr[left] = temp

        left += 1
        right -= 1
    return arr

def remove_duplicates_sorted(arr):
    # Iterate backwards to avoid index issues when removing elements
    for i in range(len(arr) - 1, 0, -1):
        if (arr[i] == arr[i-1]):
            arr.pop(i)
    
    return arr

def move_zeros(arr):
    write_index = 0

    #first pass moves all nonzero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write_index] = arr[i]
            write_index += 1
    
    #second pass sets all duplicate elements to 0
    for i in range(write_index, len(arr)):
        arr[i] = 0
    
    return arr

testArray = [1, 5, 6, 2, 3, 4, 4, 5, 6, 2]

print(find_maximum(testArray))
print(reverse_array(testArray))
print(remove_duplicates_sorted(sorted(testArray)))

testArrayZeros = [1, 3, 2, 0, 5, 4, 0, 2, 7, 0]
print(move_zeros(testArrayZeros))
