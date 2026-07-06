from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        current: List[int] = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return result


if __name__ == "__main__":
    sol = Solution()

    def normalize(perms):
        return sorted(tuple(p) for p in perms)

    assert normalize(sol.permute([1, 2, 3])) == normalize(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    assert normalize(sol.permute([0, 1])) == normalize([[0, 1], [1, 0]])
    assert sol.permute([5]) == [[5]]

    print("ok")
