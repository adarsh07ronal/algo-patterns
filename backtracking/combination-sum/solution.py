from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []
        current: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                current.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()

    def normalize(combos):
        return sorted(sorted(c) for c in combos)

    assert normalize(sol.combinationSum([2, 3, 6, 7], 7)) == normalize([[2, 2, 3], [7]])
    assert normalize(sol.combinationSum([2, 3, 5], 8)) == normalize(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
    assert sol.combinationSum([5], 3) == []

    print("ok")
