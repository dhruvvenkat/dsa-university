"""
TRIES - Prefix Trees
====================

Trie (Prefix Tree): Tree-like data structure for strings
- Each node represents a character
- Path from root to node represents a prefix
- Efficient for prefix matching and autocomplete

Use Cases:
- Autocomplete
- Spell checker
- IP routing
- String search

Time Complexity:
- Insert: O(m) where m is string length
- Search: O(m)
- Prefix search: O(m)

TODO: Implement basic trie
"""


class TrieNode:
    """
    TODO: Trie Node class
    - children: Dictionary mapping char to TrieNode
    - is_end: Boolean indicating end of word
    
    Hint:
    - Use dictionary for children (more flexible than array)
    - is_end marks complete words
    """
    pass


class Trie:
    """
    TODO: Implement Trie (Prefix Tree)
    
    Methods:
    1. __init__(self): Initialize empty trie
    2. insert(self, word): Insert word into trie
    3. search(self, word): Return True if word exists
    4. starts_with(self, prefix): Return True if prefix exists
    5. delete(self, word): Delete word from trie (optional)
    
    Hints:
    - Start from root
    - For each character, traverse/create child node
    - Mark end of word with is_end flag
    - For search: traverse and check is_end
    - For starts_with: just check if path exists
    """
    pass


def word_search_ii(board, words):
    """
    TODO: Word Search II
    - Find all words from dictionary in 2D board
    - Use trie + backtracking
    
    Hint:
    - Build trie from words
    - For each cell, DFS with trie
    - Mark visited cells, backtrack
    - Add to result when word found
    """
    pass


def longest_word(words):
    """
    TODO: Longest Word in Dictionary
    - Find longest word that can be built one character at a time
    - All prefixes must exist in dictionary
    
    Hint:
    - Build trie from words
    - DFS from root, track longest valid word
    - Word is valid if all prefixes exist
    """
    pass


def replace_words(dictionary, sentence):
    """
    TODO: Replace Words
    - Replace words in sentence with shortest root from dictionary
    - Use trie to find shortest root
    
    Hint:
    - Build trie from dictionary
    - For each word, find shortest root in trie
    - Replace word with root if found
    """
    pass


# Practice Problems:
# 1. design_add_search_words() - Add and search with '.' wildcard
# 2. word_squares(words) - Form word squares
# 3. palindrome_pairs(words) - Find palindrome pairs

