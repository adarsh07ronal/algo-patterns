# Reorganize String (Medium)

## Problem

Given a string `s`, rearrange the characters of `s` so that no two
adjacent characters are the same. Return any possible rearrangement, or
an empty string `""` if it is not possible.

**Example 1:**

```
Input: s = "aab"
Output: "aba"
```

**Example 2:**

```
Input: s = "aaab"
Output: ""
Explanation: No rearrangement avoids adjacent 'a's.
```

**Constraints:**
- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Approach

Intuitively, the character with the highest frequency is the hardest to
place — it needs the most "spacing" from itself. A greedy strategy works:
at every position, place the currently most frequent character that isn't
the one just placed, then decrement its remaining count. This is
essentially a scheduling problem (like "Task Scheduler"), and greedily
picking the highest-priority available item at each step is exactly what
a **max-heap keyed on remaining frequency** is built for.

Count character frequencies, then push `(-count, char)` for each distinct
character into a heap (negated because `heapq` is min-heap only, and we
want the *most* frequent character each time). At each step, pop the most
frequent character. If it's the same as the character placed immediately
before, we can't use it yet — instead pop the *next* most frequent
character, place that one, and push the previously-popped (still-pending)
character back so it's reconsidered next round. Decrement whichever
character was placed and, if it still has remaining count, push it back
onto the heap.

This beats repeatedly scanning all remaining characters for "the most
frequent one that isn't equal to the last placed" (O(26) or O(n) per
step, depending on alphabet handling) by keeping that lookup at O(log 26)
≈ O(1) per step via the heap, and generalizes correctly (no hard-coded
assumptions about alphabet size beyond using a hash map for counts).

Feasibility check: a valid arrangement exists if and only if the highest
frequency does not exceed `ceil(n / 2)` — equivalently `max_count <= (n +
1) // 2`. If this check fails up front (or equivalently, if the greedy
process ever gets stuck with only one character left that equals the
previous one and no substitute available), return `""`.

## Edge Cases

- **Single character string** (`n == 1`) — trivially valid; that one
  character is the whole answer.
- **All characters identical** (e.g. `"aaa"`) — max frequency (`3`)
  exceeds `ceil(3/2) = 2`, so impossible; return `""`.
- **Exactly at the feasibility boundary** (e.g. `"aab"`, max count 2,
  `ceil(3/2) = 2`) — just barely possible; greedy placement succeeds.
  Even length case: `"aabb"`, max count 2, `ceil(4/2)=2` — possible.
- **Two distinct characters with very different counts** (e.g. `"aaab"`)
  — infeasible, detected either by the upfront frequency check or by the
  greedy loop being unable to place the leftover majority character
  without repeating it.
- **Ties in frequency** — heap comparisons fall back to comparing
  characters when counts tie; any valid choice among tied characters
  works.

## Complexity

- **Time:** O(n log a), where n is the length of `s` and a is the number
  of distinct characters (at most 26 for lowercase letters, so
  effectively O(n)). Building the initial frequency count is O(n); each of
  the n placements does O(log a) heap work.
- **Space:** O(a) for the heap and frequency map, plus O(n) for the output
  buffer.

[<- Previous](../k-closest-points-to-origin/README.md) | [Category Index](../README.md) | [Next ->](../find-k-pairs-with-smallest-sums/README.md)
