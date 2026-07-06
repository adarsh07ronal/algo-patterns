from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for fast in range(len(nums)):
            if k < 2 or nums[fast] != nums[k - 2]:
                nums[k] = nums[fast]
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = sol.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [1, 1, 2, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = sol.removeDuplicates(nums)
    assert k == 7
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]

    nums = [1]
    k = sol.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [1]

    nums = [2, 2, 2, 2]
    k = sol.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [2, 2]

    print("ok")
