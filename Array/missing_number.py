"""
Time O(N) Space O(1)
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = 0
        for n in nums:
            actual_sum += n
        return expected_sum - actual_sum


if __name__ == "__main__":
    so = Solution()
    arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(so.missingNumber(arr))
