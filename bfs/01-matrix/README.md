# 01 Matrix (Medium)

## Problem

Given an `m x n` binary matrix `mat`, return a matrix of the same dimensions where each cell contains the distance (number of 4-directional steps) to the nearest cell containing a `0`.

**Example 1**

```
Input: mat = [[0,0,0],
              [0,1,0],
              [0,0,0]]
Output:      [[0,0,0],
              [0,1,0],
              [0,0,0]]
Explanation: the single 1 has a 0 neighbor in every direction, so its distance is 1.
```

**Example 2**

```
Input: mat = [[0,0,0],
              [0,1,0],
              [1,1,1]]
Output:      [[0,0,0],
              [0,1,0],
              [1,2,1]]
```

**Constraints**

- `1 <= m, n <= 10^4`, and `1 <= m * n <= 10^4`.
- `mat[i][j]` is `0` or `1`.
- There is at least one `0` in `mat`.

**Input representation**: `mat: List[List[int]]`.

## Approach

Computing "distance to nearest 0 for every cell" one cell at a time (BFS-ing outward from each `1` individually) would be extremely wasteful — it revisits the same territory over and over. The efficient trick is to flip the direction of the search: run a single **multi-source BFS starting from all the 0 cells at once**, expanding outward into the 1s. The first time BFS reaches a given `1` cell, it must be via the shortest path from *some* 0, and because all 0s start simultaneously at distance 0, that shortest path is the global nearest-0 distance for that cell.

Initialize a `dist` matrix with `0` at every 0-cell and push all those coordinates into the queue up front (multi-source seeding, same idea as Rotting Oranges). Mark 0-cells as visited implicitly by using the `dist` matrix itself (or a separate `visited` set) to avoid re-enqueueing. Then run standard BFS rounds: for each cell popped, look at its 4 neighbors; any neighbor not yet visited gets `dist = current_dist + 1`, gets marked visited, and is pushed onto the queue.

BFS guarantees correctness here specifically because it explores in non-decreasing order of distance from the source set — the moment a cell is first reached, that is its minimum distance, and it never needs to be revisited or recomputed with a smaller value later.

## Edge Cases

- **All cells are 0**: every distance is 0; the queue starts full and no neighbor ever needs updating.
- **Single cell matrix**: guaranteed to be `[[0]]` per constraints (at least one 0 must exist), trivially distance 0.
- **A 1 completely surrounded by 1s except for one distant 0**: still correctly computed since BFS explores ring by ring until it reaches that cell.
- **Non-square matrix**: handled generically using `rows = len(mat)`, `cols = len(mat[0])`.

## Complexity

- **Time**: O(m * n) — each cell is enqueued and processed at most once, regardless of how many 0s seed the initial queue.
- **Space**: O(m * n) for the queue and the output distance matrix in the worst case.

[<- Previous](../rotting-oranges/README.md) | [Category Index](../README.md) | [Next ->](../open-the-lock/README.md)
