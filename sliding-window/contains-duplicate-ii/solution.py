from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window: set = set()

        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if i >= k:
                window.remove(nums[i - k])

        return False


if __name__ == "__main__":
    sol = Solution()

    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
    assert sol.containsNearbyDuplicate([1, 1], 0) is False
    assert sol.containsNearbyDuplicate([1], 1) is False
    assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) is True

    print("ok")
