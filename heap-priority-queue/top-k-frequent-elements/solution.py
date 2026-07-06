import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []  # min-heap of (frequency, value), size capped at k
        for value, freq in counts.items():
            heapq.heappush(heap, (freq, value))
            if len(heap) > k:
                heapq.heappop(heap)
        return [value for _, value in heap]


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sol.topKFrequent([1], 1) == [1]
    assert sorted(sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)) == [-1, 2]
    assert sorted(sol.topKFrequent([1, 2, 3], 3)) == [1, 2, 3]
    print("ok")
