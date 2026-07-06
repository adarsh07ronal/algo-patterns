class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def mark_safe(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "#"
            mark_safe(r + 1, c)
            mark_safe(r - 1, c)
            mark_safe(r, c + 1)
            mark_safe(r, c - 1)

        for r in range(rows):
            mark_safe(r, 0)
            mark_safe(r, cols - 1)
        for c in range(cols):
            mark_safe(0, c)
            mark_safe(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"


if __name__ == "__main__":
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(board1)
    assert board1 == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    board2 = [["X"]]
    Solution().solve(board2)
    assert board2 == [["X"]]

    all_o = [["O", "O"], ["O", "O"]]
    Solution().solve(all_o)
    assert all_o == [["O", "O"], ["O", "O"]]

    single_o = [["O"]]
    Solution().solve(single_o)
    assert single_o == [["O"]]

    single_row = [["O", "X", "O"]]
    Solution().solve(single_row)
    assert single_row == [["O", "X", "O"]]

    print("ok")
