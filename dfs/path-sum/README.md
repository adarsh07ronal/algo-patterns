# Path Sum (Easy)

## Problem

Given the root of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that the sum of the values along that path equals `targetSum`. A leaf is a node with no children.

**Input representation**: a minimal `TreeNode` class with `val`, `left`, `right`. `root` may be `None`.

**Examples**

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

         5
        / \
       4   8
      /   / \
     11  13  4
    / \       \
   7   2       1

Path 5 -> 4 -> 11 -> 2 sums to 22 -> Output: true
```

```
Input: root = [1,2,3], targetSum = 5
Output: false   (no root-to-leaf path sums to 5: 1+2=3, 1+3=4)

Input: root = [], targetSum = 0
Output: false   (an empty tree has no root-to-leaf path at all)
```

**Constraints**: number of nodes in `[0, 5000]`; values and `targetSum` fit in a 32-bit signed integer range.

## Approach

DFS naturally models "a path from root to a leaf" because each recursive call represents extending the current path by one node. We push the running sum down through the recursion (or equivalently subtract `node.val` from the remaining target) and only check for a match **at a leaf** — an internal node matching the target doesn't count, since the path must end at a leaf.

At each call:
1. If `root is None`, this branch contributes no path — return `False`.
2. Subtract `root.val` from the remaining target.
3. If `root` is a leaf (`no left and no right`), return whether the remaining target hit exactly `0`.
4. Otherwise, recurse into both children with the updated remaining target and return `True` if *either* finds a matching path (logical OR — we only need one path to work).

This is a top-down DFS: state (remaining sum) flows from parent to child, unlike Maximum Depth where the answer flows bottom-up.

## Edge Cases

- **Empty tree**: no path exists at all, so return `False` immediately, even if `targetSum == 0`.
- **Single node**: it is itself a leaf; return `True` iff `root.val == targetSum`.
- **Negative values**: the subtraction approach handles negative node values correctly since we're doing exact equality at the leaf, not a bound/pruning check.
- **Node with only one child**: that node is *not* a leaf, so we must not check the sum there — we must continue recursing into the existing child only (the missing child returns `False` naturally since DFS into `None` yields `False`).

## Complexity

- **Time**: O(n) — every node is visited at most once in the worst case (no matching path found).
- **Space**: O(h) recursion stack, where `h` is tree height — O(n) worst case (skewed), O(log n) for a balanced tree.

[<- Previous](../maximum-depth-of-binary-tree/README.md) | [Category Index](../README.md) | [Next ->](../number-of-islands/README.md)
