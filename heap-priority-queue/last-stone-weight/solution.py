import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max-heap via negation: heapq is min-heap only.
        heap = [-w for w in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([1]) == 1
    assert sol.lastStoneWeight([1, 1]) == 0
    assert sol.lastStoneWeight([3, 7, 2]) == 2
    print("ok")
