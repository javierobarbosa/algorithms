"""
Time O(N), Space O(N)
Key: Numbers ranging from [1, n] make the index as negative if duplicate (imaginary hash map)

Given an integer array nums of length N where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""
from typing import List


class Solution:
    def find_duplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                duplicates.append(abs(n))
            nums[idx] = -nums[idx]
        return duplicates

    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[(nums[i] % n) - 1] += n
        i = 0
        k = 1
        while i < len(nums):
            if nums[i] / n > 2:
                nums[i] = k
                i += 1
                k += 1
            else:
                nums.pop(i)
                k += 1
        return nums


if __name__ == "__main__":
    so = Solution()
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(so.find_duplicates(arr))
