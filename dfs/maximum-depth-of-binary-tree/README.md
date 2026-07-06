# Maximum Depth of Binary Tree (Easy)

## Problem

Given the root of a binary tree, return its maximum depth: the number of nodes along the longest path from the root down to the farthest leaf node.

**Input representation**: the tree is built from a minimal `TreeNode` class with `val`, `left`, and `right` fields (standard LeetCode style). `root` may be `None` for an empty tree.

**Examples**

```
Input: root = [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

Output: 3
```

```
Input: root = [1]
Output: 1

Input: root = []
Output: 0
```

**Constraints**: the number of nodes is in range `[0, 10^4]`; node values fit in a normal int range.

## Approach

DFS is the natural fit because "depth" is a recursive property: the depth of a tree rooted at `node` is `1 + max(depth(left), depth(right))`. We recurse to the leaves first (the base case, `None`, has depth 0), then combine the results as we unwind back up the call stack — this is a post-order DFS where the "visit" step happens *after* both children return their answers.

Nothing needs to be tracked across calls other than the return value itself; each recursive call is self-contained, which is what makes this the cleanest possible DFS: no visited set is needed since a tree has no cycles, and no shared mutable state is needed since each subtree's answer only depends on its own children.

## Edge Cases

- **Empty tree** (`root is None`): depth is `0`, handled directly as the recursion's base case.
- **Single node**: both children are `None` (depth 0 each), so the result is `1 + max(0, 0) = 1`.
- **Skewed tree** (only left or only right children): still works correctly since the recursion doesn't assume balance; depth equals the number of nodes in the single chain.
- **Unbalanced trees where one subtree is empty**: `max` correctly picks the non-empty side.

## Complexity

- **Time**: O(n) — every node is visited exactly once.
- **Space**: O(h) for the recursion call stack, where `h` is the tree's height. Worst case O(n) for a completely skewed tree; O(log n) for a balanced tree.

[Category Index](../README.md) | [Next ->](../path-sum/README.md)
