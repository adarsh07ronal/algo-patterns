# Two Pointers: How to Remember and Code It in an Interview

Two flavors, one question to tell them apart: **are the pointers moving toward each other, or in the same direction?**

## The 2 skeletons

**Opposite ends, converging** (needs sorted input, or a palindrome-style mirror check):
```python
left, right = 0, len(nums) - 1
while left < right:
    if <condition met at (left, right)>:
        record_or_return(left, right)
        left += 1
        right -= 1
    elif <need a bigger value>:
        left += 1
    else:
        right -= 1
```

**Same direction, fast/slow** (in-place array rewriting — one pointer reads ahead, the other marks where to write next):
```python
slow = 0
for fast in range(len(nums)):
    if <nums[fast] should be kept>:
        nums[slow] = nums[fast]
        slow += 1
return slow          # new length; everything before index `slow` is the answer
```

The tell: if the problem is "does a pair/triplet exist matching some sum/condition" on **sorted** data, reach for converging pointers. If the problem is "remove/compact/partition this array in place," reach for fast/slow.

## The 7 problems in this category, decoded

| Problem | Which skeleton | What each pointer represents |
|---|---|---|
| [Valid Palindrome](./valid-palindrome/README.md) | converging | `left`/`right` mirror inward from both ends, skipping non-alphanumeric chars |
| [Merge Sorted Array](./merge-sorted-array/README.md) | same-direction (but written **backwards**, from the end) | write pointer at the true end of `nums1`; two read pointers, one per array, both scanning from their own ends |
| [3Sum](./3sum/README.md) | converging (nested inside a loop over the 3rd element) | outer loop fixes one number; `left`/`right` converge over the sorted remainder to find pairs summing to `-nums[i]` |
| [Container With Most Water](./container-with-most-water/README.md) | converging | `left`/`right` start at the widest container and move the **shorter** wall inward each step |
| [Sort Colors](./sort-colors/README.md) | same-direction, but **3 pointers** (Dutch National Flag): `low`, `mid`, `high` | `low` boundary of 0s, `high` boundary of 2s, `mid` scans and swaps into place |
| [Remove Duplicates from Sorted Array II](./remove-duplicates-from-sorted-array-ii/README.md) | same-direction fast/slow | `slow` marks the next write position; keep `nums[fast]` only if it doesn't create a 3rd consecutive duplicate (compare to `nums[slow-2]`) |
| [Boats to Save People](./boats-to-save-people/README.md) | converging | sort by weight; pair the heaviest (`right`) with the lightest (`left`) if they fit together, else the heaviest goes alone |

## Decision checklist

1. **Is the array sorted (or can I sort it without breaking the problem)?** → converging pointers become available. If the problem needs original indices/order preserved, sorting isn't free — check the problem allows it (3Sum returns values, not indices, so sorting is safe there).
2. **Am I searching for a pair/triplet matching a target sum or condition?** → converging pointers turn an O(n²) nested-loop search into O(n) per fixed element, since moving `left` up or `right` down is a monotonic, one-directional decision once sorted.
3. **Am I compacting or removing elements in place?** → same-direction fast/slow: `fast` explores, `slow` marks the last confirmed-good write position. The invariant to state out loud: "everything before `slow` is already correct; everything between `slow` and `fast` doesn't matter yet."
4. **Do I need more than 2 partitions** (0s/1s/2s, not just 2 groups)? → 3-pointer Dutch flag variant: `low`/`mid`/`high`, still same-direction in spirit but the region between `mid` and `high` is unexplored, not "doesn't matter."
5. **Which wall/pointer do I move when neither side satisfies the condition?** — in Container With Most Water, always move the *shorter* wall (moving the taller one can only shrink the area, since width decreases and height is still capped by the shorter side either way).

## How to drill this so it's automatic

- State out loud first: "converging or same-direction?" — that answer picks the skeleton; everything else is filling in the specific condition.
- For fast/slow problems, say the invariant sentence explicitly: "before `slow`: finalized answer. Between `slow` and `fast`: garbage, not yet looked at. After `fast`: unexplored." This is what interviewers listen for to confirm you understand *why* the in-place trick is correct, not just that it happens to work.
- Hand-trace `left`/`right` (or `slow`/`fast`) positions on a 5-6 element sorted array — this catches whether your loop condition should be `<` or `<=`, and whether you increment both pointers or just one per iteration.
- For "remove in place" problems, remember the return contract: you return a **length**, and only the first `length` elements of the array are required to be correct — anything after that can be left as garbage.

[<- Back to Two Pointers index](./README.md)
