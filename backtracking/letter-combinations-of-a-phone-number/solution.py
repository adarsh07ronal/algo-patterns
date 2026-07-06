from typing import List

DIGIT_TO_LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result: List[str] = []
        current: List[str] = []

        def backtrack(index: int) -> None:
            if index == len(digits):
                result.append("".join(current))
                return
            for letter in DIGIT_TO_LETTERS[digits[index]]:
                current.append(letter)
                backtrack(index + 1)
                current.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()

    assert sorted(sol.letterCombinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )
    assert sol.letterCombinations("") == []
    assert sorted(sol.letterCombinations("2")) == ["a", "b", "c"]

    print("ok")
