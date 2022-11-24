"""
Time N(M+N) Space(1)
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1.
nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        end = n + m - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1
            end -= 1
        print(nums1)


if __name__ == "__main__":
    so = Solution()
    arr1 = [1, 2, 3, 0, 0, 0]
    x = 3
    arr2 = [2, 5, 6]
    y = 3
    so.merge(arr1, x, arr2, y)
