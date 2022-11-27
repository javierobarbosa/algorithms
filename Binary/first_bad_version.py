"""
Time O(Log(N)) Space O(1)
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one.
You are given an API bool isBadVersion(version) which returns whether version is bad.
key1: while start < end (single element)
key2: update end, end = mid  (not 'end = mid-1') end = mid could be te first version of target
"""


class Solution:
    def __init__(self, bad):
        self.bad = bad

    def first_bad_version(self, target: int) -> int:
        start, end = 1, target
        while start < end:
            mid = (start + end) // 2
            if self.is_bad_version(mid):
                end = mid
            else:
                start = mid + 1
        return start

    def is_bad_version(self, target: int) -> bool:
        if target >= self.bad:
            return True
        return False


if __name__ == "__main__":
    n, bad = 5, 4
    so = Solution(bad)
    print(so.first_bad_version(n))