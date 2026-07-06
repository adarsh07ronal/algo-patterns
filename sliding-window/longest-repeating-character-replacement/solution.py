from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: dict = defaultdict(int)
        left = 0
        max_freq = 0
        best = 0

        for right, char in enumerate(s):
            counts[char] += 1
            max_freq = max(max_freq, counts[char])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    sol = Solution()

    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement("", 0) == 0
    assert sol.characterReplacement("AAAA", 0) == 4
    assert sol.characterReplacement("A", 0) == 1
    assert sol.characterReplacement("ABCDE", 5) == 5

    print("ok")
