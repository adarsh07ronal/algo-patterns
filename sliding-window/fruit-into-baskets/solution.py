from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts: dict = defaultdict(int)
        left = 0
        best = 0

        for right, fruit in enumerate(fruits):
            counts[fruit] += 1

            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1

            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    sol = Solution()

    assert sol.totalFruit([1, 2, 1]) == 3
    assert sol.totalFruit([0, 1, 2, 2]) == 3
    assert sol.totalFruit([1, 2, 3, 2, 2]) == 4
    assert sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert sol.totalFruit([5]) == 1

    print("ok")
