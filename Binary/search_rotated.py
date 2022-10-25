# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, mid, high = 0, 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == "__main__":
    so = Solution()
    arr = [4, 5, 6, 7, 0, 1, 2]
    n = 0
    print(so.search(arr, n))
