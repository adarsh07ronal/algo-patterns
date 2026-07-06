# Number of Provinces (Easy)

## Problem

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i`-th and
`j`-th cities are directly connected, and `0` otherwise. A **province** is a group of directly
or indirectly connected cities. Return the total number of provinces.

**Example 1**

```
Input: isConnected = [[1,1,0],
                       [1,1,0],
                       [0,0,1]]
Output: 2
```
City 0 and city 1 are directly connected, forming one province; city 2 is isolated, forming a
second province.

**Example 2**

```
Input: isConnected = [[1,0,0],
                       [0,1,0],
                       [0,0,1]]
Output: 3
```
No city is connected to any other, so every city is its own province.

**Constraints**

- `1 <= n <= 200`
- `isConnected[i][j]` is `0` or `1`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]` (symmetric)

## Approach

Each city `i` is an element in the DSU, so we start with `n` singleton sets (`count = n`).
Scan every pair `(i, j)` with `i < j`; whenever `isConnected[i][j] == 1`, call `union(i, j)` to
merge their sets. Each successful union (the two were in different sets) decrements the running
component count by one.

After processing all pairs, the number of distinct roots left in the DSU **is** the number of
provinces — no extra bookkeeping needed if the DSU maintains a live `count`.

Union-find fits naturally because the "edges" here are just presence flags in a matrix with no
inherent traversal order requirement: we don't need to explore neighbors recursively (as DFS/BFS
would), we only need to know, for each pair, whether they end up in the same group. A single
linear pass over pairs with union-find is simpler to reason about than tracking a `visited` set
and launching a DFS from every unvisited node, though both approaches are O(n^2) here.

## Edge Cases

- **n = 1**: single city, matrix is `[[1]]` — DSU starts and ends with 1 set, answer is `1`.
- **Fully connected matrix** (all 1s): every union succeeds until one set remains, answer is `1`.
- **Fully disconnected** (identity matrix): no unions ever fire, answer stays `n`.
- **Matrix symmetry**: only iterating `j > i` avoids redundant/duplicate union calls without
  affecting correctness, since `isConnected[i][j] == isConnected[j][i]`.

## Complexity

- **Time**: O(n^2 * α(n)) — we inspect every cell in the upper triangle of the matrix once,
  and each `union`/`find` costs amortized O(α(n)), effectively constant.
- **Space**: O(n) for the DSU parent/rank arrays.

[Category Index](../README.md) | [Next ->](../find-if-path-exists-in-graph/README.md)
