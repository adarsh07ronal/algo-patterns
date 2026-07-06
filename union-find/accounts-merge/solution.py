from collections import defaultdict


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
    def accountsMerge(self, accounts):
        n = len(accounts)
        dsu = DSU(n)
        email_to_owner = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_owner:
                    dsu.union(i, email_to_owner[email])
                else:
                    email_to_owner[email] = i

        groups = defaultdict(set)
        for email, owner in email_to_owner.items():
            groups[dsu.find(owner)].add(email)

        result = []
        for root, emails in groups.items():
            result.append([accounts[root][0]] + sorted(emails))
        return result


if __name__ == "__main__":
    sol = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    result = sol.accountsMerge(accounts)
    normalized = sorted(tuple(acc) for acc in result)
    expected = sorted(
        tuple(acc)
        for acc in [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
    assert normalized == expected, normalized
    print("ok")
