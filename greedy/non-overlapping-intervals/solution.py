from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda iv: iv[1])
        removed = 0
        last_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= last_end:
                last_end = end
            else:
                removed += 1
        return removed


if __name__ == "__main__":
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert sol.eraseOverlapIntervals([[1, 100]]) == 0
    print("ok")
