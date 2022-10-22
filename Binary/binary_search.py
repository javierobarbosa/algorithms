# General binary search algorithm
from typing import List


def binary_search(nums: List[int], n: int) -> int:
    low, mid, high = 0, 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if n < nums[mid]:
            high = mid - 1
        elif n > nums[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    print(binary_search(arr, x))


