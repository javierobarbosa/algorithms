# Two Pointers: Time Complexity = O(n), Space complexity = O(1)
from typing import List


class Solution:
    def remove_element(self, nums: List[int], var: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The relative order of the elements may be changed.
        """
        slow = 0
        for fast in nums:
            if fast != var:
                nums[slow] = fast
                slow += 1
        print(nums)
        return slow

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
        element appears only once. The relative order of the elements should be kept the same.
        """
        visited = set()
        slow = 0
        for fast in nums:
            if fast not in visited:
                visited.add(fast)
                nums[slow] = fast
                slow += 1
        print(nums)
        return slow


if __name__ == "__main__":
    so = Solution()
    # nums = [0, 1, 0, 3, 12]
    # nums = [0]
    arr_1 = [0, 1, 2, 2, 3, 0, 4, 2]
    k = 2
    # print(so.remove_element(arr_1, k))
    arr_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(so.remove_duplicates(arr_2))

