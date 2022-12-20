"""
Given two lists return the elements that are in the first list, but are missing in the second.

Time Complexity O(N)
"""
from typing import List


class Solution:
    def get_list_difference(self, first_list: List[int], second_list: List[int]) -> List[int]:
        set_list = set(second_list)
        return [n for n in first_list if n not in set_list]

    # If we all elements of a list are unique we can use a set for both lists
    def get_list_difference_unique_items(self, first_list: List[int], second_list: List[int]) -> List[int]:
        set_list1 = set(first_list)
        set_list2 = set(second_list)
        return list(set_list1 - set_list2)


if __name__ == "__main__":
    so = Solution()
    l1 = [5, 10, -5, 10]
    l2 = [1, 45, -5]
    print(so.get_list_difference(l1, l2))
    print(so.get_list_difference_unique_items(l1, l2))
