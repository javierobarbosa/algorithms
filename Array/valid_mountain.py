"""
Time O(N) Space O(1)

Given an array of integers arr, return true if and only if it is a valid mountain array.
* arr.length >= 3
* arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
* arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""
from typing import List


class Solution:
    def valid_mountain_array(self, arr: List[int]) -> int:
        n = len(arr)
        i = 1
        if n < 3:
            return False
        while i < n and arr[i-1] < arr[i]:
            i += 1
        if i == 1 or i == n:
            return False
        while i < n and arr[i-1] > arr[i]:
            i += 1
        return i == n


if __name__ == "__main__":
    so = Solution()
    nums = [0, 3, 2, 1]
    print(so.valid_mountain_array(nums))