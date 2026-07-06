from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self._lower_bound(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self._lower_bound(nums, target + 1) - 1
        return [left, right]

    def _lower_bound(self, nums: List[int], target: int) -> int:
        """Smallest index i such that nums[i] >= target (or len(nums))."""
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert sol.searchRange([], 0) == [-1, -1]
    assert sol.searchRange([1], 1) == [0, 0]
    assert sol.searchRange([2, 2, 2, 2], 2) == [0, 3]
    assert sol.searchRange([1, 2, 3], 3) == [2, 2]
    print("ok")
