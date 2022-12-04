"""
Backtracking - recursive, Time O(N * 2^N), Space O(N * 2^N) --> two power N recursive stacks as is binary tree.

Note:
    As subset is changing in each recursive call we need to keep the value static in result suing acopy
    In python list is passed by object reference. To copy a list use list(a) or a[:]. In both a new object is created.

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        start = 0
        result = []
        subset = []
        self.backtracking(nums, result, subset, start)
        return result

    def backtracking(self, nums: List[int], result: List[int], subset: List[int], start: int) -> None:
        # return condition
        if start > len(nums):
            return
        # collect subset, --> append a copy of subset in result
        result.append(list(subset))
        # for loop for branching depending on each element
        for i in range(start, len(nums)):
            # add unique element to the subset
            if nums[i] not in subset:
                subset.append(nums[i])
                self.backtracking(nums, result, subset, i)
                # remove element to the subset queue
                subset.pop()
        return


if __name__ == "__main__":
    so = Solution()
    n = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(so.subsets(n))
