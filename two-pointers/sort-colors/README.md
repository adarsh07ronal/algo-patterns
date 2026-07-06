# Sort Colors (Medium)

## Problem

Given an array `nums` with `n` objects colored red, white, or blue,
represented by the integers `0`, `1`, and `2` respectively, sort them
in-place so that objects of the same color are adjacent, in the order red,
white, blue — without using a library sort function, and in one pass.

**Example 1:**

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2:**

```
Input: nums = [2,0,1]
Output: [0,1,2]
```

**Constraints:**
- `n == nums.length`, `1 <= n <= 300`
- `nums[i]` is `0`, `1`, or `2`.

## Approach

This is the Dutch National Flag algorithm, using three same-direction
pointers: `low` and `mid` starting at index 0, and `high` starting at the
last index. The invariant maintained is: everything before `low` is `0`,
everything between `low` and `mid` is `1`, everything after `high` is `2`,
and everything from `mid` to `high` (inclusive) is unexamined.

`mid` scans forward through the unexamined region:
- If `nums[mid] == 0`, swap it with `nums[low]` (extending the "0" zone),
  then advance both `low` and `mid` — safe to advance `mid` too because the
  value swapped into `mid`'s old position came from the `0`-zone boundary
  and is known to be a `1` (or `mid == low` and nothing changes).
- If `nums[mid] == 1`, it's already in the right zone, just advance `mid`.
- If `nums[mid] == 2`, swap it with `nums[high]` (extending the "2" zone)
  and decrement `high`, but do **not** advance `mid` — the freshly-swapped
  value at `mid` came from the unexamined region and still needs to be
  classified.

Since there are only three possible values, this avoids a full O(n log n)
comparison sort entirely, and it avoids the O(n) extra space of a
counting-sort-then-overwrite approach: it sorts in place in a single O(n)
pass by directly partitioning into three contiguous regions rather than
comparing arbitrary elements against each other.

## Edge Cases

- **Single element** — loop runs at most once (or not at all), trivially
  sorted.
- **All same color** (e.g. all `1`s) — `mid` just walks to the end without
  triggering any swaps.
- **Already sorted** — swaps still happen at zone boundaries but are
  no-ops in effect (or genuinely skipped when `low == mid`).
- **Reverse sorted** (`[2,1,0]`) — exercises both swap branches
  repeatedly; the invariant still holds at every step.
- **`mid` crossing `high` after a `2`-swap** — loop condition `mid <= high`
  ensures the loop terminates exactly when the unexamined region is empty.

## Complexity

- **Time:** O(n) — `mid` moves forward on every iteration except when
  swapping with `high`, and `high` only ever decreases; both pointers make
  a bounded number of moves totaling O(n).
- **Space:** O(1) — sorting happens via in-place swaps with three index
  variables.

[<- Previous](../container-with-most-water/README.md) | [Category Index](../README.md) | [Next ->](../remove-duplicates-from-sorted-array-ii/README.md)
