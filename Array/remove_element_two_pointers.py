# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# Time Complexity = O(n), Space complexity = O(1)
from typing import List


class Solution:
    def remove_element(self, nums: List[int], var: int) -> int:
        slow = 0
        for fast in nums:
            if fast != var:
                nums[slow] = fast
                slow += 1
        return slow


if __name__ == "__main__":
    so = Solution()
    # nums = [0, 1, 0, 3, 12]
    # nums = [0]
    arr = [0, 1, 2, 2, 3, 0, 4, 2]
    k = 2
    print(so.remove_element(arr, k))
