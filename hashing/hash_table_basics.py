"""
HASHING - Hash Tables & Sets
=============================

Hash Table: Key-value data structure
- Average time: O(1) for insert, delete, search
- Worst case: O(n) if all keys hash to same bucket

Key Concepts:
- Hash Function: Maps key to index
- Collision: Two keys map to same index
- Collision Resolution:
  1. Chaining: Linked list at each bucket
  2. Open Addressing: Find next available slot

TODO: Implement hash table with chaining
"""


class HashNode:
    """
    TODO: Node for chaining
    - key: The key
    - value: The value
    - next: Pointer to next node in chain
    """
    pass


class HashTable:
    """
    TODO: Implement Hash Table with Chaining
    
    Methods:
    1. __init__(self, capacity): Initialize with given capacity
    2. _hash(self, key): Hash function to map key to index
    3. put(self, key, value): Insert/update key-value pair
    4. get(self, key): Get value for key, return None if not found
    5. remove(self, key): Remove key-value pair
    6. contains(self, key): Check if key exists
    7. size(self): Return number of key-value pairs
    
    Hints:
    - Use list of buckets (each bucket is a linked list)
    - Hash function: hash(key) % capacity
    - Handle collisions by chaining
    - Consider load factor and rehashing
    """
    pass


class HashSet:
    """
    TODO: Implement Hash Set (similar to HashTable but only keys)
    
    Methods:
    1. add(key): Add key to set
    2. remove(key): Remove key from set
    3. contains(key): Check if key exists
    4. size(): Return number of elements
    
    Hint: Similar to HashTable but no values
    """
    pass


def two_sum(nums, target):
    """
    TODO: Two Sum using Hash Table
    - Find two numbers that add up to target
    - Return indices of the two numbers
    - O(n) time using hash table
    
    Hint:
    - Use hash map to store number -> index
    - For each number, check if complement exists
    """
    pass


def group_anagrams(strs):
    """
    TODO: Group Anagrams
    - Group strings that are anagrams together
    - Use sorted string as key in hash map
    
    Hint:
    - Sort each string to get canonical form
    - Use sorted string as key, list of strings as value
    """
    pass


def longest_consecutive(nums):
    """
    TODO: Longest Consecutive Sequence
    - Find length of longest consecutive sequence
    - O(n) time using hash set
    
    Hint:
    - Add all numbers to hash set
    - For each number, check if it's start of sequence
    - Count consecutive numbers
    """
    pass


# Practice Problems:
# 1. contains_duplicate(nums) - Check for duplicates
# 2. first_missing_positive(nums) - Find first missing positive integer
# 3. valid_anagram(s, t) - Check if strings are anagrams

