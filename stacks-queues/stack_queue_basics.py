"""
STACKS & QUEUES - Fundamentals
===============================

STACK (LIFO - Last In First Out):
- Operations: push, pop, peek/top, isEmpty
- Like a stack of plates
- Applications: Expression evaluation, backtracking, function calls

QUEUE (FIFO - First In First Out):
- Operations: enqueue, dequeue, front, isEmpty
- Like a line of people
- Applications: BFS, scheduling, buffering

TODO: Implement both using arrays and linked lists
"""


class StackArray:
    """
    TODO: Implement Stack using Array/List
    
    Methods:
    1. __init__(self, capacity): Initialize stack
    2. push(self, item): Add item to top
    3. pop(self): Remove and return top item
    4. peek(self): Return top item without removing
    5. is_empty(self): Check if stack is empty
    6. is_full(self): Check if stack is full
    7. size(self): Return number of elements
    
    Hint:
    - Use list to store elements
    - Track top index
    - Handle overflow/underflow
    """
    pass


class StackLinkedList:
    """
    TODO: Implement Stack using Linked List
    
    Same methods as StackArray
    
    Hint:
    - Use linked list with head pointer
    - Push/pop at head for O(1) operations
    - No need to track capacity
    """
    pass


class QueueArray:
    """
    TODO: Implement Queue using Array (Circular Queue)
    
    Methods:
    1. __init__(self, capacity): Initialize queue
    2. enqueue(self, item): Add item to rear
    3. dequeue(self): Remove and return front item
    4. front(self): Return front item without removing
    5. is_empty(self): Check if queue is empty
    6. is_full(self): Check if queue is full
    7. size(self): Return number of elements
    
    Hint:
    - Use circular array to reuse space
    - Track front and rear indices
    - Use modulo for circular wrapping
    """
    pass


class QueueLinkedList:
    """
    TODO: Implement Queue using Linked List
    
    Same methods as QueueArray
    
    Hint:
    - Maintain head and tail pointers
    - Enqueue at tail, dequeue from head
    - Both operations O(1)
    """
    pass


def valid_parentheses(s):
    """
    TODO: Check if parentheses are valid
    - Use stack to match opening and closing brackets
    - Return True if valid, False otherwise
    
    Hint:
    - Push opening brackets onto stack
    - Pop when closing bracket matches
    - Stack should be empty at end
    """
    pass


def implement_queue_using_stacks():
    """
    TODO: Implement queue using two stacks
    - Enqueue: push to stack1
    - Dequeue: if stack2 empty, transfer stack1 to stack2, then pop
    
    Hint:
    - Use two stacks
    - Transfer elements when needed for dequeue
    """
    pass


# Practice Problems:
# 1. next_greater_element(nums) - Find next greater element
# 2. daily_temperatures(temperatures) - Days until warmer temperature
# 3. min_stack() - Stack with O(1) min operation

