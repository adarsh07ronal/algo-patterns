class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        target = [0] * 26
        window = [0] * 26

        def idx(c: str) -> int:
            return ord(c) - ord("a")

        for i in range(n):
            target[idx(s1[i])] += 1
            window[idx(s2[i])] += 1

        matches = sum(1 for i in range(26) if target[i] == window[i])

        if matches == 26:
            return True

        for right in range(n, m):
            enter, leave = idx(s2[right]), idx(s2[right - n])

            window[enter] += 1
            if window[enter] == target[enter]:
                matches += 1
            elif window[enter] == target[enter] + 1:
                matches -= 1

            window[leave] -= 1
            if window[leave] == target[leave]:
                matches += 1
            elif window[leave] == target[leave] - 1:
                matches -= 1

            if matches == 26:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    assert sol.checkInclusion("ab", "eidbaooo") is True
    assert sol.checkInclusion("ab", "eidboaoo") is False
    assert sol.checkInclusion("adc", "dcda") is True
    assert sol.checkInclusion("abcdefg", "short") is False
    assert sol.checkInclusion("a", "a") is True

    print("ok")
