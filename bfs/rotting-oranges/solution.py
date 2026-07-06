from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    minutes = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue and fresh_count > 0:
        rotted_this_round = False
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))
                    rotted_this_round = True
        if rotted_this_round:
            minutes += 1

    return minutes if fresh_count == 0 else -1


if __name__ == "__main__":
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert oranges_rotting(grid1) == 4

    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert oranges_rotting(grid2) == -1

    # No fresh oranges
    assert oranges_rotting([[0, 2]]) == 0

    # No rotten, some fresh -> impossible
    assert oranges_rotting([[1]]) == -1

    print("ok")
