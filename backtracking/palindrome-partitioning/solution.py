from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: List[List[str]] = []
        current: List[str] = []
        n = len(s)

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int) -> None:
            if start == n:
                result.append(current[:])
                return
            for end in range(start, n):
                if is_palindrome(start, end):
                    current.append(s[start : end + 1])
                    backtrack(end + 1)
                    current.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()

    def normalize(parts):
        return sorted(tuple(p) for p in parts)

    assert normalize(sol.partition("aab")) == normalize([["a", "a", "b"], ["aa", "b"]])
    assert sol.partition("a") == [["a"]]
    assert normalize(sol.partition("abc")) == [("a", "b", "c")]

    print("ok")
