from collections import deque
from typing import List


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    rows, cols = len(mat), len(mat[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist


if __name__ == "__main__":
    mat1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert update_matrix(mat1) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    mat2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert update_matrix(mat2) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

    # All zeros
    assert update_matrix([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]

    # Single cell
    assert update_matrix([[0]]) == [[0]]

    print("ok")
