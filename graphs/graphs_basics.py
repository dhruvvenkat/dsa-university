"""
GRAPHS - Representation & BFS/DFS
==================================

Graph: Collection of nodes (vertices) and edges
- Directed: Edges have direction
- Undirected: Edges are bidirectional
- Weighted: Edges have weights
- Unweighted: All edges equal

Representations:
1. Adjacency List: List of lists (most common)
2. Adjacency Matrix: 2D array
3. Edge List: List of edges

Traversals:
- BFS: Level-order, uses queue
- DFS: Depth-first, uses stack (recursive/iterative)

TODO: Implement graph structure and traversals
"""


class Graph:
    """
    TODO: Implement Graph using Adjacency List
    
    Methods:
    1. __init__(self, num_vertices): Initialize graph
    2. add_edge(self, u, v, directed=False): Add edge
    3. add_vertex(self, v): Add vertex
    4. get_neighbors(self, v): Return neighbors of vertex
    5. display(self): Print graph representation
    
    Hint:
    - Use dictionary: {vertex: [neighbors]}
    - Or list of lists: graph[i] = [neighbors of i]
    """
    pass


def bfs(graph, start):
    """
    TODO: Breadth-First Search
    - Traverse graph level by level
    - Return list of visited vertices in BFS order
    - Use queue
    
    Hint:
    - Use queue, start with source
    - Mark visited, add neighbors to queue
    - Process until queue empty
    """
    pass


def dfs_recursive(graph, start, visited=None):
    """
    TODO: DFS Recursive
    - Traverse graph depth-first
    - Return list of visited vertices
    - Use recursion (implicit stack)
    
    Hint:
    - Mark current as visited
    - Recursively visit unvisited neighbors
    - Use set to track visited
    """
    pass


def dfs_iterative(graph, start):
    """
    TODO: DFS Iterative
    - Same as recursive but use explicit stack
    
    Hint:
    - Use stack instead of recursion
    - Push start, pop and process
    - Push unvisited neighbors
    """
    pass


def number_of_islands(grid):
    """
    TODO: Number of Islands
    - Count connected components in 2D grid
    - Use BFS or DFS
    
    Hint:
    - Treat grid as graph
    - Each cell is node, adjacent cells are edges
    - BFS/DFS from each unvisited land cell
    - Count number of BFS/DFS calls
    """
    pass


def clone_graph(node):
    """
    TODO: Clone Graph
    - Deep copy undirected graph
    - Use BFS or DFS with hash map
    
    Hint:
    - Use hash map: original -> copy
    - BFS/DFS to visit all nodes
    - Create copy and connect edges
    """
    pass


def course_schedule(num_courses, prerequisites):
    """
    TODO: Course Schedule (Cycle Detection)
    - Check if can finish all courses (no cycles)
    - Return True if possible
    
    Hint:
    - Build directed graph from prerequisites
    - Detect cycle using DFS
    - Use three states: unvisited, visiting, visited
    """
    pass


# Practice Problems:
# 1. word_ladder(begin_word, end_word, word_list) - BFS problem
# 2. all_paths_source_target(graph) - Find all paths
# 3. graph_coloring(graph, colors) - Color graph

