# DFS: How to Remember and Code It in an Interview

DFS is one idea (go as deep as possible, then back up) wearing four different costumes depending on the input shape. Recognize which costume you're in, and the code is almost boilerplate.

## The universal skeleton

```python
def dfs(node):
    if <base case: null / out of bounds / already visited>:
        return <identity value: 0, False, None, etc.>

    mark_visited(node)                       # only needed for graphs/grids, not trees
    result = combine(dfs(child) for child in neighbors(node))
    return result
```

Trees don't need a `visited` set (no cycles, no shared references back up) — that's the tell that separates the two flavors below.

## The 4 costumes

| Costume | Input | Visited tracking | Recurses on |
|---|---|---|---|
| **Tree traversal** | `TreeNode` (`left`/`right`) | none needed — a tree has no cycles | `node.left`, `node.right` |
| **Grid flood-fill** | 2D grid | mutate grid in place (e.g. `'1' -> '0'`) *or* a `visited` set | the 4 (or 8) neighboring cells |
| **Graph traversal** | adjacency list / `Node.neighbors` | explicit `visited` set (graphs can have cycles / shared nodes) | each unvisited neighbor |
| **Cycle detection** | directed graph (e.g. course prerequisites) | **3-state** coloring: unvisited / in-progress / done — not just a boolean | neighbors, but a hit on an "in-progress" node means a cycle |

The 3-state cycle detector is the one people forget under pressure — a plain visited-boolean set can't tell "I've fully explored this and it's safe" apart from "I'm still in the middle of exploring this and just looped back to it." That distinction is exactly what makes a cycle a cycle.

## The 7 problems in this category, decoded

| Problem | Costume | What DFS returns / tracks |
|---|---|---|
| [Maximum Depth of Binary Tree](./maximum-depth-of-binary-tree/README.md) | Tree | `1 + max(dfs(left), dfs(right))`, base case `None -> 0` |
| [Path Sum](./path-sum/README.md) | Tree | bool: leaf reached with `remaining == node.val` |
| [Number of Islands](./number-of-islands/README.md) | Grid flood-fill | mutate grid to `'0'` on visit; count how many times DFS is *launched* from unvisited land |
| [Course Schedule](./course-schedule/README.md) | Cycle detection | 3-state coloring; a course reachable from itself through prerequisites = cycle = impossible |
| [Clone Graph](./clone-graph/README.md) | Graph traversal | `visited` is a `dict` mapping original node → its clone (doubles as both "seen" set and the answer) |
| [Validate Binary Search Tree](./validate-binary-search-tree/README.md) | Tree | pass down a `(low, high)` valid-range bound, shrinking it on each recursive call |
| [Surrounded Regions](./surrounded-regions/README.md) | Grid flood-fill | DFS from the **border** first to mark safe `'O'`s, then flip everything else — inverted approach vs. Number of Islands |

## Decision checklist

1. **Is the input a tree?** → no visited set needed, recursion terminates naturally at `None`. Skip straight to the recurrence.
2. **Is the input a grid or general graph?** → you need a `visited` mechanism, or you'll infinite-loop on a cycle/shared cell. Grids: either mutate in place (fastest, but destroys input) or keep a `set()` of `(row, col)`.
3. **Does the problem ask "does a cycle exist" or "is this a valid ordering"?** → plain visited isn't enough, use 3-state coloring (or track the current recursion path explicitly).
4. **Does the answer bubble up from children, or get decided while going down?** — depth/path-sum-style problems combine children's return values on the way back *up*; range-validation (BST) style problems pass constraints *down* and only need a boolean at the leaves.
5. **"Surrounded" / "enclosed" style problems** — consider DFS-ing from the border inward to find what's *safe*, then treat everything else as the answer. It's often easier than trying to detect "enclosed" directly.

## How to drill this so it's automatic

- Before coding, say out loud which of the 4 costumes you're in — that alone tells you whether you need a `visited` set and what shape it should be (boolean set, 3-state array, or a dict).
- Draw the tree/grid/graph for a tiny example (3-4 nodes) and trace the DFS call order and return values by hand before trusting the code.
- For grid problems, always double check the boundary condition (`0 <= r < rows and 0 <= c < cols`) is checked *before* indexing — this is the single most common DFS interview bug.
- For cycle detection, explicitly say: "gray/in-progress means it's still on the current call stack; hitting a gray node means back-edge means cycle" — this sentence is the whole algorithm.

[<- Back to DFS index](./README.md)
