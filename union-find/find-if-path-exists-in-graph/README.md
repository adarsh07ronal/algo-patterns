# Find if Path Exists in Graph (Easy)

## Problem

You are given a bi-directional graph with `n` nodes labeled `0` to `n - 1`, described by an
edge list `edges` where `edges[i] = [ui, vi]` denotes an undirected edge between `ui` and `vi`.
Given `source` and `destination`, determine whether there is a valid path between them.

**Example 1**

```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
```
0 -> 1 -> 2 is a valid path.

**Example 2**

```
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
```
{0,1,2} and {3,4,5} are separate components; there is no way to reach 5 from 0.

**Constraints**

- `1 <= n <= 2 * 10^5`
- `0 <= edges.length <= 2 * 10^5`
- No self-loops or repeated edges guaranteed to matter for correctness, but the solution
  tolerates them.

## Approach

Build a DSU over the `n` nodes and `union` the two endpoints of every edge. Once all edges are
processed, the graph's connectivity is fully captured in the DSU's parent structure: `source`
and `destination` have a valid path between them **iff** `find(source) == find(destination)`.

This is a textbook dynamic-connectivity question — we only ever need yes/no answers to "same
component?" and never need the actual path. Union-find answers that in near-constant time after
an O(E) linear build, whereas DFS/BFS would need to traverse from `source` and stop early only
if `destination` is found, doing comparable work for a single query but scaling worse if this
question were asked repeatedly for different `(source, destination)` pairs on the same graph
(union-find only builds the DSU once).

## Edge Cases

- **No edges** (`edges = []`): every node is its own component; answer is `true` only if
  `source == destination`.
- **`source == destination`**: trivially `true` regardless of edges, since a node has a
  (zero-length) path to itself and shares a root with itself.
- **Self-loop edge** (`[u, u]`): `union(u, u)` is a no-op (same root already), harmless.
- **Disconnected graph**: nodes not reachable from `source` simply have a different root.

## Complexity

- **Time**: O((n + E) * α(n)) — initializing the DSU is O(n), processing edges is O(E) unions,
  each amortized O(α(n)).
- **Space**: O(n) for the DSU arrays.

[<- Previous](../number-of-provinces/README.md) | [Category Index](../README.md) | [Next ->](../redundant-connection/README.md)
