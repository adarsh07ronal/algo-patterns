from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child


if __name__ == "__main__":
    sol = Solution()
    assert sol.findContentChildren([1, 2, 3], [1, 1]) == 1
    assert sol.findContentChildren([1, 2], [1, 2, 3]) == 2
    assert sol.findContentChildren([], [1, 2]) == 0
    assert sol.findContentChildren([1, 2], []) == 0
    print("ok")
