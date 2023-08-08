"""
Time O(N Log(N)), Space O(N)
The merge_sort() function first concatenates the two input arrays. Then, it defines two nested functions:
merge() to merge two sorted arrays and sort() to perform the merge sort algorithm recursively.
"""
from typing import List


class Solution:
    def merge_sort(self, arr1: List[int], arr2: List[int]) -> List[int]:
        merged = arr1 + arr2

        def merge(left: List[int], right: List[int]) -> List[int]:
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            middle = len(arr) // 2
            left = arr[:middle]
            right = arr[middle:]
            return merge(sort(left), sort(right))

        sorted_array = sort(merged)
        return sorted_array


if __name__ == "__main__":
    so = Solution()
    arr1 = [4, 2, 8, 1, 6]
    arr2 = [5, 3, 7, 9]
    sorted_result = so.merge_sort(arr1, arr2)
    print(sorted_result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == sorted_result
