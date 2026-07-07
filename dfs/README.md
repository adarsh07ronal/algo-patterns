# Depth-First Search (DFS)

## Pattern

Depth-First Search explores as far as possible along one branch before backtracking. Starting from a node, DFS dives into a neighbor (or child), then that neighbor's neighbor, and so on, only backtracking to try alternatives once a path is exhausted.

**Recursive vs explicit-stack implementation**

- *Recursive*: the call stack does the bookkeeping for you. Each recursive call represents "go one level deeper." This is the natural fit for trees (`left`/`right` children) and is usually the most readable form. Watch out for recursion-depth limits on very deep/unbalanced structures.
- *Explicit stack*: you maintain your own `stack` (a list used as a LIFO), pushing unvisited neighbors and popping to continue. This avoids Python's recursion limit and makes iterative control flow (e.g. early termination) easier to reason about. Functionally equivalent to recursion — just trades the call stack for a manual one.

**Typical use cases**

- Tree traversal (pre/in/post-order), computing depth, or validating structural properties (e.g. BST validity).
- Graph connectivity: counting connected components, flood-fill on grids (e.g. islands), cloning a graph.
- Cycle detection in directed graphs (e.g. course scheduling / topological feasibility) using node coloring (unvisited / in-progress / done).
- Path-finding where you need *any* path or need to enumerate *all* paths (e.g. path sum, backtracking problems).

**DFS vs BFS**

Reach for DFS when:
- You need to explore full paths or connectivity rather than the *shortest* path.
- The problem is naturally recursive (trees, nested structures, backtracking).
- You need to detect cycles or classify edges (tree/back/forward/cross edges).
- Memory is a concern for wide graphs — DFS's stack depth is bounded by path length, not by breadth.

Reach for BFS instead when you need shortest-path / minimum-steps guarantees on unweighted graphs, or level-by-level processing.

**[Interview cheatsheet: how to remember and code this pattern from scratch](./interview-cheatsheet.md)**

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| Easy | [Maximum Depth of Binary Tree](./maximum-depth-of-binary-tree/README.md) | Classic recursive DFS returning a computed value from children |
| Easy | [Path Sum](./path-sum/README.md) | DFS that threads a running total down to leaves |
| Medium | [Number of Islands](./number-of-islands/README.md) | Grid flood-fill DFS to count connected components |
| Medium | [Course Schedule](./course-schedule/README.md) | Cycle detection in a directed graph via DFS coloring |
| Medium | [Clone Graph](./clone-graph/README.md) | DFS with a visited map to deep-copy a graph |
| Medium | [Validate Binary Search Tree](./validate-binary-search-tree/README.md) | DFS with propagated value bounds |
| Medium | [Surrounded Regions](./surrounded-regions/README.md) | DFS from borders to mark safe regions before flipping |

[<- Back to repo root](../README.md)
