"""
STACKS & QUEUES - Advanced Applications
========================================

Advanced patterns:
1. Monotonic Stack: Maintain stack with monotonic property
2. Expression Evaluation: Infix, postfix, prefix
3. Deque: Double-ended queue
4. BFS: Breadth-first search using queues
"""


def monotonic_stack_example(nums):
    """
    TODO: Next Greater Element using Monotonic Stack
    - For each element, find next greater element
    - Use decreasing monotonic stack
    
    Hint:
    - Maintain stack in decreasing order
    - When current > stack top, pop and set result
    - Push current index onto stack
    """
    pass


def largest_rectangle_histogram(heights):
    """
    TODO: Largest Rectangle in Histogram
    - Find largest rectangle area in histogram
    - Use monotonic stack
    
    Hint:
    - For each bar, find left and right boundaries
    - Use stack to track indices
    - Calculate area when popping from stack
    """
    pass


def evaluate_postfix(expression):
    """
    TODO: Evaluate Reverse Polish Notation (Postfix)
    - Expression: ["2", "1", "+", "3", "*"]
    - Result: (2+1)*3 = 9
    
    Hint:
    - Use stack
    - Push numbers, pop two when operator encountered
    - Apply operation and push result
    """
    pass


def infix_to_postfix(expression):
    """
    TODO: Convert infix to postfix notation
    - Input: "3 + 4 * 2"
    - Output: "3 4 2 * +"
    
    Hint:
    - Use stack for operators
    - Handle operator precedence
    - Process parentheses correctly
    """
    pass


class Deque:
    """
    TODO: Implement Double-Ended Queue (Deque)
    
    Methods:
    1. add_front(item): Add to front
    2. add_rear(item): Add to rear
    3. remove_front(): Remove from front
    4. remove_rear(): Remove from rear
    5. is_empty(): Check if empty
    6. size(): Return size
    
    Hint:
    - Can use list or doubly linked list
    - Both ends support O(1) operations
    """
    pass


def bfs_example(graph, start):
    """
    TODO: Breadth-First Search using Queue
    - Traverse graph level by level
    - Return list of visited nodes in BFS order
    
    Hint:
    - Use queue, start with source node
    - Mark visited, add neighbors to queue
    - Process nodes level by level
    """
    pass


# Practice Problems:
# 1. sliding_window_maximum(nums, k) - Using deque
# 2. basic_calculator(s) - Evaluate expression
# 3. number_of_islands_bfs(grid) - BFS approach

