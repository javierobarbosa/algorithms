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

    def remove_duplicates_2(self, nums: List[int]) -> int:
        # With no set
        slow = 1
        for fast in range(len(nums)-1):
            if nums[fast] != nums[fast+1]:
                nums[slow] = nums[fast+1]
                slow += 1
        print(nums)
        return slow


if __name__ == "__main__":
    so = Solution()
    # nums = [0, 1, 0, 3, 12]
    # nums = [0]
    arr_1 = [-1,0,0,0,0,3,3]
    k = 2
    # print(so.remove_element(arr_1, k))
    arr_2 = [-1,0,0,0,0,3,3]
    print(so.remove_duplicates(arr_1))
    # print(so.remove_duplicates_2(arr_2))

