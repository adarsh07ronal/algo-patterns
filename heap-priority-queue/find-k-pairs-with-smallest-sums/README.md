# Find K Pairs with Smallest Sums (Medium)

## Problem

You are given two integer arrays `nums1` and `nums2`, both sorted in
ascending order, and an integer `k`. Define a pair `(u, v)` where `u` is
from `nums1` and `v` is from `nums2`. Return the `k` pairs `(u1, v1), (u2,
v2), ...` with the smallest sums.

**Example 1:**

```
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

**Example 2:**

```
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
```

**Constraints:**
- `1 <= nums1.length, nums2.length <= 10^5`
- `-10^9 <= nums1[i], nums2[i] <= 10^9`
- `nums1` and `nums2` are sorted in non-decreasing order.
- `1 <= k <= 10^4`

## Approach

The brute-force approach generates all `len(nums1) * len(nums2)` pairs and
sorts them, which is wasteful when k is small — most pairs are never
needed. Because both arrays are sorted, we can generate pairs "on demand,
smallest first" using a heap, similar to merging k sorted lists.

Key insight: fix each index `i` in `nums1`. As `j` increases, the sum
`nums1[i] + nums2[j]` only increases (since `nums2` is sorted). So for a
fixed `i`, the smallest available pair is always `(i, 0)`, then `(i, 1)`,
and so on. This means we can treat each `i` as a lazily-generated sorted
sequence and merge all of these sequences with a **min-heap**, keyed on
the pair sum.

Seed the heap with pairs `(nums1[i] + nums2[0], i, 0)` for each `i` up to
`min(len(nums1), k)` (no need to seed more starting rows than k, since we
can never need more than k results, and `nums1` is sorted so the smallest
sums start with the smallest `nums1[i]` values). Repeatedly pop the
smallest-sum entry `(sum, i, j)`, record `(nums1[i], nums2[j])` as part of
the answer, and if `j + 1` is still in bounds, push the next candidate in
that row, `(nums1[i] + nums2[j+1], i, j+1)`. Stop once k pairs have been
collected or the heap empties.

This is a min-heap (no negation needed) because we genuinely want the
smallest sums first, popped in increasing order — exactly what `heapq`
gives natively. It costs O(k log k) (or O(min(n, k) log(min(n,k))))
instead of O(n*m log(n*m)) for generating and sorting every pair, which
matters enormously when `n` and `m` are large but `k` is comparatively
small.

## Edge Cases

- **k larger than the total number of possible pairs**
  (`k > len(nums1) * len(nums2)`) — the heap naturally empties before k
  pairs are collected; stop early and return whatever was found (this
  matches accepted behavior for this problem).
- **k == 1** — heap seeded normally, first pop gives the single smallest
  pair, which is always `(nums1[0], nums2[0])`.
- **One array has length 1** — only one starting row is seeded; the loop
  simply walks along `nums2` (or `nums1`) in order.
- **Duplicate values within or across arrays** — heap comparisons fall
  back to comparing indices when sums tie, so ties never cause an error;
  any valid set of k smallest-sum pairs is accepted.
- **Negative numbers** — sums and comparisons work identically; no special
  handling needed since Python integers compare correctly regardless of
  sign.

## Complexity

- **Time:** O(k log k) — at most `min(len(nums1), k)` initial pushes, and
  each of the up to k pops does O(1) additional pushes, all O(log k) since
  the heap never holds more than O(min(len(nums1), k)) elements at once.
- **Space:** O(min(len(nums1), k)) for the heap, plus O(k) for the output.

[<- Previous](../reorganize-string/README.md) | [Category Index](../README.md)
