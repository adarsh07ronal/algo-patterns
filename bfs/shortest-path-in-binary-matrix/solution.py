from collections import deque
from typing import List


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    n = len(grid)

    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1

    if n == 1:
        return 1

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    visited = {(0, 0)}
    queue = deque([(0, 0, 1)])

    while queue:
        r, c, length = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                if nr == n - 1 and nc == n - 1:
                    return length + 1
                visited.add((nr, nc))
                queue.append((nr, nc, length + 1))

    return -1


if __name__ == "__main__":
    assert shortest_path_binary_matrix([[0, 1], [1, 0]]) == 2
    assert shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert shortest_path_binary_matrix([[0]]) == 1
    assert shortest_path_binary_matrix([[1]]) == -1

    print("ok")
