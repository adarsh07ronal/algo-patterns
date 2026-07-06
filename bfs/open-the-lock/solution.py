from collections import deque
from typing import List


def open_lock(deadends: List[str], target: str) -> int:
    dead = set(deadends)
    start = "0000"

    if start in dead:
        return -1
    if start == target:
        return 0

    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        state, turns = queue.popleft()
        for i in range(4):
            digit = int(state[i])
            for delta in (-1, 1):
                new_digit = (digit + delta) % 10
                neighbor = state[:i] + str(new_digit) + state[i + 1:]
                if neighbor in visited or neighbor in dead:
                    continue
                if neighbor == target:
                    return turns + 1
                visited.add(neighbor)
                queue.append((neighbor, turns + 1))

    return -1


if __name__ == "__main__":
    assert open_lock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert open_lock(["8888"], "0009") == 1
    assert open_lock(["0000"], "8888") == -1
    assert open_lock([], "0000") == 0

    print("ok")
