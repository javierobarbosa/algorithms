"""
Two Pointers: Time Complexity = O(n), Space complexity = O(1)
Given a 0-indexed array nums of size n consisting of non-negative integers.
Apply n - 1 operations to this array (0-indexed):
If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.
"""

from typing import List


class Solution:
    def apply_operations(self, nums: List[int]) -> List[int]:
        end = len(nums)
        slow = 0
        for i in range(end):
            if i < end - 1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        for fast in range(end):
            if nums[fast] != 0:
                if fast != slow:
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        return nums

    def apply_operations_2(self, nums: List[int]) -> List[int]:
        end = len(nums)
        j = 0
        for i in range(end):
            if i < end - 1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


if __name__ == "__main__":
    so = Solution()
    arr = [1, 2, 2, 1, 1, 0]
    print(so.apply_operations_2(arr))
    # output:: [1, 4, 2, 0, 0, 0]


