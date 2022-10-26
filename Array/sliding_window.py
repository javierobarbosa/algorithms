#  O(N)
from typing import List


def fix_sliding_window(arr: List[int], k: int) -> List[int]:
    current_subarray = sum(arr[:k])
    result = [current_subarray]
    for i in range(1, len(arr)-k+1):
        current_subarray = current_subarray - arr[i-1]
        current_subarray = current_subarray + arr[i+1]
        result.append(current_subarray)
    return result


# min sub array greater than x
def dynamic_sliding_window(arr: List[int], x: int) -> List[int]:
    min_length = float('inf')
    start, end, current_sum = 0, 0, 0
    while end < len(arr):
        current_sum += arr[end]
        end += 1
        while start < end and current_sum >= x:
            current_sum -= arr[start]
            start += 1
            min_length = min(min_length, end-start+1)
    return min_length


# Maximum sum subarray of Size k
def get_max_sum(arr: List[int], k: int) -> int:
    max_sum, window_sum, start = 0, 0, 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if (i - start + 1) == k:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum


# Count Occurrences of Anagram
def count_anagram(text: str, word: str) -> int:
    word_heap, text_heap = 0 * 26, 0 * 26
    start, count = 0, 0
    for ch in word:
        word_heap[ord(ch) - ord('a')] += 1
    for i in range(len(word)):
        text_heap[ord(i) - ord('a')] += 1
        if (i -start + 1) == len(word):
            if text_heap == word_heap:
                count += 1
            text_heap[ord(i) - ord('a')] -= 1
            start += 1
    return count


# Difference between the maximum and minimum average of all k-length continuous subarrays
def get_min_max_diff(arr: list[int], k: int) -> int:
    current_sum = max_sum = start = 0
    min_sum = float('inf')
    for i in range(len(arr)):
        current_sum += arr[i]
        if (i - start + 1) == k:
            avg = current_sum / 2
            max_sum = max(max_sum, avg)
            min_sum = min(min_sum, avg)
            current_sum -= arr[start]
            start += 1
    return max_sum - min_sum


if __name__ == "__main__":
    arr = [3, 8, 9, 15]
    k = 2
    args = arr, k
    print(get_min_max_diff(*args))