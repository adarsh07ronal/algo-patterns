# Union-Find (Disjoint Set Union)

## Pattern

A disjoint-set (union-find) structure tracks a partition of elements into a collection of
non-overlapping sets, and answers "are these two elements in the same set?" / "merge these
two sets" queries efficiently as the partition evolves.

Two operations power everything:

- **`find(x)`** — walks parent pointers up to the representative ("root") of `x`'s set. With
  **path compression**, every node visited during the walk is re-pointed directly at the root,
  so future lookups are nearly instant.
- **`union(x, y)`** — finds the roots of `x` and `y` and, if different, links one root under
  the other, merging the two sets. With **union by rank/size**, the smaller/shallower tree is
  attached under the larger/deeper one, keeping trees flat.

Combined, path compression + union by rank give amortized **near-O(1)** operations (formally
O(α(n)), the inverse Ackermann function, which is effectively constant for any realistic input
size).

### Typical use cases

- Counting or identifying **connected components** in an undirected graph.
- **Cycle detection** in undirected graphs (a `union` call that finds both endpoints already
  share a root means the new edge closes a cycle).
- **Grouping by shared relation** — merging items that are transitively linked by some
  "belongs together" signal (shared email, shared row/column, equality constraint, etc.).
- **Dynamic/incremental connectivity** — when edges or relations arrive one at a time and you
  need an up-to-date answer without recomputing from scratch (DFS/BFS would need to re-traverse
  the whole graph after every change; union-find updates incrementally).

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| Easy | [Number of Provinces](./number-of-provinces/README.md) | Count connected components from an adjacency matrix |
| Easy | [Find if Path Exists in Graph](./find-if-path-exists-in-graph/README.md) | Simple connectivity query between two nodes |
| Medium | [Redundant Connection](./redundant-connection/README.md) | Detect the edge that first closes a cycle |
| Medium | [Accounts Merge](./accounts-merge/README.md) | Group accounts transitively linked by shared emails |
| Medium | [Graph Valid Tree](./graph-valid-tree/README.md) | Validate connectivity + acyclicity together |
| Medium | [Satisfiability of Equality Equations](./satisfiability-of-equality-equations/README.md) | Group variables by equality, then check inequalities |
| Medium | [Most Stones Removed with Same Row or Column](./most-stones-removed-with-same-row-or-column/README.md) | Union stones sharing a row/column, count components |

[<- Back to repo root](../README.md)
