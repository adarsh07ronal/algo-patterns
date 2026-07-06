# Number of Islands (Medium)

## Problem

Given an `m x n` 2D grid of characters `'1'` (land) and `'0'` (water), return the number of islands. An island is formed by connecting adjacent land cells horizontally or vertically (not diagonally), and is surrounded by water.

**Input representation**: `grid` is a `list[list[str]]`, each cell either `'1'` or `'0'`.

**Examples**

```
Input:
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

```
Input:
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Constraints**: `1 <= m, n <= 300`; each cell is `'0'` or `'1'`.

## Approach

This is a connected-components problem on an implicit grid graph, where two land cells are "connected" if they're horizontal/vertical neighbors. DFS (flood fill) is a great fit: whenever we find an unvisited `'1'`, it must be part of a *new* island we haven't counted yet, so we increment the island count and then DFS outward from it, marking every reachable land cell as visited so it's never counted again.

Concretely: scan every cell in row-major order. On finding a `'1'` that hasn't been visited, increment the answer, then run DFS (recursive or explicit stack) in the 4 cardinal directions, sinking every connected `'1'` by marking it visited (here, by mutating it to `'0'` in place — a common trick that avoids a separate `visited` set and its O(mn) memory, since we're allowed to consume the input grid).

The scan-and-sink pattern is standard: DFS handles "explore this whole island, don't stop until a boundary" naturally, since it doesn't need to track distance or order, just reachability.

## Edge Cases

- **All water**: no DFS is ever triggered; the answer is `0`.
- **All land**: exactly one DFS from `(0,0)` sinks the entire grid; answer is `1`.
- **Empty grid** (`grid == []` or a row is empty): loop bounds are `0`, so the answer is `0` without needing a special case.
- **Single cell** grid (`1x1`): works correctly — either `0` or `1` island depending on the cell.
- **Diagonal-only adjacency** (two land cells touching only at a corner): explicitly NOT connected since DFS only explores 4-directional neighbors, matching the problem definition.
- **Out-of-bounds neighbors**: guarded by bounds checks before recursing.

## Complexity

- **Time**: O(m·n) — every cell is visited by the outer scan once, and every land cell is visited by DFS exactly once total across all islands (each cell is sunk after its first visit).
- **Space**: O(m·n) worst case for the DFS recursion stack (e.g. a grid that is entirely one snaking island), plus O(1) extra since we mutate the grid in place instead of allocating a visited set.

[<- Previous](../path-sum/README.md) | [Category Index](../README.md) | [Next ->](../course-schedule/README.md)
