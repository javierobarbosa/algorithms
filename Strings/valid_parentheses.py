"""
Time: O(N), Space O(N)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""


class Solution:
    def is_valid(self, s:str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif not stack or brackets[stack.pop()] != ch:
                return False
        return not stack


if __name__ == "__main__":
    so = Solution()
    string = "()[]{}"
    print(so.is_valid(string))