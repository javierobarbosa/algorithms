"""
O(1) space and O(n) time

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements of nums
except nums[i]. You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List


class Solution:
    def product_except_self_1(self, nums: List[int]) -> List[int]:
        right_product = [1]
        left_product = [1]
        for left in nums[:-1]:
            left_product.append(left_product[-1]*left)
        for right in reversed(nums[1:]):
            right_product.append(right_product[-1]*right)
        return [i*j for i, j in zip(left_product, reversed(right_product))]

    def product_except_self_2(self, nums: List[int]) -> List[int]:
        left_sum = right_sum = 1
        result = []
        for n in nums:
            result.append(left_sum)
            left_sum *= n
        for idx in reversed(range(len(nums))):
            result[idx] *= right_sum
            right_sum *= nums[idx]
        return result


if __name__ == "__main__":
    so = Solution()
    arr = [2, 3, 4, 5]
    print(so.product_except_self_1(arr))
    print(so.product_except_self_2(arr))


