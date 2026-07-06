from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        max_freq = max(freqs.values())
        max_count = sum(1 for f in freqs.values() if f == max_freq)

        frame = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), frame)


if __name__ == "__main__":
    sol = Solution()
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert sol.leastInterval(["A"], 5) == 1
    assert sol.leastInterval(["A", "A", "A", "A"], 3) == 13
    print("ok")
