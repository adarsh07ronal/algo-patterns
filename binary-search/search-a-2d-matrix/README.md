# Search a 2D Matrix (Medium)

## Problem

Given an `m x n` integer matrix where each row is sorted in ascending order
and the first integer of each row is greater than the last integer of the
previous row, determine whether a given `target` value exists in the
matrix. Must run in O(log(m*n)) time.

**Examples**

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

**Constraints**
- `1 <= m, n <= 100`.
- `-10^4 <= matrix[i][j], target <= 10^4`.

## Approach

The stated property (rows sorted, and each row's first element greater than
the previous row's last element) means the whole matrix, read row by row
left to right, is equivalent to one fully sorted 1D array of length `m*n`.
So we run a single classic binary search over virtual indices `0` to
`m*n - 1`, and convert each virtual index to real coordinates with
`row, col = divmod(idx, n)`. The predicate is the same ordinary
less-than/greater-than comparison as plain binary search — the "trick" is
purely the index mapping, not a new kind of predicate.

Because the flattened view is truly sorted, discarding the half of virtual
indices that can't contain `target` is exactly as safe as in 1D binary
search, so it converges to the correct answer (or proves absence) in
O(log(m·n)).

## Edge Cases

- Single row or single column matrix: flattening still works uniformly (`n`
  is just the row width used for `divmod`).
- Target smaller than `matrix[0][0]` or larger than the last element:
  the closed-interval search correctly exits with `lo > hi`, returns
  `False`.
- Target equal to a value at the start or end of some row (a "seam"
  between rows): no special-casing needed since the flattened order
  handles seams the same as any other adjacent pair.
- `1x1` matrix: single comparison decides the result.

## Complexity

- **Time:** O(log(m·n)) — one binary search over the flattened index space.
- **Space:** O(1) — only index arithmetic, no extra structures.

[<- Previous](../find-first-and-last-position-of-element-in-sorted-array/README.md) | [Category Index](../README.md) | [Next ->](../koko-eating-bananas/README.md)
