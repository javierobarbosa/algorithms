"""
Time O(log(N)) Space(1)
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        while x:
            result = result * 10 + x % 10
            x = x // 10
        if result > pow(2, 31):
            return 0
        return result * symbol


if __name__ == "__main__":
    so = Solution()
    n = -123
    print(so.reverse(n))