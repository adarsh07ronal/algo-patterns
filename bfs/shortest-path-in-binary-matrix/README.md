# Shortest Path in Binary Matrix (Medium)

## Problem

Given an `n x n` binary grid, return the length of the shortest *clear path* from the top-left cell `(0, 0)` to the bottom-right cell `(n-1, n-1)`. A clear path consists of cells with value `0` only (both the start and end cells must be `0`), and consecutive cells in the path must be 8-directionally connected (up, down, left, right, and all 4 diagonals). Path length is the number of cells visited, including start and end. Return `-1` if no clear path exists.

**Example 1**

```
Input: grid = [[0,1],
               [1,0]]
Output: 2
Explanation: path (0,0) -> (1,1) moves diagonally, length 2.
```

**Example 2**

```
Input: grid = [[0,0,0],
               [1,1,0],
               [1,1,0]]
Output: 4
Explanation: path (0,0) -> (0,1) -> (1,2) -> (2,2), length 4, using a
diagonal move from (0,1) to (1,2) to skip past the wall of 1s.
```

**Example 3**

```
Input: grid = [[1,0,0],
               [1,1,0],
               [1,1,0]]
Output: -1
Explanation: the start cell (0,0) is a 1, so no clear path can begin.
```

**Constraints**

- `1 <= n <= 100`.
- `grid[i][j]` is `0` or `1`.

**Input representation**: `grid: List[List[int]]`.

## Approach

"Shortest path" in an unweighted grid where every move (including diagonals) costs exactly one step is the defining signature of BFS. Seed the queue with the single source `(0, 0)` — but only if it's a `0`; if either the start or end cell is blocked (`1`), no path can possibly exist, so return `-1` immediately without searching.

Track path length either as a value stored alongside each queued coordinate, or via the level-by-level "snapshot the queue size" technique, incrementing a counter once per full round. Mark cells visited the moment they're enqueued (not when dequeued) to avoid enqueueing the same cell multiple times from different neighbors in the same round. For each popped cell, check all 8 neighbors (the extra 4 diagonal directions compared to a typical grid BFS); any neighbor that is in-bounds, equal to `0`, and not yet visited gets marked visited and enqueued with `length + 1`.

Terminate as soon as the bottom-right cell `(n-1, n-1)` is dequeued (or detected during neighbor expansion) — because BFS explores in non-decreasing order of path length, that is guaranteed to be the shortest possible path length. If the queue empties without ever reaching the target, no clear path exists, so return `-1`.

## Edge Cases

- **Start or end cell blocked** (`grid[0][0] == 1` or `grid[n-1][n-1] == 1`): no valid path can exist; checked upfront and returns `-1` immediately.
- **Single-cell grid** (`n == 1`): start equals end; if that cell is `0`, the answer is `1` (a path of length 1, no moves needed) — handled by checking start == target before or immediately upon starting BFS.
- **No path exists** (target unreachable due to blocking `1`s): BFS exhausts its queue and the function falls through to return `-1`.
- **Diagonal-only shortest route**: since 8 directions are allowed, the BFS neighbor generation must include all 4 diagonals, not just the 4 orthogonal ones, or the computed shortest path would be wrong (too long or falsely `-1`).

## Complexity

- **Time**: O(n^2) — each of the n^2 cells is enqueued and processed at most once, and each expansion checks a constant 8 neighbors.
- **Space**: O(n^2) for the visited tracking and the queue in the worst case.

[<- Previous](../open-the-lock/README.md) | [Category Index](../README.md)
