# Backtracking - Introduction

## Overview

Backtracking is a systematic method for solving problems by trying partial solutions and abandoning them ("backtracking") if they cannot lead to a valid solution.

## Key Concepts

1. **Incremental Construction**: Build solution step by step
2. **Constraint Checking**: Verify if partial solution is valid
3. **Backtracking**: Undo last choice if no valid solution possible
4. **State Space Tree**: Tree of all possible solutions

## When to Use Backtracking

- Constraint satisfaction problems
- Combinatorial problems
- Problems requiring all solutions
- When brute force is too slow but need to explore all possibilities

## Common Patterns

1. **N-Queens**: Place N queens on N×N board
2. **Sudoku Solver**: Fill 9×9 grid following rules
3. **Subset Generation**: Generate all subsets
4. **Permutations**: Generate all permutations
5. **Combination Sum**: Find combinations that sum to target

## Algorithm Template

```
def backtrack(candidate):
    if is_solution(candidate):
        output(candidate)
        return
    
    for next_candidate in generate_candidates(candidate):
        if is_valid(next_candidate):
            make_move(next_candidate)
            backtrack(next_candidate)
            unmake_move(next_candidate)  # Backtrack
```

## Learning Path (Future)

After completing the 30-day course:
- Day 1: Subsets, Permutations, Combinations
- Day 2: N-Queens, Sudoku Solver
- Day 3: Combination Sum variations
- Day 4: Word Search, Letter Combinations
- Day 5: Advanced backtracking problems

## Practice Problems (No Solutions - Implement Yourself)

1. Subsets
2. Permutations
3. Combinations
4. Combination Sum
5. N-Queens
6. Sudoku Solver
7. Word Search
8. Letter Combinations of Phone Number
9. Generate Parentheses
10. Restore IP Addresses

---

**Note**: This topic is marked for future learning after completing the core 30-day curriculum. Focus on mastering the fundamentals first!

