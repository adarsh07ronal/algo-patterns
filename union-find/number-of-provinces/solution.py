class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

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
        self.count -= 1
        return True


class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)
        return dsu.count


if __name__ == "__main__":
    sol = Solution()
    assert sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert sol.findCircleNum([[1]]) == 1
    print("ok")
