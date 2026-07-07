# Sliding Window: How to Remember and Code It in an Interview

One skeleton, one knob: **is the window a fixed size, or does it grow and shrink?** Everything else — what you track inside the window, when you update the answer — falls out of that single decision.

## The universal skeleton

**Fixed size `k`:**
```python
window_state = init()               # e.g. running sum, Counter()
for right in range(len(nums)):
    add(nums[right], window_state)              # expand

    if right >= k - 1:
        update_answer(window_state)              # window is exactly size k — record it
        remove(nums[right - k + 1], window_state)  # shrink from the left before next expand
```

**Variable size (grow until invalid, then shrink until valid again):**
```python
left = 0
window_state = init()
for right in range(len(nums)):
    add(nums[right], window_state)               # expand

    while <window is invalid, e.g. too many distinct chars, sum too big>:
        remove(nums[left], window_state)          # shrink
        left += 1

    update_answer(right - left + 1)               # window [left, right] is now valid — record it
```

The `while`, not `if`, on the shrink step is the detail people drop under pressure — a single `if` might leave the window still invalid after one shrink; `while` guarantees you always end each iteration with a valid (or empty) window.

## The 7 problems in this category, decoded

| Problem | Fixed or variable? | What's tracked in the window | When the answer updates |
|---|---|---|---|
| [Maximum Average Subarray I](./maximum-average-subarray-i/README.md) | fixed (`k`) | running sum | every time window reaches size `k` |
| [Contains Duplicate II](./contains-duplicate-ii/README.md) | fixed (`k`, but framed as "within distance k") | a set/dict of values currently in window | before adding the new value, check if it's already in the window |
| [Longest Substring Without Repeating Characters](./longest-substring-without-repeating-characters/README.md) | variable | last-seen index of each character | every time the window is valid (no repeats), compare `right - left + 1` to best |
| [Longest Repeating Character Replacement](./longest-repeating-character-replacement/README.md) | variable | char frequency counts + running max frequency | shrink when `window_size - max_freq_char_count > k`; then compare size to best |
| [Minimum Size Subarray Sum](./minimum-size-subarray-sum/README.md) | variable | running sum | shrink *while* `sum >= target`, updating the min length on every successful shrink |
| [Permutation in String](./permutation-in-string/README.md) | fixed (`len(s1)`) | char frequency count of window vs. target frequency count | every time window reaches size `len(s1)`, compare frequency counts |
| [Fruit Into Baskets](./fruit-into-baskets/README.md) | variable | frequency count of fruit types currently in window | shrink while more than 2 distinct types; compare size to best on every valid window |

## Decision checklist

1. **Is a window size explicitly given (`k`)?** → fixed-size template: expand, and once you've expanded `k` times, record + shrink in lockstep (one in, one out, every iteration after the window first fills).
2. **Is the problem "find the longest/shortest substring/subarray such that `<constraint>`"?** → variable-size template: expand always; shrink only when the constraint breaks (longest) or shrink to look for something even shorter once it's already satisfied (shortest, e.g. Minimum Size Subarray Sum).
3. **What breaks the window's validity?** — too many distinct characters, a frequency count exceeding what's allowed, sum exceeding/undershooting a target. Whatever that condition is becomes the `while` guard.
4. **Frequency-comparison problems** (Permutation in String) are really fixed-size sliding window plus "compare two frequency tables" instead of a single running number — same skeleton, richer window state.
5. **Am I about to write nested loops recomputing the sum/count from scratch each time?** That's the O(n²) brute force this pattern replaces — the window should only ever do O(1) work to add/remove one element, never re-scan.

## How to drill this so it's automatic

- Say out loud first: "fixed or variable?" — that answer alone picks which of the two skeletons above you're writing.
- For variable-size "longest" problems, the answer update goes *after* the shrink loop (window is now guaranteed valid). For "shortest" problems, the update happens *inside* the shrink loop (you're recording every size that still satisfies the condition, looking for the smallest).
- Hand-trace `right` and `left` moving through a 5-6 character string, writing out the window state at each step — this is what catches whether you should be using `while` vs `if`, and whether the answer update belongs inside or after the shrink loop.
- Watch for "exactly k distinct" style problems (not in this set, but common) — those are usually solved as `atMost(k) - atMost(k-1)`, a variant worth remembering exists even if you don't need it here.

[<- Back to Sliding Window index](./README.md)
