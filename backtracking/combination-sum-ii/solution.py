from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                current.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()

    def normalize(combos):
        return sorted(sorted(c) for c in combos)

    assert normalize(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == normalize(
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    )
    assert normalize(sol.combinationSum2([2, 5, 2, 1, 2], 5)) == normalize([[1, 2, 2], [5]])
    assert sol.combinationSum2([5], 3) == []

    print("ok")
