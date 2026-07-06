# Container With Most Water (Medium)

## Problem

Given `n` non-negative integers `height[0..n-1]`, where each represents a
vertical line at position `i` with height `height[i]`, find two lines that,
together with the x-axis, form a container that holds the most water.
Return the maximum amount of water it can store.

**Example 1:**

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: lines at index 1 (height 8) and index 8 (height 7) form a
container of width 7 and height min(8,7)=7, area = 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Constraints:**
- `n == height.length`, `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Approach

Start with two opposite-direction pointers, `left = 0` and
`right = n - 1` — the widest possible container. At each step compute the
area `min(height[left], height[right]) * (right - left)`, track the
maximum seen, then move inward the pointer at the **shorter** line.

The reason this greedy move is safe (and doesn't need to check every pair,
avoiding O(n^2)) is: the container's height is capped by the shorter of the
two lines. If we keep the shorter line fixed and move the taller line
inward, the width shrinks while the height cap stays the same or gets
worse (bounded by the same short line, or an even shorter one) — so that
move could never produce a better area than what we already measured.
Moving the *shorter* line inward is the only move that has a chance of
increasing the height cap (a taller line further in), which might
compensate for the reduced width. So at every step, discarding the shorter
line's current position is provably safe — no better container can include
it — which means we never need to re-examine it, and the two pointers
together only take O(n) total steps to consider every "surviving"
candidate pair implicitly.

## Edge Cases

- **All lines the same height** (e.g. `[3,3,3,3]`) — pointer movement
  degenerates to always moving one side, but the widest pair is checked
  first and is optimal since height is constant.
- **Two elements only** — loop runs exactly once, returns the only
  possible area.
- **Strictly increasing or decreasing heights** — one pointer does nearly
  all the moving; still correct since the algorithm doesn't assume
  symmetry.
- **Zero-height lines** — a container touching a `0` line has area `0`,
  which is naturally never chosen as the max unless it's the only option
  (e.g. `[0,0]`).
- **Tie in height between `left` and `right`** — moving either pointer is
  safe to move (commonly the convention is to move `left`), since both
  lines equally cap the height and are equally safe to discard.

## Complexity

- **Time:** O(n) — `left` and `right` together traverse the array once,
  moving strictly toward each other until they meet.
- **Space:** O(1) — only a few scalar variables are used.

[<- Previous](../3sum/README.md) | [Category Index](../README.md) | [Next ->](../sort-colors/README.md)
