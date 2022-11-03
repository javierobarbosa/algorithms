# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def get_length_longest_substring_1(self, s: str) -> int:
        max_substring = start = 0
        duplicates = {}
        for i in range(len(s)):
            if s[i] in duplicates:
                if start <= duplicates[s[i]]:
                    start = duplicates[s[i]] + 1
                else:
                    max_substring = max(max_substring, i - start + 1)
            else:
                max_substring = max(max_substring, i - start + 1)
            duplicates[s[i]] = i
        return max_substring

    def get_length_longest_substring_2(self, s: str) -> int:
        start = max_substring = 0
        duplicates = {}
        for i in range(len(s)):
            if s[i] in duplicates and start <= duplicates[s[i]]:
                start = duplicates[s[i]] + 1
            else:
                max_substring = max(max_substring, i - start + 1)
            duplicates[s[i]] = i
        return max_substring


if __name__ == "__main__":
    so = Solution()
    s = "pwwkew"
    print(so.get_length_longest_substring_2(s))

