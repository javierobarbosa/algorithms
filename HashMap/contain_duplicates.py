"""
Approach 1: sorted the array and look for previous is equal to the arr[i] --> Time O(N Log(N))
Approach 2: using set() and compare with len of the array --> Time O(N) Space O(N)
Approach 3: using dict - hash map --> Time O(N) Space O(N)

-- To use as interview

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for value in nums:
            if value in hash_map:
                return True
            hash_map[value] = True
        return True


if __name__ == "__main__":
    so = Solution()
    n = [3, 2, 4, 4]
    print(so.contains_duplicate(n))
