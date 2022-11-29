"""
Time O(N) Space O(N)
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
"""


class Solution:
    def count_binary_substrings(self, s: str) -> int:
        frequency = []
        count = 1
        substrings = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                frequency.append(count)
                count = 1
        frequency.append(count)
        for i in range(1, len(frequency)):
            substrings += min(frequency[i], frequency[i-1])
        return substrings


if __name__ == "__main__":
    so = Solution()
    t = "00110011"
    print(so.count_binary_substrings(t))