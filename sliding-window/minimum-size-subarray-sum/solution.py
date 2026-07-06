from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = float("inf")

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if best == float("inf") else best


if __name__ == "__main__":
    sol = Solution()

    assert sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert sol.minSubArrayLen(4, [1, 4, 4]) == 1
    assert sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert sol.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5
    assert sol.minSubArrayLen(1, [1]) == 1

    print("ok")
