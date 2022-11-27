"""
Time - O(N) Space - O(1)
n1 ^ n2 = 0 if n1 == n2
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor


if __name__ == "__main__":
    so = Solution()
    arr = [4, 1, 2, 1, 2]
    print(so.single_number(arr))
