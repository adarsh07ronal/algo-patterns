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
    def validPath(self, n, edges, source, destination):
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.find(source) == dsu.find(destination)


if __name__ == "__main__":
    sol = Solution()
    assert sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
    assert sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False
    assert sol.validPath(1, [], 0, 0) is True
    print("ok")
