"""
Note: reversed() or sum() Time Complexity O(N) sorted() Time Complexity O(N log(N))

Time Complexity O(N) Space O(N)
Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry == 1:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(result))


if __name__ == "__main__":
    so = Solution()
    s = "1010"
    t = "1011"
    print(so.addBinary(s, t))
