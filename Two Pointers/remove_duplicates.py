"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that
each unique element appears at most twice. The relative order of the elements should be kept the same.

Time Complexity = O(n), Space complexity = O(1)
"""
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        slow = 0
        visited = {}
        for fast in nums:
            visited[fast] = visited.get(fast, 0) + 1
            if visited[fast] <= 2:
                nums[slow] = fast
                slow += 1
        return slow

    def remove_duplicates_2(self, nums: List[int]) -> int:
        slow = 0
        for fast in nums:
            if slow < 2 or fast > nums[slow-2]:
                nums[slow] = fast
                slow += 1
        return slow


if __name__ == "__main__":
    so = Solution()
    arr = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    # print(so.remove_duplicates(arr))
    print(so.remove_duplicates_2(arr))