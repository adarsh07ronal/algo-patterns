isBadVersion = None  # injected by the judge in the real LeetCode environment


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


def make_is_bad_version(bad: int):
    """Mock API: returns True for version >= bad."""
    def isBadVersion(version: int) -> bool:
        return version >= bad
    return isBadVersion


if __name__ == "__main__":
    sol = Solution()

    isBadVersion = make_is_bad_version(4)
    assert sol.firstBadVersion(5) == 4

    isBadVersion = make_is_bad_version(1)
    assert sol.firstBadVersion(1) == 1

    isBadVersion = make_is_bad_version(1)
    assert sol.firstBadVersion(5) == 1

    isBadVersion = make_is_bad_version(5)
    assert sol.firstBadVersion(5) == 5

    print("ok")
