"""
Two Pointers + Hash Map
Time O(N), Space O(N) (worst: storing all elements in the map)
Given two strings s and t of lengths m and n respectively, return the minimum window substring
that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
"""


class Solution:
    def min_window(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        pattern_map = {}
        str_map = {}
        count = low = 0
        min_len = float('inf')
        start = -1
        for ch in t:
            pattern_map[ch] = pattern_map.get(ch, 0) + 1
        for high in range(len(s)):
            str_map[s[high]] = str_map.get(s[high], 0) + 1
            if str_map[s[high]] <= pattern_map.get(s[high], 0):
                count += 1
            if count == len(t):
                while str_map[s[low]] > pattern_map.get(s[low], 0):
                    str_map[s[low]] -= 1
                    low += 1
                if min_len > high - low + 1:
                    min_len =  high - low + 1
                    start = low
        if start == -1:
            return ""
        return s[low: low + min_len]


if __name__ == "__main__":
    so = Solution()
    s1 = "ADOBECODEBANC"
    s2 = "ABC"
    print(so.min_window(s1, s2))
