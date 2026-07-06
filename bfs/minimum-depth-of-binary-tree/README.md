# Minimum Depth of Binary Tree (Easy)

## Problem

Given the root of a binary tree, return its minimum depth — the number of nodes along the shortest path from the root down to the nearest leaf node. A leaf is a node with no children.

**Example 1**

```
Input: root = [3,9,20,null,null,15,7]

        3
       / \
      9   20
         /  \
        15   7

Output: 2
Explanation: node 9 is a leaf at depth 2 (root counts as depth 1).
```

**Example 2**

```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
Explanation: the tree is a single right-leaning chain, so the only leaf (6) is at depth 5.
```

**Constraints**

- The number of nodes is in `[0, 10^5]`.
- `-1000 <= Node.val <= 1000`.

**Input representation**: a binary tree built from `TreeNode` objects (`val`, `left`, `right`); `root` may be `None`.

## Approach

Minimum depth is a "find the nearest thing" problem, which is exactly what BFS is built for. Seed the queue with the single `root` at depth 1. Process the tree level by level (tracking depth as a counter that increments once per full level processed), and as soon as a node is popped that has **no left and no right child** (i.e. it's a leaf), immediately return the current depth.

This works, and is more efficient than DFS, because BFS visits nodes in non-decreasing order of depth — the very first leaf it encounters is guaranteed to be at the *minimum* depth over all leaves. A DFS solution has to explore every path to the bottom of the tree and take a `min` over all of them (or aggressively prune), doing potentially much more work on trees that are deep on one side but have a shallow leaf on the other.

A common trap: a node with exactly one child is **not** a leaf, so it must not be mistaken for one — the search must continue past it into the single existing child.

## Edge Cases

- **Empty tree** (`root is None`): defined as depth 0 — checked before entering the BFS loop.
- **Single node**: it's the root and a leaf simultaneously; returns depth 1 immediately.
- **One-sided chain** (every node has exactly one child until the final node): must not terminate early at an internal node with only one child — only a node with *zero* children counts as a leaf, so depth equals the full chain length.
- **Root has two children at different subtree depths**: BFS naturally returns the shallower leaf's depth without needing to explore the deeper subtree at all once a leaf is found.

## Complexity

- **Time**: O(n) worst case (e.g. a tree with no leaves until the last level, like a complete tree missing only leaves at the very bottom), but often much better in practice since BFS stops as soon as the first leaf is found — this is the key advantage over an exhaustive DFS.
- **Space**: O(w), the maximum width of the tree at any processed level, for the queue.

[<- Previous](../average-of-levels-in-binary-tree/README.md) | [Category Index](../README.md) | [Next ->](../binary-tree-level-order-traversal/README.md)
