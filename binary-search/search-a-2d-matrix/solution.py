from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert sol.searchMatrix(matrix, 3) is True
    assert sol.searchMatrix(matrix, 13) is False
    assert sol.searchMatrix([[1]], 1) is True
    assert sol.searchMatrix([[1]], 2) is False
    assert sol.searchMatrix(matrix, 1) is True
    assert sol.searchMatrix(matrix, 60) is True
    print("ok")
