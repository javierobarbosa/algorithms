"""
Given an array of integers, remove the zeros from it. Only O(1) of additional memory can be used.

Time Complexity O(N), Space O(1)
"""
from typing import List


class Solution:
    def remove_zeroes(self, array: List[int]) -> List[int]:
        end = len(array)
        j = 0
        for n in array:
            if n != 0:
                array[j] = n
                j += 1
        for i in range(j, len(array)):
            array.pop()
        return array


if __name__ == "__main__":
    so = Solution()
    a = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
    print(so.remove_zeroes(a))

