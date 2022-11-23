"""
**To ask in interviews**
Time O(N) Space O(N)
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


class Solution:
    def is_anagram_v1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def is_anagram_v2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_frequency = {}
        t_frequency = {}
        for i, j in zip(s, t):
            s_frequency[i] = s_frequency.get(i, 0) + 1
            t_frequency[j] = t_frequency.get(j, 0) + 1
        return t_frequency == s_frequency

    def is_anagram_v3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_frequency = [0] * 26
        t_frequency = [0] * 26
        for i, j in zip(s, t):
            s_frequency[ord(i) - ord('a')] += 1
            t_frequency[ord(j) - ord('a')] += 1
        return s_frequency == t_frequency

    def is_anagram_v4(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency = {}
        for i in s:
            frequency[i] = frequency.get(i, 0) + 1
        for j in t:
            frequency[j] = frequency.get(j, 0) - 1
            if frequency[j] < 0:
                return False
        return True


if __name__ == "__main__":
    so = Solution()
    s1 = "anagram"
    s2 = "nagaram"
    #print(so.is_anagram_v1(s1, s2))
    #print(so.is_anagram_v2(s1, s2))
    #print(so.is_anagram_v3(s1, s2))
    #print(so.is_anagram_v4(s1, s2))
