# Given an array of integers nums and an integer target,
# Return indices of the two numbers such that they add up to target.
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in seen:
                return [seen[num2], idx]
            else:
                seen[num1] = idx


if __name__ == "__main__":
    so = Solution()
    n = [3, 2, 4]
    t = 6
    print(so.two_sum(n, t))