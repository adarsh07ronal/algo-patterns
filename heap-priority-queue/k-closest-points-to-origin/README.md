# K Closest Points to Origin (Medium)

## Problem

Given an array of `points` where `points[i] = [xi, yi]` represents a point
on the X-Y plane and an integer `k`, return the `k` closest points to the
origin `(0, 0)`. The distance between two points is the Euclidean
distance. The answer may be returned in any order.

**Example 1:**

```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
distance([1,3])  = sqrt(10)
distance([-2,2]) = sqrt(8)
Since sqrt(8) < sqrt(10), [-2,2] is closer.
```

**Example 2:**

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

**Constraints:**
- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Approach

Distance ranking only requires *comparing* distances, so the square root
can be skipped entirely — squared distance (`x*x + y*y`) preserves the
same ordering and avoids floating point. That's the key simplification;
the heap mechanics are the same "keep the best k" pattern used elsewhere
in this category.

Maintain a **max-heap of size k**, keyed on squared distance, simulated
via negation (push `(-dist_sq, point)`). Push each point's negated
squared distance; whenever the heap exceeds size k, pop the max (i.e. the
most negative entry, which is the point *farthest* from the origin among
those currently kept). After processing all points, the heap holds
exactly the k closest points.

A max-heap (not min) is the right choice here because, unlike "find the
k-th largest," this problem wants to actively evict the *worst* candidate
(farthest point) as better ones are discovered — the heap's root needs to
be "the one I'd throw out first," which is the farthest, i.e. the max
distance among the kept set. This costs O(n log k), versus O(n log n) to
sort every point by distance when k is much smaller than n.

## Edge Cases

- **k == points.length** — every point ends up in the heap; nothing
  meaningful is ever evicted (or the single farthest point is popped and
  never matters since it's immediately clear all n are wanted... in
  practice the heap simply grows to size k = n without ever exceeding it).
- **k == 1** — heap holds only the single closest point seen so far,
  replacing it whenever a strictly closer point arrives (ties are broken
  arbitrarily by heap order, which is acceptable since any point at the
  minimum distance is a valid answer).
- **Duplicate points / duplicate distances** — heap comparisons fall back
  to comparing the point tuples when distances tie; correctness is
  unaffected since either point is a valid answer at that distance.
- **Point exactly at the origin** — squared distance is 0, guaranteed to
  be kept (it's the smallest possible distance).

## Complexity

- **Time:** O(n log k) — n pushes, each O(log k) since the heap is capped
  at size k.
- **Space:** O(k) for the heap.

[<- Previous](../kth-largest-element-in-an-array/README.md) | [Category Index](../README.md) | [Next ->](../reorganize-string/README.md)
