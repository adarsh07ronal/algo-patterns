# Surrounded Regions (Medium)

## Problem

Given an `m x n` board containing `'X'` and `'O'`, capture all regions that are **surrounded** by `'X'`: flip every `'O'` in such a region to `'X'`. A region is *not* surrounded (and must stay `'O'`) if it connects — via a chain of horizontally/vertically adjacent `'O'` cells — to any cell on the border of the board.

**Input representation**: `board` is a `list[list[str]]` of `'X'`/`'O'` characters, modified in place.

**Examples**

```
Input:
[
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output:
[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
(The middle blob of O's is fully enclosed and gets flipped. The bottom-left
 O touches the border, so it survives.)
```

```
Input: [["X"]]
Output: [["X"]]   (no O's at all, nothing to do)
```

**Constraints**: `1 <= m, n <= 200`; each cell is `'X'` or `'O'`.

## Approach

The naive idea — "flip any O whose region never reaches the border" — is awkward to compute directly per-region without careful bookkeeping. The standard trick flips the problem around: instead of asking "is this region surrounded," DFS **from every border cell** to find every `'O'` that is definitely *safe* (i.e., connected to the border), and mark those. Anything left over that's still `'O'` afterward, by definition, never reached the border through any path, so it must be captured.

Steps:
1. DFS/flood-fill starting from every `'O'` on the four edges of the board, marking each visited safe cell with a temporary sentinel (e.g. `'#'`).
2. After all border-connected DFS calls finish, scan the whole board: any remaining `'O'` (never reached from a border) gets flipped to `'X'` (captured); any `'#'` (was safe) gets flipped back to `'O'`.

This "search from the boundary inward" pattern is a common DFS trick whenever the condition is defined in terms of "connects to the outside" — it turns an otherwise awkward per-region computation into a single linear flood-fill pass plus a cleanup scan.

## Edge Cases

- **No `'O'` cells at all**: no DFS is ever triggered, board is unchanged.
- **All `'O'`**: every border cell is `'O'`, so DFS from the border marks the entire connected board as safe (assuming it's all one connected region reaching the border) — nothing gets captured, matching the physical intuition that an all-open board has no surrounded region.
- **Single row or single column board**: every cell is on the border by definition, so no `'O'` can ever be surrounded — the border DFS correctly marks all of them safe.
- **Region touching a corner**: corners are covered by both the top/bottom row scan and the left/right column scan without double-processing issues, since DFS marks visited cells with the sentinel immediately.
- **Multiple disjoint safe regions along different border edges**: handled independently since we DFS from every border `'O'`, not just one.
- **1x1 board**: the only cell is on the border, so if it's `'O'` it stays `'O'`.

## Complexity

- **Time**: O(m·n) — the border scan triggers DFS that visits each safe cell once total, and the final cleanup scan touches every cell once.
- **Space**: O(m·n) worst case for the DFS recursion stack (e.g. the entire board is one large safe region), no extra grid needed since we mark in place with a sentinel character.

[<- Previous](../validate-binary-search-tree/README.md) | [Category Index](../README.md)
