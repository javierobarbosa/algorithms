"""
Time O(Log N), Space O(1)
Given a 0-indexed integer array nums, find a peak element (greater than its neighbors), and return its index.
If multiple peaks, return the index to any of the peaks.
An element is always considered to be strictly greater than a neighbor that is outside the array.

2   3   4 -> peak update start
4   3   2 <-- peak update end
"""
from typing import List


class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return 0
        if nums[start] > nums[start+1]:
            return start
        if nums[end] > nums[end-1]:
            return end
        while start <= end:
            mid = (start + end) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid - 1


if __name__ == "__main__":
    so = Solution()
    arr = [1, 2, 1, 3, 5, 6, 4]
    print(so.find_peak_element(arr))
