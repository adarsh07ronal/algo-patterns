# Union-Find: How to Remember and Code It in an Interview

One reusable class, memorized once, dropped unchanged into every problem. The only thing that ever changes between problems is *what a node represents* and *when you call `union`*.

## The universal DSU class (memorize this verbatim)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False              # already connected — this is how you detect a cycle
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
```

Path compression (`find` rewrites parents to point straight at the root on the way back up) plus union-by-rank (attach the shorter tree under the taller one) together give near-O(1) amortized `find`/`union` — that's the whole reason this beats redoing a BFS/DFS from scratch every time a new edge arrives.

## The one recipe every problem follows

1. Decide what a "node" is (an index `0..n-1`? a string label? a row or column of a grid?). If it isn't already a dense integer range, map each distinct label to an integer first (or use a `dict`-keyed DSU instead of a list-keyed one).
2. Loop over the given relations/edges, calling `union(a, b)` for each one that means "these are connected."
3. Derive the answer from the DSU's final state: count of distinct roots, whether two specific nodes share a root, or whatever `union` returned along the way (e.g. `union` returning `False` = redundant edge = cycle).

## The 7 problems in this category, decoded

| Problem | What a node represents | When `union` is called | How the answer is derived |
|---|---|---|---|
| [Number of Provinces](./number-of-provinces/README.md) | a city (`0..n-1`) | for every `isConnected[i][j] == 1` | count of distinct roots (`len({find(i) for i in range(n)})`) |
| [Find if Path Exists in Graph](./find-if-path-exists-in-graph/README.md) | a node (`0..n-1`) | for every given edge | `find(source) == find(destination)`? |
| [Redundant Connection](./redundant-connection/README.md) | a node (`1..n`) | for every edge, **in input order** | the first edge where `union` returns `False` (already same root) is the answer — it's the one edge creating the cycle |
| [Accounts Merge](./accounts-merge/README.md) | an **account index**, not an email | for every pair of accounts sharing an email | group accounts by root, then union all their emails together per group |
| [Graph Valid Tree](./graph-valid-tree/README.md) | a node (`0..n-1`) | for every edge | valid tree iff exactly `n-1` edges **and** no `union` call ever returned `False` (no cycle) **and** everything ends up under one root |
| [Satisfiability of Equality Equations](./satisfiability-of-equality-equations/README.md) | a variable letter, mapped to `0..25` | for every `"=="` equation (process these *first*) | for every `"!="` equation, check `find(a) != find(b)` — if they're already unioned, it's a contradiction |
| [Most Stones Removed with Same Row or Column](./most-stones-removed-with-same-row-or-column/README.md) | a **tagged** key: `("row", r)` or `("col", c)` (not the stone itself!) | for every stone, `union(("row", r), ("col", c))` | `stones - number_of_distinct_roots` = max removable (one stone must survive per connected component) |

Note the two problems that deviate from "node = array index": Accounts Merge unions **account indices** (then separately merges the email sets belonging to each root), and Most Stones Removed unions **row-tags and column-tags** rather than stones directly — a stone just becomes the edge connecting its row-node to its column-node. Recognizing when the "nodes" being unioned aren't the objects the problem talks about is the harder half of this pattern.

## Decision checklist

1. **Am I processing a fixed, static graph once**, or **incrementally adding edges/relations over time and need to answer connectivity questions in between**? Union-Find shines specifically at the second — that's when redoing a full BFS/DFS on every query would be wasteful, and DSU gives near-O(1) per update instead.
2. **Do I need to detect a cycle in an undirected graph?** → `union` returning `False` (both endpoints already share a root) *is* your cycle check — no separate visited-set/coloring logic needed (contrast with directed-graph cycle detection, which needs the 3-state DFS approach in the [DFS cheatsheet](../dfs/interview-cheatsheet.md)).
3. **Are the "nodes" actually array indices, or do I need to invent a mapping** (string → int, or a tagged tuple like `("row", 3)`) because the natural entities aren't already a dense `0..n-1` range? If so, use a `dict`-based DSU (`parent = {}` with `.setdefault`) instead of a list-based one.
4. **Is the final answer "count of groups," "are these two connected," or "is this whole structure exactly one connected tree with no cycles"?** — each maps to a different one-liner over the DSU's final `parent` array, but the DSU-building loop itself barely changes.

## How to drill this so it's automatic

- Type the `DSU` class from memory, blank, until `find` (with path compression) and `union` (with union by rank, returning `False` on cycle) come out correctly without looking anything up — this is the "skeleton" here, exactly analogous to the 6-line backtracking skeleton.
- For every new problem, answer just one question out loud first: "what is a node, here?" — once that's settled, the rest of the code is almost always the same 3-line loop calling `union`.
- Hand-trace `parent[]` array contents after each `union` call on a tiny 4-5 node example — this is what makes path compression and "count distinct roots" click instead of feeling like magic.
- Remember `union` returning a boolean is doing double duty: use it directly for cycle detection instead of writing a separate `find(a) == find(b)` check before calling `union`.

[<- Back to Union-Find index](./README.md)
