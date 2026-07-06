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
    def equationsPossible(self, equations):
        dsu = DSU(26)

        def idx(c):
            return ord(c) - ord('a')

        for eq in equations:
            if eq[1] == '=':
                dsu.union(idx(eq[0]), idx(eq[3]))

        for eq in equations:
            if eq[1] == '!':
                if dsu.find(idx(eq[0])) == dsu.find(idx(eq[3])):
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.equationsPossible(["a==b", "b!=a"]) is False
    assert sol.equationsPossible(["b==a", "a==b"]) is True
    assert sol.equationsPossible(["a==a"]) is True
    assert sol.equationsPossible(["a!=a"]) is False
    print("ok")
