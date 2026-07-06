# Most Stones Removed with Same Row or Column (Medium)

## Problem

`stones[i] = [xi, yi]` gives the row and column of the `i`-th stone on an infinite 2D grid. A
stone can be removed if it shares a row **or** column with at least one other stone that has not
yet been removed. Return the maximum number of stones that can be removed.

**Example 1**

```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```
One valid order removes every stone except one, leaving a single survivor.

**Example 2**

```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
```
Two connected groups of stones exist ({(0,0),(2,0),(0,2),(2,2)} and {(1,1)} is isolated); each
connected group can be fully cleared down to one survivor.

**Example 3**

```
Input: stones = [[0,0]]
Output: 0
```
A single stone has nothing to share a row/column with, so it can never be removed.

**Constraints**

- `1 <= stones.length <= 1000`
- `0 <= xi, yi <= 10^4`
- No two stones occupy the same coordinate.

## Approach

Think of each stone as connecting its row and its column: if we union `("row", x)` with
`("col", y)` for every stone `(x, y)`, all stones that are transitively reachable from one
another via shared rows/columns end up in the same DSU component — this is exactly a connected
component in the graph where stones are edges between "row nodes" and "column nodes."

The key insight: within any connected group of `k` stones, you can always remove `k - 1` of them
(remove one at a time, each removal leaving at least one stone behind to justify the next
removal, until only one stone per group remains — this is always achievable by removing stones
in an order that keeps the group connected until the last one). So the answer is
`total_stones - number_of_connected_components`.

To count components without ever materializing row/column indices as separate integer ranges, a
dict-based DSU keyed by `("row", x)` / `("col", y)` tuples is used (rows and columns share the
same coordinate space, so plain integers would collide without a prefix tag). After unioning
every stone, the number of distinct roots among `{find(("row", x)) for (x, y) in stones}` is the
component count.

Union-find suits this far better than a DFS/BFS over an explicit stones-adjacency graph: building
that graph would require grouping stones by row and by column first (effectively O(n^2) pairwise
comparisons naively, or O(n) with row/column maps) before traversing. The row/column-as-node
trick lets union-find discover components in a single O(n) pass over stones with no need to ever
connect stones directly to each other.

## Edge Cases

- **Single stone**: forms its own component of size 1; `total - components = 1 - 1 = 0`,
  matching the "nothing to remove" intuition.
- **All stones share one row**: one giant component, `n - 1` stones removable.
- **Stones with no shared row/column with anything**: each is an isolated component of size 1,
  contributing 0 removable stones from that stone.
- **Duplicate coordinates**: excluded by constraints, not specially handled.

## Complexity

- **Time**: O(n * α(n)) — one union per stone (O(n) total) plus one final find per stone to
  collect roots, each amortized O(α(n)).
- **Space**: O(n) for the dict-based DSU (at most `2n` row/column keys).

[<- Previous](../satisfiability-of-equality-equations/README.md) | [Category Index](../README.md)
