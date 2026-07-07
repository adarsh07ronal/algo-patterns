# Algo Patterns

A browsable collection of classic coding-interview problems, organized by pattern rather than by source. Each category folder explains the underlying technique once, then walks through 7 problems (2 easy, 5 medium) that use it — each with a plain-English approach writeup, edge cases, complexity, and a tested Python solution.

Every problem folder contains:

- `README.md` — problem statement, approach explanation (the *why*, not just the *what*), edge cases, and complexity.
- `solution.py` — a clean, LeetCode-style `Solution` class with a self-checking `__main__` block (`python3 solution.py` prints `ok` on success).

Problems within a category link to each other (Previous / Next) so you can work through a pattern end-to-end, and every category README links back here.

## Categories

| Category | Pattern | Problems |
|---|---|---|
| [Backtracking](backtracking/README.md) ([cheatsheet](backtracking/interview-cheatsheet.md)) | Explore, choose, undo — search combinatorial state spaces | 7 |
| [Dynamic Programming](dynamic-programming/README.md) ([cheatsheet](dynamic-programming/interview-cheatsheet.md)) | Optimal substructure + overlapping subproblems | 7 |
| [Depth-First Search (DFS)](dfs/README.md) ([cheatsheet](dfs/interview-cheatsheet.md)) | Recursive/stack-based traversal for trees & graphs | 7 |
| [Breadth-First Search (BFS)](bfs/README.md) ([cheatsheet](bfs/interview-cheatsheet.md)) | Queue-based level-order traversal, shortest paths | 7 |
| [Greedy Algorithms](greedy/README.md) ([cheatsheet](greedy/interview-cheatsheet.md)) | Locally optimal choice provably leads to a global optimum | 7 |
| [Sliding Window](sliding-window/README.md) ([cheatsheet](sliding-window/interview-cheatsheet.md)) | Expand/shrink a contiguous window over an array or string | 7 |
| [Two Pointers](two-pointers/README.md) ([cheatsheet](two-pointers/interview-cheatsheet.md)) | Converging or fast/slow pointers, usually over sorted data | 7 |
| [Binary Search](binary-search/README.md) ([cheatsheet](binary-search/interview-cheatsheet.md)) | Halve the search space using a monotonic condition | 7 |
| [Heap / Priority Queue](heap-priority-queue/README.md) ([cheatsheet](heap-priority-queue/interview-cheatsheet.md)) | Efficient access to the min/max of a dynamic set | 7 |
| [Union-Find (Disjoint Set Union)](union-find/README.md) ([cheatsheet](union-find/interview-cheatsheet.md)) | Track and merge connected components efficiently | 7 |

70 problems total across 10 patterns.

## Running a solution

Each solution is self-contained and dependency-free (standard library only):

```bash
python3 backtracking/subsets/solution.py
```

No output means the asserts passed; each script prints `ok` on success.
