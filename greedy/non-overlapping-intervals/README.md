# Non-overlapping Intervals (Medium)

## Problem

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove so that the rest of the intervals do not overlap. Intervals that merely touch at an endpoint (e.g. `[1,2]` and `[2,3]`) are not considered overlapping.

**Examples:**

- Input: `intervals = [[1,2],[2,3],[3,4],[1,3]]` -> Output: `1` (remove `[1,3]`, leaving `[1,2],[2,3],[3,4]` non-overlapping)
- Input: `intervals = [[1,2],[1,2],[1,2]]` -> Output: `2` (keep only one `[1,2]`, remove the other two duplicates)

**Constraints:**

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Approach

Sort intervals by their **end** time. Greedily keep an interval if its start is at or after the end of the last interval kept; otherwise it overlaps with what's already kept, so remove it (count it as a removal) and keep the previously-kept interval's end as the boundary (since it ends earlier or equal, it leaves more room for future intervals). The answer is the total number of intervals minus the number kept.

Why sort by end and always favor the earlier end when there's a conflict? This is a classic activity-selection exchange argument: among any two overlapping intervals, keeping the one that ends earlier can never do worse than keeping the one that ends later — every future interval compatible with the later-ending one is also compatible with the earlier-ending one (since its end time is <= the other's), but the reverse isn't guaranteed. So greedily discarding the later-ending interval whenever a conflict arises maximizes the number of intervals kept, which minimizes the number removed.

## Edge Cases

- Single interval -> nothing to remove, answer `0`.
- Already non-overlapping intervals -> every interval is kept, answer `0`.
- All intervals identical or fully nested -> only one survives, the rest are removed.
- Intervals that only touch at endpoints (e.g. `[1,2]` and `[2,3]`) -> not overlapping, both kept (comparison uses `start >= last_end`, not strict `>`).

## Complexity

- **Time:** O(n log n) — dominated by sorting; the greedy scan afterward is O(n).
- **Space:** O(log n) to O(n) depending on the sort implementation's overhead; O(1) extra beyond that for the scan.

[<- Previous](../partition-labels/README.md) | [Category Index](../README.md)
