# Given an integer array nums, move all 0's to the end of it while maintaining the order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Time Complexity = O(n), Space complexity = O(1)
from typing import List


class Solution:
    def move_zeroes_1(self, nums: List[int]) -> List[int]:
        j = 0
        for n in nums:
            if n != 0:
                nums[j] = n
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums

    def move_zeroes_2(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


if __name__ == "__main__":
    so = Solution()
    # nums = [0, 1, 0, 3, 12]
    # nums = [0]
    nums = [1, 2, 3, 4, 5]
    print(so.move_zeroes_2(nums))
