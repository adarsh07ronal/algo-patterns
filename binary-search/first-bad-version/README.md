# First Bad Version (Easy)

## Problem

You are given `n` versions `[1, 2, ..., n]` and you want to find the first
bad one, which causes all following versions to also be bad. You are given
an API `isBadVersion(version)` that returns whether a given version is bad.
It is monotonic: there exists some version `k` such that
`isBadVersion` returns `False` for all `versions < k` and `True` for all
`versions >= k`. Find `k` using as few calls to `isBadVersion` as possible.

**Examples**

```
Input: n = 5, bad = 4
isBadVersion(version) -> version >= 4
Output: 4          # versions 1,2,3 are good; 4,5 are bad

Input: n = 1, bad = 1
Output: 1
```

**Constraints**
- `1 <= bad <= n <= 2^31 - 1`.

## Approach

We binary search over the *answer space* `[1, n]`, not over an array. The
monotonic predicate is `isBadVersion(mid)`: once it flips to `True` it stays
`True` for every larger version. That's exactly the "first true" boundary
pattern.

Use a half-open interval `lo = 1`, `hi = n + 1` (representing "the first bad
version is somewhere in `[lo, hi)`, and `hi` is a sentinel meaning 'no bad
version found yet, could be just past our range'"). While `lo < hi`, compute
`mid`. If `isBadVersion(mid)` is true, `mid` might be the first bad version,
so keep it in range with `hi = mid`. Otherwise `mid` is definitely good, so
`lo = mid + 1`. When the loop ends, `lo == hi` points exactly at the first
version for which the predicate is true — this is guaranteed because the
loop invariant maintains "everything before `lo` is known good" and
"`hi` (before shrinking) is either `n + 1` or a known-bad version," and the
interval shrinks by at least one element every iteration.

## Edge Cases

- `n == 1`: the only version is checked once; loop still terminates
  correctly since `lo=1, hi=2`.
- The bad version is the very first one (`k == 1`): predicate is true
  immediately at `mid == 1`, `hi` collapses down to `1`.
- The bad version is the very last one (`k == n`): `lo` climbs all the way
  up to `n` before the loop ends.
- Minimizing API calls: each iteration calls `isBadVersion` exactly once, so
  total calls are O(log n), which is the minimum possible for a monotonic
  boolean predicate over `n` candidates.

## Complexity

- **Time:** O(log n) calls to `isBadVersion`, each assumed O(1).
- **Space:** O(1) — only index variables are kept.

[<- Previous](../binary-search/README.md) | [Category Index](../README.md) | [Next ->](../search-in-rotated-sorted-array/README.md)
