import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # max-heap (via negation) of the k closest points so far
        for x, y in points:
            dist_sq = x * x + y * y
            heapq.heappush(heap, (-dist_sq, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    sol = Solution()
    assert sol.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    result = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(result) == sorted([[3, 3], [-2, 4]])
    assert sol.kClosest([[0, 0]], 1) == [[0, 0]]
    assert sorted(sol.kClosest([[1, 1], [2, 2], [3, 3]], 3)) == [[1, 1], [2, 2], [3, 3]]
    print("ok")
