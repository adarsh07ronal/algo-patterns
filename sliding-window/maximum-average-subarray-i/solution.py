from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            best_sum = max(best_sum, window_sum)

        return best_sum / k


if __name__ == "__main__":
    sol = Solution()

    assert sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert sol.findMaxAverage([5], 1) == 5.0
    assert sol.findMaxAverage([0, 1, 1, 3, 3], 4) == 2.0

    print("ok")
