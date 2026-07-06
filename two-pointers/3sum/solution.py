from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = -nums[i]
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result


def _normalize(triplets):
    return sorted(sorted(t) for t in triplets)


if __name__ == "__main__":
    sol = Solution()

    result = sol.threeSum([-1, 0, 1, 2, -1, -4])
    assert _normalize(result) == _normalize([[-1, -1, 2], [-1, 0, 1]])

    assert sol.threeSum([0, 1, 1]) == []

    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]

    assert sol.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]

    assert sol.threeSum([1, 2, 3]) == []

    print("ok")
