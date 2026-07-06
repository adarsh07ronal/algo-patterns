# Sliding Window

## Pattern

A sliding window is a contiguous range `[left, right]` over an array or string that you move across the input instead of re-scanning it from scratch for every starting position. It turns many brute-force O(n^2) "try every subarray/substring" solutions into O(n) by reusing work from the previous window instead of recomputing it.

There are two flavors:

- **Fixed-size window**: the window width `k` is given up front and never changes. You slide it one step at a time — add the incoming element on the right, remove the outgoing element on the left — updating a running aggregate (sum, count, etc.) in O(1) per step instead of recomputing the aggregate for each window from scratch.
- **Variable-size window**: the width isn't known in advance; it grows and shrinks based on a constraint (e.g., "no duplicate characters", "at most k distinct values", "sum >= target"). The classic two-pointer technique:
  1. **Expand** the window by advancing `right` and folding the new element into the window's running state.
  2. **Check** whether the window still satisfies the constraint.
  3. **Shrink** the window by advancing `left` (removing elements from the running state) until the constraint is satisfied again (or, for "at least"-type constraints, record the answer and then shrink to look for something better).

Because `left` and `right` each only move forward and never backtrack, the total work across the whole scan is O(n) even though it looks like a nested loop.

**How to recognize a sliding-window problem:**
- The question asks about a **contiguous** subarray or substring (not an arbitrary subsequence).
- There's a running constraint or quantity to track as the window changes — a sum, a count of distinct elements, a frequency map, a max/min.
- You're optimizing something (longest, shortest, max average) or checking existence, over all contiguous windows.

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| easy | [Maximum Average Subarray I](./maximum-average-subarray-i/README.md) | Fixed-size window, track running sum |
| easy | [Contains Duplicate II](./contains-duplicate-ii/README.md) | Fixed-size window as a bounded lookback set |
| medium | [Longest Substring Without Repeating Characters](./longest-substring-without-repeating-characters/README.md) | Variable window, shrink on duplicate via last-seen index |
| medium | [Longest Repeating Character Replacement](./longest-repeating-character-replacement/README.md) | Variable window, shrink when replacements needed exceed k |
| medium | [Minimum Size Subarray Sum](./minimum-size-subarray-sum/README.md) | Variable window, shrink while sum still meets target |
| medium | [Permutation in String](./permutation-in-string/README.md) | Fixed-size window, compare character frequency counts |
| medium | [Fruit Into Baskets](./fruit-into-baskets/README.md) | Variable window, shrink while more than 2 distinct types |

[<- Back to repo root](../README.md)
