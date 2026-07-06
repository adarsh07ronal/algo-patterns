import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        # Seed with the smallest pair of each row i: (nums1[i], nums2[0]).
        # No need to seed more rows than k, since nums1 is sorted.
        heap = [
            (nums1[i] + nums2[0], i, 0) for i in range(min(len(nums1), k))
        ]
        heapq.heapify(heap)

        result = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]
    assert sol.kSmallestPairs([1, 2], [3], 3) == [[1, 3], [2, 3]]
    assert sol.kSmallestPairs([], [], 1) == []
    assert sol.kSmallestPairs([1], [1], 1) == [[1, 1]]
    print("ok")
