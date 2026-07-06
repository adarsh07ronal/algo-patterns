class DSU:
    """Dict-based DSU so arbitrary hashable keys (tagged row/col ids) can be unioned."""

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def _add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        self._add(x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


class Solution:
    def removeStones(self, stones):
        dsu = DSU()
        for x, y in stones:
            dsu.union(("row", x), ("col", y))

        roots = {dsu.find(("row", x)) for x, y in stones}
        return len(stones) - len(roots)


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
    assert sol.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3
    assert sol.removeStones([[0, 0]]) == 0
    print("ok")
