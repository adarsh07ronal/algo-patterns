# Top K Frequent Elements (Medium)

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most
frequent elements. The answer may be returned in any order.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of distinct elements in the array]`.
- It is guaranteed that the answer is unique.

## Approach

First count frequencies with a hash map (`Counter`) — this is unavoidable
O(n) work regardless of approach. The question is how to pull out the top
k *distinct values* by frequency without fully sorting all distinct values.

Maintain a **min-heap of size k**, keyed on `(frequency, value)`. Push each
`(frequency, value)` pair; whenever the heap exceeds size k, pop the
smallest (least frequent, and thus least useful to keep). After processing
every distinct value, the heap holds exactly the k pairs with the highest
frequencies, and the root is the least frequent among them.

This beats sorting all distinct values by frequency (O(d log d) where d is
the number of distinct values, which can be as large as n) because the
heap never grows past size k: each push/pop is O(log k), and there are d
of them, giving O(d log k). When k is small relative to the number of
distinct values, this is a meaningful improvement.

Note the heap is a plain min-heap here (no negation needed) — the point is
to always be able to cheaply discard the *current weakest* candidate among
the k being kept, which is precisely what a min-heap's O(log k) pop-min
gives you.

## Edge Cases

- **k equals the number of distinct elements** — the heap ends up holding
  every distinct value; nothing is ever popped once the heap first reaches
  size k+1 at the very end (or nothing is popped at all if k is exactly
  the number of unique values and pushes never exceed it by more than one
  at a time).
- **All elements identical** — one distinct value with count n; heap holds
  a single entry, trivially correct for any k in range.
- **k == 1** — heap always simplifies to holding just the single most
  frequent value once enough distinct values have been pushed and popped.
- **Frequency ties** — including the value in the heap key
  (`(freq, value)`) makes comparisons well-defined even when frequencies
  match; any tie-break is acceptable since the problem guarantees a unique
  answer set for the requested k.

## Complexity

- **Time:** O(n + d log k), where n is the array length (for counting) and
  d is the number of distinct values (for the heap operations).
- **Space:** O(d) for the frequency map, plus O(k) for the heap.

[<- Previous](../kth-largest-element-in-a-stream/README.md) | [Category Index](../README.md) | [Next ->](../kth-largest-element-in-an-array/README.md)
