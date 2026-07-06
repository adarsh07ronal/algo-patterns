from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        light, heavy = 0, len(people) - 1
        boats = 0
        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                light += 1
            heavy -= 1
            boats += 1
        return boats


if __name__ == "__main__":
    sol = Solution()
    assert sol.numRescueBoats([1, 2], 3) == 1
    assert sol.numRescueBoats([3, 2, 2, 1], 3) == 3
    assert sol.numRescueBoats([3, 5, 3, 4], 5) == 4
    assert sol.numRescueBoats([5], 5) == 1
    print("ok")
