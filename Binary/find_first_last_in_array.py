"""
Time O(Log(N)) Space O(1)
Given an array of nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
"""
from typing import List


class SolutionV1:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search_left(nums, target)
        right = self.binary_search_right(nums, target)
        return [left, right]

    def binary_search_left(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid > 0 and nums[mid-1] < target or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def binary_search_right(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid+1] > target or mid == len(nums) - 1:
                    return mid
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1


class SolutionV2:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        # function to get the lowest index based on target
        def binary_search(target: int) -> int:
            start, end = 0, len(nums)
            while start < end:
                mid = (start + end) // 2
                if nums[mid] >= target:
                    end = mid
                else:
                    start = mid + 1
            return start

        left = binary_search(target)
        right = binary_search(target+1) - 1
        if left <= right:
            return [left, right]
        return [-1, -1]


if __name__ == "__main__":
    so1 = SolutionV1()
    so2 = SolutionV1()
    arr = [5, 7, 7, 8, 8, 10]
    t = 8
    print(so1.search_range(arr, t))
    print(so2.search_range(arr, t))

    #print(so.search_range_v2(arr, t))
