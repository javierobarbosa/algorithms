# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
from typing import List


class Solution:
    def find_min_v1(self, nums: List[int]) -> int:
        low, mid, high = 0, 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                high = mid - 1
            else:
                low = mid + 1
        return nums[0]


if __name__ == "__main__":
    so = Solution()
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(so.find_min_v1(arr))
