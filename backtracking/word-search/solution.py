from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            original = board[r][c]
            board[r][c] = "#"  # sentinel: can't match any real letter

            found = (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )

            board[r][c] = original
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    assert sol.exist([row[:] for row in board], "ABCCED") is True
    assert sol.exist([row[:] for row in board], "SEE") is True
    assert sol.exist([row[:] for row in board], "ABCB") is False

    print("ok")
