# Given a string s, find the length of the longest substring without repeating characters.
"""
pwwkew
  _
duplicates = {p:0, w:1}
"""


class Solution:
    def get_length_longest_substring_1(self, s: str) -> int:
        max_substring = start = 0
        duplicates = {}
        for end in range(len(s)):
            if s[end] in duplicates:
                # If char is already within the window, the update the window start pointer
                if start <= duplicates[s[end]]:
                    start = duplicates[s[end]] + 1
                # Char is out of the window, does not count as duplicated, just increment the count
                else:
                    max_substring = max(max_substring, end - start + 1)
                # to get the len of the substring adding +1 as end is initialized with 0 to count the item iterated
            else:
                max_substring = max(max_substring, end - start + 1)
            duplicates[s[end]] = end
        return max_substring

    def get_length_longest_substring_2(self, s: str) -> int:
        start = max_substring = 0
        duplicates = {}
        for end in range(len(s)):
            if s[end] in duplicates and start <= duplicates[s[end]]:
                start = duplicates[s[end]] + 1
            else:
                max_substring = max(max_substring, end - start + 1)
            duplicates[s[end]] = end
        return max_substring


if __name__ == "__main__":
    so = Solution()
    s = "pwwkew"
    print(so.get_length_longest_substring_2(s))

