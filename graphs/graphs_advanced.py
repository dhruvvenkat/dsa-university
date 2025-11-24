"""
GRAPHS - Advanced Algorithms
=============================

Advanced graph algorithms:
1. Topological Sort
2. Cycle Detection
3. Shortest Path (BFS-based)
4. Union-Find (for connectivity)
"""


def topological_sort(graph, num_vertices):
    """
    TODO: Topological Sort
    - Linear ordering of vertices in directed acyclic graph
    - For edge (u->v), u comes before v
    - Use DFS or Kahn's algorithm
    
    Hint (DFS approach):
    - DFS and add to result when all neighbors processed
    - Reverse result at end
    - Or use Kahn's: process nodes with in-degree 0
    """
    pass


def kahn_algorithm(graph, num_vertices):
    """
    TODO: Kahn's Algorithm for Topological Sort
    - Use in-degree counting
    - Process nodes with in-degree 0
    
    Hint:
    - Calculate in-degree for each vertex
    - Queue nodes with in-degree 0
    - Remove edges, update in-degrees
    - If all nodes processed, no cycle
    """
    pass


def detect_cycle_directed(graph, num_vertices):
    """
    TODO: Detect Cycle in Directed Graph
    - Return True if cycle exists
    - Use DFS with three states
    
    Hint:
    - States: WHITE (unvisited), GRAY (visiting), BLACK (visited)
    - If GRAY node encountered, cycle exists
    - Mark BLACK when all neighbors processed
    """
    pass


def detect_cycle_undirected(graph, num_vertices):
    """
    TODO: Detect Cycle in Undirected Graph
    - Return True if cycle exists
    - Use DFS with parent tracking
    
    Hint:
    - Track parent to avoid false cycle detection
    - If visited neighbor is not parent, cycle exists
    """
    pass


def shortest_path_unweighted(graph, start, end):
    """
    TODO: Shortest Path in Unweighted Graph
    - Return shortest path from start to end
    - Use BFS
    
    Hint:
    - BFS finds shortest path in unweighted graph
    - Track parent to reconstruct path
    - Return path when end reached
    """
    pass


def network_delay_time(times, n, k):
    """
    TODO: Network Delay Time (BFS approach for unweighted)
    - Time for signal to reach all nodes from node k
    - For weighted version, need Dijkstra's (advanced)
    
    Hint:
    - Build graph from times
    - BFS from node k
    - Track maximum time to reach any node
    """
    pass


def find_town_judge(n, trust):
    """
    TODO: Find the Town Judge
    - Person trusted by everyone, trusts nobody
    - Use graph concepts
    
    Hint:
    - Judge has in-degree n-1, out-degree 0
    - Count in-degrees and out-degrees
    """
    pass


def redundant_connection(edges):
    """
    TODO: Redundant Connection
    - Find edge that creates cycle
    - Use Union-Find (or DFS)
    
    Hint:
    - Use Union-Find to detect when edge connects already connected components
    - Or use DFS to detect cycle
    """
    pass


# Practice Problems:
# 1. course_schedule_ii(num_courses, prerequisites) - Topological sort
# 2. alien_dictionary(words) - Build order from alien language
# 3. critical_connections(n, connections) - Find bridges

