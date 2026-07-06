class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
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
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert sol.validTree(1, []) is True
    print("ok")
