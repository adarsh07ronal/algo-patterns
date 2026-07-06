# Validate Binary Search Tree (Medium)

## Problem

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST satisfies, for every node:
- Every value in the node's left subtree is strictly less than the node's value.
- Every value in the node's right subtree is strictly greater than the node's value.
- Both the left and right subtrees must also be valid BSTs.

**Input representation**: a minimal `TreeNode` class with `val`, `left`, `right`. `root` may be `None`.

**Examples**

```
Input: root = [2,1,3]

    2
   / \
  1   3

Output: true
```

```
Input: root = [10,5,15,null,null,6,20]

      10
     /  \
    5    15
        /  \
       6    20

Output: false
(Node 6 sits in 10's right subtree, so it must be > 10, but 6 < 10.
 A check against only the immediate parent (15) would pass — 6 < 15 is
 fine locally — so catching this requires knowing the bound inherited
 from the grandparent, which is exactly what DFS with propagated bounds
 tracks.)
```

**Constraints**: number of nodes in `[1, 10^4]`; node values fit in a 32-bit signed integer range.

## Approach

A common bug is checking only the immediate parent-child relationship (`left.val < node.val < right.val`), but that's insufficient — the BST property is about *every* ancestor, not just the direct parent (see the example above, where `6` passes a check against its parent `15` but still invalid because it's less than the grandparent `10`, while sitting in `10`'s right subtree).

The fix is a DFS that carries a valid **range** `(low, high)` down through the recursion, narrowing it at each step:
- Start at the root with `(-infinity, +infinity)`.
- At each node, first check `low < node.val < high`; if not, fail immediately.
- Recurse left with the range narrowed to `(low, node.val)` — everything in the left subtree must stay below `node.val`, in addition to any tighter bound already inherited from higher ancestors.
- Recurse right with the range narrowed to `(node.val, high)`.
- Return `True` only if both recursive calls succeed (short-circuits on first failure).

This is exactly why DFS (not just a local check) is required: the constraint on a node depends on state accumulated from *all* its ancestors, not just its parent, and DFS is the mechanism that threads that accumulated state down the tree layer by layer.

An alternative equivalent approach is an in-order DFS traversal that should yield strictly increasing values; we use the bounds-passing version here since it makes the "why" (ancestor constraints) explicit.

## Edge Cases

- **Single node**: trivially valid (`-inf < val < inf`).
- **Duplicate values** (e.g. a node equal to its parent): invalid, since the BST property is strict (`<` and `>`, not `<=`/`>=`); the bound check `low < val < high` naturally rejects equal values.
- **Deceptive locally-valid-but-globally-invalid trees** (the classic pitfall, shown in Example 2): correctly caught because the range narrows across *all* ancestors, not just the immediate parent.
- **Skewed tree** (e.g. strictly increasing right-only chain): each step just narrows `low` upward; still O(n) and correct.
- **Extreme values** at the boundaries of the allowed value range: using `float('-inf')`/`float('inf')` as sentinels avoids off-by-one issues with integer boundaries.

## Complexity

- **Time**: O(n) — every node is visited exactly once.
- **Space**: O(h) recursion stack, where `h` is tree height — O(n) worst case (skewed), O(log n) balanced.

[<- Previous](../clone-graph/README.md) | [Category Index](../README.md) | [Next ->](../surrounded-regions/README.md)
