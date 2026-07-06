# Partition Labels (Medium)

## Problem

Given a string `s`, partition it into as many contiguous parts as possible so that each letter appears in at most one part (i.e., no letter is split across two parts). Return a list of the sizes of these parts, in order.

**Examples:**

- Input: `s = "ababcbacadefegdehijhklij"` -> Output: `[9, 7, 8]` (partitions: `"ababcbaca"`, `"defegde"`, `"hijhklij"`)
- Input: `s = "eccbbbbdec"` -> Output: `[10]` (every letter's last occurrence forces one single partition)

**Constraints:**

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters

## Approach

First record the last index at which each letter occurs anywhere in `s`. Then scan left to right, maintaining `end`, the farthest "last occurrence" seen among letters encountered so far in the current partition. When the scan pointer `i` reaches `end`, the current partition can safely close here — every letter seen since the partition started has its last occurrence at or before `i`, so none of them will reappear later and force merging with the next partition.

This is safe because a partition boundary at `i` is valid exactly when no letter seen so far still has an occurrence beyond `i` — which is precisely what tracking the running max of last-occurrence indices detects. Closing as soon as this condition is met (rather than waiting longer) is what maximizes the number of partitions: any earlier boundary would violate the no-split rule (some letter's last occurrence lies past it), so this is the earliest — and therefore most partitions produce the greedy way — valid cut point, and taking the earliest valid cut repeatedly is always at least as good as taking a later one, since a later cut can only merge what could otherwise have been separate parts.

## Edge Cases

- Single character string -> one partition of size `1`.
- Every character distinct -> each becomes its own partition of size `1`.
- Every character the same -> a single partition covering the whole string.
- A letter's last occurrence is at the very end of the string -> forces the final partition to extend all the way to the end.

## Complexity

- **Time:** O(n) — one pass to find last occurrences, one pass to build partitions (n = len(s)).
- **Space:** O(1) extra beyond the output — the last-occurrence table is bounded by the 26-letter alphabet.

[<- Previous](../task-scheduler/README.md) | [Category Index](../README.md) | [Next ->](../non-overlapping-intervals/README.md)
