# Kth Largest Element in an Array (Medium)

## Problem

Given an integer array `nums` and an integer `k`, return the `k`th largest
element in the array. Note that it is the `k`th largest element in sorted
order, not the `k`th distinct element.

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:**
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Approach

Maintain a **min-heap of size k** over the elements seen so far. Push each
element; whenever the heap grows past k, pop the smallest. After
processing the whole array, the heap holds exactly the k largest elements
seen, and — because it's a min-heap — its root is the smallest of those k,
which is precisely the k-th largest element overall.

This is a min-heap, not a max-heap, because the goal is the opposite of
"give me the max": we want to cheaply discard the weakest of the k
candidates we're keeping, over and over, while the heap fills. If the
whole array were sorted, `nums[-k]` would be the answer, but that costs
O(n log n) and doesn't take advantage of k possibly being much smaller
than n. The heap approach costs O(n log k) — each of the n elements
triggers at most one O(log k) push/pop pair — which is cheaper whenever
k << n. (Note: `heapq.nlargest(k, nums)[-1]` or the quickselect algorithm,
averaging O(n), are the other standard approaches; the heap is the one
that generalizes cleanly to streaming input, per the "stream" variant of
this problem.)

## Edge Cases

- **k == 1** — heap effectively just tracks the running maximum, since
  anything smaller than the current single held element gets popped
  immediately.
- **k == nums.length** — heap ends up holding the entire array; the root
  is the global minimum, which is indeed the "n-th largest" (i.e. the
  smallest) element.
- **Duplicate values** — duplicates are treated as separate heap entries;
  since the problem explicitly wants the k-th largest by sorted position
  (not by distinct value), duplicates correctly count individually toward
  k.
- **Negative numbers** — no special handling needed; heap comparisons work
  identically on negative integers.

## Complexity

- **Time:** O(n log k) — n pushes/pops, each O(log k) since the heap never
  exceeds size k.
- **Space:** O(k) for the heap.

[<- Previous](../top-k-frequent-elements/README.md) | [Category Index](../README.md) | [Next ->](../k-closest-points-to-origin/README.md)
