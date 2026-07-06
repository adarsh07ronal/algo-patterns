# Word Search (Medium)

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. The word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same cell may not be used more than once within one word path.

**Example 1:**
```
Input:  board = [["A","B","C","E"],
                  ["S","F","C","S"],
                  ["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**
```
Input:  board = [["A","B","C","E"],
                  ["S","F","C","S"],
                  ["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**
```
Input:  board = [["A","B","C","E"],
                  ["S","F","C","S"],
                  ["A","D","E","E"]], word = "ABCB"
Output: false   (the second "B" would require reusing the cell already used for the first "B")
```

**Constraints:**
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist of English letters.

## Approach

Try starting the search from every cell in the grid whose character matches `word[0]`. From a starting cell, backtracking DFS explores in all four directions (up/down/left/right): at each step the choice is "which unvisited neighboring cell matches the next character of `word`?"

To avoid reusing a cell within the current path, mark the current cell as visited before recursing (a common trick is to temporarily overwrite `board[r][c]` with a sentinel character, e.g. `'#'`, since it can't match any letter in `word`), then restore the original character (undo) after all four directions have been explored from that cell — whether or not a match was found. This in-place marking avoids allocating a separate `visited` grid.

The base case for success: the current index equals `len(word)`, meaning every character has been matched along a valid path — return `True` immediately (short-circuiting further exploration). The base case for failure at a given cell: out-of-bounds, already visited (sentinel), or character mismatch — return `False` for that branch, which causes the caller to try the next direction and eventually restore state and report failure up the call stack if all directions fail.

## Edge Cases

- **Word longer than the number of cells**: impossible to satisfy since each cell is used at most once; returns `false` (checked implicitly — the recursion never finds enough unused matching cells).
- **Single character word**: `true` if any cell matches that character.
- **Word appears but only via cell reuse** (like `"ABCB"` in Example 3): the sentinel-marking correctly rejects paths that would need to revisit a used cell.
- **Multiple valid starting cells**: the search tries every cell with a matching first letter, short-circuiting on the first success.
- **1x1 grid**: trivially checked against a one-character word.

## Complexity

- **Time:** O(m · n · 4^L) where `L = len(word)` — in the worst case every cell is tried as a start, and from each cell up to 4 directions are explored at each of the L steps (in practice branching is at most 3 after the first step, since one direction is where you came from).
- **Space:** O(L) for the recursion stack depth; no extra visited grid is needed since marking is done in place on `board`.

[<- Previous](../palindrome-partitioning/README.md) | [Category Index](../README.md) | [Next ->](../letter-combinations-of-a-phone-number/README.md)
