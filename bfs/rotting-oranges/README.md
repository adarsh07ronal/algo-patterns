# Rotting Oranges (Medium)

## Problem

You are given an `m x n` grid where each cell can have one of three values:

- `0`: an empty cell
- `1`: a fresh orange
- `2`: a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

**Example 1**

```
Input: grid = [[2,1,1],
               [1,1,0],
               [0,1,1]]
Output: 4
Explanation: rot spreads outward from the single rotten orange at (0,0),
reaching the farthest fresh orange after 4 minutes.
```

**Example 2**

```
Input: grid = [[2,1,1],
               [0,1,1],
               [1,0,1]]
Output: -1
Explanation: the orange at (2,0) is isolated by zeros and can never rot.
```

**Constraints**

- `1 <= m, n <= 10`.
- `grid[i][j]` is `0`, `1`, or `2`.

**Input representation**: `grid: List[List[int]]`.

## Approach

This is a **multi-source** BFS: rot doesn't spread from a single starting point but from every rotten orange simultaneously, all at minute 0. So instead of seeding the queue with one cell, scan the whole grid first and push every cell that is already `2` into the queue (also counting the number of fresh oranges as we scan, so we can tell later whether any are left unrotted).

Then run standard multi-level BFS: process the queue in rounds ("minutes"). For each rotten cell popped in the current round, look at its 4 neighbors; any neighbor that is fresh (`1`) becomes rotten (`2`), gets decremented from the fresh count, and gets pushed onto the queue for the *next* round. After a full round with at least one newly-rotted orange, increment the minute counter.

BFS (rather than DFS) is essential here because the answer is literally "how many *simultaneous* rounds of spreading are needed," which is exactly the level structure BFS produces — round `k` of the BFS corresponds to minute `k`. A DFS would not naturally model the "everything spreads together" semantics.

Termination: stop when the queue empties. At that point, if `fresh_count == 0`, return the number of minutes elapsed; otherwise some fresh oranges are unreachable, so return `-1`.

## Edge Cases

- **No fresh oranges at all**: `fresh_count` starts at 0, so the loop can be skipped (or runs zero effective rounds) and the answer is `0` minutes.
- **No rotten oranges but some fresh ones**: queue starts empty, so no BFS rounds occur, `fresh_count` stays positive, and the answer is `-1`.
- **Isolated fresh oranges** (surrounded by 0s / unreachable): correctly left un-rotted, leading to a final `-1`.
- **Grid entirely rotten or entirely empty**: `fresh_count` is 0, answer is `0`.
- **Off-by-one on the minute count**: the minute counter must only increment after a round that actually rotted at least one orange (or equivalently, increment per round and simply not count the initial seeding round) — handled by incrementing only when the queue for the next round is non-empty before moving on.

## Complexity

- **Time**: O(m * n) — every cell is enqueued and processed at most once.
- **Space**: O(m * n) for the queue in the worst case (e.g. a grid that is mostly rotten already).

[<- Previous](../binary-tree-level-order-traversal/README.md) | [Category Index](../README.md) | [Next ->](../01-matrix/README.md)
