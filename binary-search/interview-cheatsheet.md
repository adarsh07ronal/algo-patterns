# Binary Search: How to Remember and Code It in an Interview

Binary search interviews are lost to off-by-one bugs, not to not knowing the algorithm. Fix that by memorizing **one invariant style** and never mixing it with the other.

## Pick one invariant style and stick to it

**Closed interval `[lo, hi]`** (both ends are still candidates):
```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1                      # or lo, if you want the insertion point
```

**Half-open interval `[lo, hi)`** (searching on the answer / feasibility predicate):
```python
lo, hi = 0, upper_bound          # hi starts one-past-the-last-candidate
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid                # mid could be the answer — keep it in range
    else:
        lo = mid + 1
return lo                        # lo == hi == smallest feasible value
```

Never mix `<=` with `mid` (half-open habits) or `<` with `mid ± 1` (closed habits) in the same function — that's where infinite loops and off-by-ones come from. Pick one style before you start typing, say it out loud, and stay consistent for the whole function.

## The 2 shapes every problem here is

1. **Classic search**: array is sorted (or "sorted with a twist," like rotation), you're searching for a literal value or index. Use the closed-interval template.
2. **Search on the answer**: the *answer itself* lives on a number line, and there's a monotonic yes/no `feasible(x)` function ("can Koko finish within `h` hours at speed `x`?"). Binary search over candidate answers, not over the input array. Use the half-open template — it naturally returns "the smallest `x` for which `feasible(x)` is true," which is exactly what these problems ask for.

## The 7 problems in this category, decoded

| Problem | Shape | What `mid` represents | The monotonic condition |
|---|---|---|---|
| [Binary Search](./binary-search/README.md) | classic | an array index | `nums[mid]` vs `target` |
| [First Bad Version](./first-bad-version/README.md) | search on the answer | a version number | `isBadVersion(mid)` — false...false,true...true, find the first `true` |
| [Search in Rotated Sorted Array](./search-in-rotated-sorted-array/README.md) | classic (with a twist) | an array index | first figure out which half (`[lo,mid]` or `[mid,hi]`) is the sorted half, then check if target lies in that half's range |
| [Find First and Last Position of Element in Sorted Array](./find-first-and-last-position-of-element-in-sorted-array/README.md) | classic, run twice | an array index | once biased to find the *leftmost* match, once for the *rightmost* |
| [Search a 2D Matrix](./search-a-2d-matrix/README.md) | classic | a flattened index, mapped to `(row, col) = divmod(mid, cols)` | treat the 2D matrix as one sorted 1D array |
| [Koko Eating Bananas](./koko-eating-bananas/README.md) | search on the answer | a candidate eating speed | `hours_needed(speed) <= h` — higher speed always needs fewer-or-equal hours (monotonic) |
| [Find Peak Element](./find-peak-element/README.md) | classic-ish | an array index | compare `nums[mid]` to `nums[mid+1]`; always step toward the side that's still increasing |

## Decision checklist

1. **Is the thing I'm searching over already an array, or is it a range of possible answers?** → array → classic template. Range of possible answers with a feasibility check → search-on-the-answer template.
2. **Is the feasibility condition actually monotonic?** (`false,false,...,false,true,true,...,true` or the reverse) — if it isn't, binary search doesn't apply at all; double check this before committing.
3. **Do I need the first occurrence, last occurrence, or any occurrence?** — "any" is the plain template; "first"/"last" needs a biased template that keeps narrowing even after finding a match (don't `return` immediately on `==`, instead move `hi = mid` or `lo = mid + 1` and keep searching).
4. **Rotated / twisted sorted array?** — first determine which half is *actually* sorted by comparing `nums[lo]` to `nums[mid]`, then check if the target falls in that half's value range before deciding which half to keep.
5. **2D matrix?** — check whether it's "fully sorted as if flattened" (single binary search via `divmod`) vs. "sorted per row *and* per column but not fully flattenable" (that variant needs a different approach — staircase search from a corner, not this template).

## How to drill this so it's automatic

- Before typing a single line, say out loud: "closed interval, `lo <= hi`, `mid ± 1`" or "half-open, `lo < hi`, `hi = mid`." Committing to the sentence first prevents the mid-typing style-mixing that causes 90% of binary search bugs.
- For "search on the answer" problems, explicitly write the feasibility check as its own named function/line first (`def feasible(x): ...`) before wiring up the binary search loop around it — untangling "what am I checking" from "how do I narrow the range" is the whole difficulty.
- Trace a 4-5 element array (or a small numeric range for search-on-the-answer) by hand, writing `lo`, `hi`, `mid` at every iteration, until the loop terminates — this is the fastest way to catch an infinite loop before running the code.
- Sanity check the terminal state: closed-interval templates end with `lo == hi + 1`; half-open templates end with `lo == hi`. If your loop doesn't end in the state you expect for your chosen style, something is inconsistent.

[<- Back to Binary Search index](./README.md)
