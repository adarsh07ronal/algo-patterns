# Jump Game (Medium)

## Problem

Given an integer array `nums`, you start at index `0`. Each element `nums[i]` represents the maximum jump length from index `i`. Determine whether you can reach the last index.

**Examples:**

- Input: `nums = [2, 3, 1, 1, 4]` -> Output: `true` (jump 1 step to index 1, then 3 steps to the last index)
- Input: `nums = [3, 2, 1, 0, 4]` -> Output: `false` (you always land on index 3, whose max jump is 0, so index 4 is unreachable)

**Constraints:**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Approach

Scan left to right while tracking `farthest`, the farthest index reachable so far. At each index `i`, if `i > farthest` then that index (and everything past it) is unreachable, so fail immediately. Otherwise update `farthest = max(farthest, i + nums[i])`. If `farthest` ever reaches or passes the last index, succeed.

This greedy works because reachability only depends on the *farthest* point you can get to, not on which specific path or index achieved it — a smaller jump from a closer index is never better than a bigger jump from an equally-or-more-reachable index, since all that matters going forward is the single number `farthest`. Tracking the maximum collapses all reachable positions into one sufficient statistic, so there's no need to explore alternate paths (which is what a naive backtracking/DP-over-paths approach would do).

## Edge Cases

- Single-element array -> already at the last index, return `true` without looping.
- A `0` at the very start with length > 1 -> `farthest` stays at `0`, next index `1 > farthest` fails immediately (correctly `false` unless length is 1).
- A `0` somewhere in the middle that is already exceeded by an earlier bigger jump -> harmless, since `farthest` already covers past it.
- All zeros except index 0 -> only reachable if `nums.length == 1`.

## Complexity

- **Time:** O(n) — single left-to-right pass.
- **Space:** O(1) — only the `farthest` counter is kept.

[<- Previous](../best-time-to-buy-and-sell-stock-ii/README.md) | [Category Index](../README.md) | [Next ->](../gas-station/README.md)
