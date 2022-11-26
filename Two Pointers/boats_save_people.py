"""
Time O(Log(N)) only traverse the array once but require NlogN,
Space O(N) space complexity for sort,

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats.
Each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time.
Return the minimum number of boats to carry every given person.
keys: sort the array and use two pointers algorithm
"""
from typing import List


class Solution:
    def num_rescue_boats(self, people: List[int], limit: int) -> int:
        i = boats = 0
        j = len(people) - 1
        people.sort()
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats


if __name__ == "__main__":
    so = Solution()
    arr = [3, 5, 3, 4]
    l = 5
    print(so.num_rescue_boats(arr, l))
