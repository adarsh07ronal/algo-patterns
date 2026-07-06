import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        n = len(s)
        if max(counts.values()) > (n + 1) // 2:
            return ""

        # Max-heap via negation: most frequent remaining char first.
        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)

        result = []
        prev_count, prev_char = 0, ""
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            # Re-queue the previously placed char now that a step has passed.
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            prev_count, prev_char = count + 1, char  # +1 because count is negative

        return "".join(result)


if __name__ == "__main__":
    sol = Solution()

    def is_valid(original: str, result: str) -> bool:
        if result == "":
            return False
        if sorted(result) != sorted(original):
            return False
        return all(result[i] != result[i + 1] for i in range(len(result) - 1))

    assert is_valid("aab", sol.reorganizeString("aab"))
    assert sol.reorganizeString("aaab") == ""
    assert is_valid("a", sol.reorganizeString("a"))
    assert is_valid("aabb", sol.reorganizeString("aabb"))
    assert is_valid("vvvlo", sol.reorganizeString("vvvlo"))
    print("ok")
