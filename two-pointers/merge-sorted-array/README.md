# Merge Sorted Array (Easy)

## Problem

You are given two integer arrays `nums1` and `nums2`, sorted in
non-decreasing order, and two integers `m` and `n` representing the number
of elements in `nums1` and `nums2` respectively. `nums1` has a length of
`m + n`, where the first `m` elements hold meaningful values and the last
`n` elements are `0` and should be ignored — they exist just to give the
array enough room. Merge `nums2` into `nums1` in place so the result is one
sorted array.

**Example 1:**

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Example 2:**

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

**Constraints:**
- `nums1.length == m + n`, `nums2.length == n`
- `0 <= m, n <= 200`, `1 <= m + n <= 200`
- Both `nums1[0..m-1]` and `nums2` are sorted in non-decreasing order.

## Approach

Two same-direction pointers, but running **backward** from the ends of the
meaningful data: `i = m - 1` (last real element of `nums1`) and
`j = n - 1` (last element of `nums2`), writing into position
`k = m + n - 1` (the last slot of `nums1`'s full length) and moving all
three pointers left as elements are placed.

Merging from the back is the key trick: `nums1` has empty (zero-valued)
trailing space, but its *front* is packed with real data. If we merged
forward like a textbook merge-sort merge, writing the smallest element
first, we would overwrite `nums1` elements we still need to read. Writing
the *largest* remaining candidate into the *last* open slot first never
overwrites data that hasn't been read yet, because we always write further
right than either pointer currently reads. This gets correctness for free
without needing an auxiliary array, and it's still just a linear merge, so
no O(n^2) shifting-and-inserting is needed.

After the loop, if `nums2` still has leftover elements, copy them in — they
are guaranteed to be the smallest remaining and already sorted among
themselves. If `nums1` has leftover elements instead, they're already in
place and need no action.

## Edge Cases

- **`n == 0`** — `nums2` is empty; nothing to merge, `nums1` is already
  correct. The loop condition `j >= 0` is false immediately.
- **`m == 0`** — `nums1`'s real portion is empty; the leftover-copy step at
  the end copies all of `nums2` in directly.
- **All of `nums2` smaller than all of `nums1`** — the main loop keeps
  picking from `nums2` until it's exhausted, then the `nums1` remainder
  (already sorted, already in place) needs no further writes.
- **All of `nums2` larger than all of `nums1`** — the main loop keeps
  picking from `nums1` until `i < 0`, then the leftover-copy step places
  the rest of `nums2` at the front.
- **Duplicate values across the two arrays** — handled naturally since ties
  are broken by taking from either array (stability doesn't matter for
  correctness here, only sortedness).

## Complexity

- **Time:** O(m + n) — each element from both arrays is visited and written
  exactly once.
- **Space:** O(1) — merging happens in place inside `nums1`, using only a
  constant number of index variables.

[<- Previous](../valid-palindrome/README.md) | [Category Index](../README.md) | [Next ->](../3sum/README.md)
