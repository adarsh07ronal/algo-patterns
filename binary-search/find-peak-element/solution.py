from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.findPeakElement([1, 2, 3, 1]) == 2
    assert sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
    assert sol.findPeakElement([1]) == 0
    assert sol.findPeakElement([1, 2, 3, 4, 5]) == 4
    assert sol.findPeakElement([5, 4, 3, 2, 1]) == 0
    print("ok")
