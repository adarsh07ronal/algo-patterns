# Graph Valid Tree (Medium)

## Problem

Given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, determine whether these
edges form a valid tree — i.e. the graph is connected and contains no cycles.

**Example 1**

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2**

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```
The edges `1-2`, `2-3`, `1-3` form a cycle.

**Constraints**

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- No self-loops or duplicate edges.

## Approach

A valid tree on `n` nodes has exactly two properties simultaneously: it is connected, and it has
exactly `n - 1` edges (equivalently, no cycles, given the edge count). Check the edge count first
as a cheap short-circuit: if `len(edges) != n - 1`, it's impossible to be a tree regardless of
structure (too few edges means disconnected, too many guarantees a cycle).

If the count matches, build a DSU over the `n` nodes and `union` each edge's endpoints. If any
`union` call finds both endpoints already sharing a root, that edge closes a cycle — return
`False` immediately. If every edge unions two previously-separate components, then after
processing exactly `n - 1` such successful unions, all `n` nodes must be pulled into a single
component (since each successful union reduces the component count by exactly one, from `n` down
to `1`), so the graph is both acyclic and connected — a valid tree.

Union-find is preferable to DFS/BFS because it verifies **both** conditions (no cycle, fully
connected) in the same incremental pass over edges, with a trivial cycle check (`find(u) ==
find(v)` before unioning). A DFS-based approach needs a separate cycle-detection traversal (or
careful parent-tracking during DFS) plus a separate reachability count — union-find folds both
into one loop.

## Edge Cases

- **n = 1, no edges**: a single node is trivially a valid tree (`0 == n - 1` edges). Handled
  since the edge-count check passes and the loop body never runs.
- **Edge count mismatch**: any `len(edges) != n - 1` short-circuits to `False` without even
  touching the DSU.
- **Disconnected graph with exactly `n - 1` edges** (impossible in practice for simple graphs,
  since disconnection with `n-1` edges implies some component has a cycle) — still correctly
  caught because the cycle check (`union` returning `False`) will fire somewhere.
- **Duplicate edge between the same pair**: would be caught as a cycle on the second occurrence
  (not present per constraints, but handled safely).

## Complexity

- **Time**: O(n * α(n)) — initializing the DSU is O(n), processing at most `n - 1` edges is
  O(n) unions, each amortized O(α(n)).
- **Space**: O(n) for the DSU parent/rank arrays.

[<- Previous](../accounts-merge/README.md) | [Category Index](../README.md) | [Next ->](../satisfiability-of-equality-equations/README.md)
