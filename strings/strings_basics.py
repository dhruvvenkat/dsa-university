"""
STRINGS - Basics & Patterns
===========================

String manipulation fundamentals:
- Character access and iteration
- String operations (concatenation, slicing)
- Pattern matching basics
- Two-pointer technique for strings

TODO: Implement string utilities and patterns
"""


def reverse_string(s):
    """
    TODO: Reverse string
    - In-place if mutable, or return new string
    - Use two-pointer technique
    
    Hint:
    - Swap characters from both ends
    - Move pointers toward center
    """
    pass


def valid_palindrome(s):
    """
    TODO: Check if string is palindrome
    - Ignore non-alphanumeric, case-insensitive
    - "A man, a plan, a canal: Panama" -> True
    
    Hint:
    - Use two pointers
    - Skip non-alphanumeric characters
    - Compare characters (case-insensitive)
    """
    pass


def reverse_words(s):
    """
    TODO: Reverse words in string
    - "the sky is blue" -> "blue is sky the"
    - Handle multiple spaces
    
    Hint:
    - Split string into words
    - Reverse word order
    - Join with single space
    """
    pass


def longest_palindromic_substring(s):
    """
    TODO: Find longest palindromic substring
    - "babad" -> "bab" or "aba"
    - Use expand around centers approach
    
    Hint:
    - For each position, expand as center
    - Handle odd and even length palindromes
    - Track maximum length and substring
    """
    pass


def valid_anagram(s, t):
    """
    TODO: Check if two strings are anagrams
    - "anagram" and "nagaram" -> True
    - Use frequency counting
    
    Hint:
    - Count frequency of characters in both strings
    - Compare frequency maps
    - Or sort both and compare
    """
    pass


def string_compression(chars):
    """
    TODO: Compress string in-place
    - ["a","a","b","b","c","c","c"] -> ["a","2","b","2","c","3"]
    - Return new length
    
    Hint:
    - Use two pointers: read and write
    - Count consecutive characters
    - Write character and count
    """
    pass


# Practice Problems:
# 1. is_subsequence(s, t) - Check if s is subsequence of t
# 2. first_unique_character(s) - Find first non-repeating character
# 3. valid_parentheses_string(s) - Check valid parentheses

