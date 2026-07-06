# Satisfiability of Equality Equations (Medium)

## Problem

You are given an array of strings `equations` representing relationships between variables,
each of length 4 and either `"a==b"` or `"a!=b"` (each variable is a single lowercase letter).
Return `true` if it is possible to assign integer values to each variable satisfying all the
equations simultaneously.

**Example 1**

```
Input: equations = ["a==b","b!=a"]
Output: false
```
If `a == b`, then `b != a` is impossible to satisfy.

**Example 2**

```
Input: equations = ["b==a","a==b"]
Output: true
```
Both equations agree that `a` and `b` are equal, e.g. `a = b = 1`.

**Constraints**

- `1 <= equations.length <= 500`
- `equations[i].length == 4`
- Variables are single lowercase English letters (`'a'`-`'z'`).

## Approach

Variables that must be equal form a group; only 26 possible variables exist, so map each letter
to an index `0..25` and build a DSU of size 26. Do a first pass over `equations` and `union` the
two variables for every `"=="` equation — this groups all variables that are forced to share the
same value.

Then do a second pass over the `"!="` equations: for each one, check whether its two variables
already ended up in the same group (`find(x) == find(y)`). If they do, the equations are
contradictory (something forced them equal, but this equation demands they differ) — return
`False`. If no `"!="` equation finds its variables already unified, every constraint can be
satisfied (assign each DSU group a distinct integer) — return `True`.

Union-find fits perfectly because equality is a transitive, incremental relation exactly like
disjoint-set grouping: `a==b` and `b==c` together imply `a==c`, which union-find derives for
free via shared roots, without explicitly enumerating all implied equalities. A DFS/BFS approach
would need to build an explicit equality graph and traverse components — extra structure for the
same result. Processing `==` before `!=` is essential: equalities must be fully resolved before
any inequality check is meaningful.

## Edge Cases

- **A variable equated to itself** (`"a==a"`): unioning an index with itself is a no-op, always
  satisfiable.
- **A variable both equal and unequal to itself** (`"a!=a"`): `find(a) == find(a)` is trivially
  true, so this immediately returns `False` — correctly impossible.
- **No `"=="` equations at all**: DSU stays all singletons; any `"!="` between distinct letters
  is trivially satisfiable (they're never forced equal).
- **No `"!="` equations at all**: nothing to contradict; always `True`.
- **Equations reference letters not appearing elsewhere**: unaffected, DSU simply has an unused
  singleton for them.

## Complexity

- **Time**: O(E * α(26)) ≈ O(E) — two linear passes over the `E` equations, each `find`/`union`
  effectively O(1) since the DSU has a fixed 26 elements.
- **Space**: O(1) — the DSU arrays are fixed size 26 regardless of input size.

[<- Previous](../graph-valid-tree/README.md) | [Category Index](../README.md) | [Next ->](../most-stones-removed-with-same-row-or-column/README.md)
