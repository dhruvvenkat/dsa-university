# Union-Find (Disjoint Set Union) - Introduction

## Overview

Union-Find is a data structure that efficiently tracks disjoint sets and supports two operations:
- **Find**: Determine which set an element belongs to
- **Union**: Merge two sets

## Key Concepts

1. **Disjoint Sets**: Sets with no common elements
2. **Representative**: One element represents each set
3. **Path Compression**: Optimize find operation
4. **Union by Rank**: Optimize union operation

## Operations

- **Find(x)**: Find representative of set containing x
- **Union(x, y)**: Merge sets containing x and y
- **Connected(x, y)**: Check if x and y are in same set

## Optimizations

1. **Path Compression**: Make all nodes point directly to root during find
2. **Union by Rank**: Always attach smaller tree to larger tree

## Time Complexity

- Without optimization: O(n) worst case
- With both optimizations: Nearly O(1) amortized (inverse Ackermann function)

## Applications

- Kruskal's algorithm (MST)
- Network connectivity
- Image segmentation
- Friend circles
- Cycle detection in graphs

## Learning Path (Future)

After completing the 30-day course:
- Day 1: Basic Union-Find implementation
- Day 2: Path compression and union by rank
- Day 3: Applications: Friend circles, redundant connections
- Day 4: Kruskal's algorithm for MST
- Day 5: Advanced applications

## Practice Problems (No Solutions - Implement Yourself)

1. Number of Islands (Union-Find approach)
2. Friend Circles
3. Redundant Connection
4. Accounts Merge
5. Sentence Similarity II
6. Regions Cut By Slashes
7. Most Stones Removed with Same Row or Column
8. Smallest String With Swaps
9. Remove Max Number of Edges to Keep Graph Fully Traversable
10. Kruskal's Algorithm implementation

---

**Note**: This topic is marked for future learning after completing the core 30-day curriculum. Master the fundamentals first!

