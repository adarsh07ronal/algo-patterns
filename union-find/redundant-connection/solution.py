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
    def findRedundantConnection(self, edges):
        n = len(edges)
        dsu = DSU(n + 1)  # nodes are 1-indexed
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        return []


if __name__ == "__main__":
    sol = Solution()
    assert sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("ok")
