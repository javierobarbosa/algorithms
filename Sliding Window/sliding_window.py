#  O(N)
from typing import List


# Sum of k subset
def fix_sliding_window(arr: List[int], k: int) -> List[int]:
    current_subarray = sum(arr[:k])
    result = [current_subarray]
    for i in range(1, len(arr)-k+1):
        current_subarray -= arr[i-1]
        current_subarray += arr[i+1]
        result.append(current_subarray)
    return result


# min sub array greater than x
def dynamic_sliding_window(arr: List[int], k: int) -> List[int]:
    min_length = float('inf')
    start = end = current_sum = 0
    while end < len(arr):
        current_sum += arr[end]
        end += 1
        while start < end and current_sum >= k:
            current_sum -= arr[start]
            start += 1
            min_length = min(min_length, end-start+1)
    return min_length


# Maximum sum subarray of Size k
def get_max_sum(arr: List[int], k: int) -> int:
    max_sum = window_sum = start = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if (i - start + 1) == k:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum


# Count Occurrences of Anagram
def count_anagram(text: str, word: str) -> int:
    word_heap = text_heap = 0 * 26
    start = count = 0
    for ch in word:
        word_heap[ord(ch) - ord('a')] += 1
    for i in range(len(text)):
        text_heap[ord(text[i]) - ord('a')] += 1
        if (i - start + 1) == len(word):
            if text_heap == word_heap:
                count += 1
            text_heap[ord(text[i]) - ord('a')] -= 1
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


# Find the longest substring of a string containing ‘k’ distinct characters
def get_longest(s: str, k: int) -> str:
    high = low = 0
    start = end = 0
    windows = set()
    freq = [0] * 26

    while high < len(s):
        windows.add(s[high])
        freq[ord(s[high]) - ord('a')] += 1

        while len(windows) > k:
            freq[ord(s[low]) - ord('a')] -= 1
            # If char is out of the window sum, it should be removed from the set
            if freq[ord(s[low]) - ord('a')] == 0:
                windows.remove(s[low])
            low += 1

        # Update max substring if new max window length
        if end - start < high - low:
            start = low
            end = high
        high += 1
    return s[start:end + 1]


# Find duplicates within a range ‘k’ in an array
def get_duplicates(nums: List[int], k: int) -> bool:
    duplicates = {}
    for i in range(len(nums)):
        if nums[i] in duplicates and i - duplicates[nums[i]] <= k:
            return True
        else:
            duplicates[nums[i]] = i
    return False


if __name__ == "__main__":
    arr = [5, 6, 6, 8, 2, 4, 6, 9]
    k = 2
    s = 'abcbdbdbbdcdabd'
    args = arr, k
    print(get_duplicates(*args))