from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        current: List[int] = []

        def backtrack(start: int) -> None:
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()

    def normalize(subsets):
        return sorted(sorted(s) for s in subsets)

    assert normalize(sol.subsets([1, 2, 3])) == normalize(
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert normalize(sol.subsets([0])) == normalize([[], [0]])
    assert len(sol.subsets([1, 2, 3, 4, 5])) == 32

    print("ok")
