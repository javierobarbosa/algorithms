"""
- Hash Map with sorted --> Time O(N Log(N)) Space  O(N)
- Hash Map without sorted --> Time O(N * M) = O(N) Space  O(N)
Given an array of strings strs, group the anagrams together.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
"""

from typing import List
from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            pattern = "".join(sorted(word))
            if pattern not in hash_map:
                hash_map[pattern] = []
            hash_map[pattern].append(word)
        return list(hash_map.values())

    def group_anagrams_2(self, strs: List[str]) -> List[List[str]]:
        # ord returns the Unicode code for a character.
        hash_map = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char)-ord('a')] += 1
            hash_map[tuple(temp)].append(word)
        return list(hash_map.values())


if __name__ == "__main__":
    so = Solution()
    anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(so.group_anagrams_2(anagrams))
