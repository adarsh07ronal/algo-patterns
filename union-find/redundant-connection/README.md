# Redundant Connection (Medium)

## Problem

A tree with `n` nodes labeled `1` to `n` had exactly one extra edge added, turning it into a
graph with exactly one cycle. You're given `edges`, a list of `n` edges (the original tree has
`n - 1` edges, so exactly one is redundant) as pairs `[ui, vi]`. Return the edge that can be
removed to restore a tree. If multiple edges could be removed, return the one that occurs
**last** in the input.

**Example 1**

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```
Removing `[1,2]` or `[2,3]` both restore a tree, but `[2,3]` appears later in the input.

**Example 2**

```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

**Constraints**

- `n == edges.length`, `3 <= n <= 1000`
- Each `edges[i] = [ui, vi]`, `1 <= ui, vi <= n`, `ui != vi`
- No repeated edges; the resulting graph is guaranteed to have exactly one cycle.

## Approach

Each node `1..n` is a DSU element. Process edges **in input order**, calling `union(u, v)` for
each. Right before merging, check whether `u` and `v` already share a root (`find(u) == find(v)`)
— if so, this edge connects two nodes already connected by earlier edges, meaning it's the one
that closes the cycle. Because we process edges left to right and return on the *first* such
detection, and only one edge can ever close the (single) cycle, that edge is guaranteed to be
the last-occurring redundant edge in the input (any edge before it was still needed to build the
spanning tree so far).

Union-find beats DFS/BFS cycle detection here because it processes edges **incrementally and
in order**: as soon as we hit an edge whose endpoints are already connected, we have our answer
without needing to rebuild or re-scan the whole graph. A DFS-based cycle detector would need to
run a full traversal (or careful back-edge tracking) and doesn't as naturally give you "which
edge, in input order, is the one to blame."

## Edge Cases

- **Cycle formed by the very last edge**: still handled — we simply detect it on the last
  iteration.
- **Multiple edges that would each individually break the cycle**: the guarantee "return the
  one that occurs last" is satisfied automatically since we scan in order and only report the
  edge that actually triggers the same-root check.
- **Minimum size** (`n = 3`, a triangle): works the same as any other case.
- **Self-loop**: not present per constraints (`ui != vi`), so not specially handled.

## Complexity

- **Time**: O(n * α(n)) — one pass over the `n` edges, each an amortized near-O(1) `find`/`union`.
- **Space**: O(n) for the DSU parent/rank arrays.

[<- Previous](../find-if-path-exists-in-graph/README.md) | [Category Index](../README.md) | [Next ->](../accounts-merge/README.md)
