class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict = {}
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("abba") == 2

    print("ok")
