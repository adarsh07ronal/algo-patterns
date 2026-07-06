class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * numCourses

        def has_cycle(node: int) -> bool:
            color[node] = GRAY
            for nxt in graph[node]:
                if color[nxt] == GRAY:
                    return True
                if color[nxt] == WHITE and has_cycle(nxt):
                    return True
            color[node] = BLACK
            return False

        for course in range(numCourses):
            if color[course] == WHITE and has_cycle(course):
                return False
        return True


if __name__ == "__main__":
    assert Solution().canFinish(2, [[1, 0]]) is True
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False
    assert Solution().canFinish(1, []) is True
    assert Solution().canFinish(1, [[0, 0]]) is False  # self-loop
    # diamond: 1 and 2 both depend on 0, no cycle
    assert Solution().canFinish(3, [[1, 0], [2, 0]]) is True
    # disconnected components, one has a cycle
    assert Solution().canFinish(4, [[1, 0], [3, 2], [2, 3]]) is False

    print("ok")
