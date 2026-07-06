# Kth Largest Element in a Stream (Easy)

## Problem

Design a class `KthLargest` that keeps track of the `k`th largest element
in a stream of integers.

- `KthLargest(k, nums)` initializes the object with the integer `k` and an
  initial stream of integers `nums`.
- `add(val)` appends `val` to the stream and returns the element
  representing the `k`th largest element in the stream so far.

**Example:**

```
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);  // stream = [4,5,8,2,3],        3rd largest = 4
kthLargest.add(5);  // stream = [4,5,8,2,3,5],      3rd largest = 5
kthLargest.add(10); // stream = [4,5,8,2,3,5,10],   3rd largest = 5
kthLargest.add(9);  // stream = [4,5,8,2,3,5,10,9], 3rd largest = 8
kthLargest.add(4);  // stream = [...,4],            3rd largest = 8
```

**Constraints:**
- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- It's guaranteed there will be at least `k` elements in the array when
  you search for the `k`th element.
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.

## Approach

The trick is to never keep the whole stream sorted. Keep a **min-heap of
exactly size k** holding the k largest values seen so far; its root (the
smallest of those k) is, by construction, the k-th largest value overall.

On construction, push all initial values through this size-k discipline:
push a value, and if the heap grows past k, pop the smallest. After
processing everything, the heap holds the k largest values and its root
answers the query directly — no negation trick needed here because we
want the *smallest of the top-k*, which is exactly what a plain min-heap
root gives you.

On `add(val)`, push the new value, and if the heap now has more than k
elements, pop the min. Either way, the heap always ends the call with at
most k elements, and its root is the answer. This costs O(log k) per call
instead of re-sorting the whole growing stream (O(n log n)) or re-scanning
it (O(n)) on every single `add`.

## Edge Cases

- **Initial `nums` shorter than k** — allowed as long as the stream
  reaches at least k elements by the time `add` is queried; the heap
  simply grows toward size k without popping until it exceeds k.
- **Initial `nums` empty** — heap starts empty; behaves the same as above.
- **k == 1** — heap holds only the single largest value; every `add` that
  beats it replaces it.
- **Duplicate values in the stream** — heap comparisons treat equal values
  as interchangeable; correctness is unaffected since we only care about
  values, not identity.
- **`add` called with a value smaller than everything in the heap once
  full** — value is pushed then immediately popped back off, leaving the
  k-th largest unchanged.

## Complexity

- **Time:** O(n log k) to build from n initial values, and O(log k) per
  `add` call.
- **Space:** O(k) — the heap never holds more than k elements.

[<- Previous](../last-stone-weight/README.md) | [Category Index](../README.md) | [Next ->](../top-k-frequent-elements/README.md)
