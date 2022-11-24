"""
Time O(N), Space O(1)
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
"""
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - 1)
            max_area = max(max_area, area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area


if __name__ == "__main__":
    so = Solution()
    h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(so.max_area(h))
