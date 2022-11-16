"""
Time complexity is O(n), Memory complexity is O(n)

Given a string s of '(' , ')' and lowercase English characters. Remove the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""


class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:
        stack = []
        str_list = list(s)
        for idx in range(len(str_list)):
            if str_list[idx] == '(':
                stack.append(idx)
            elif str_list[idx] == ')':
                if stack:
                    stack.pop()
                else:
                    str_list[idx] = ""
        for idx in stack:
            str_list[idx] = ""
        return "".join(str_list)


if __name__ == "__main__":
    so = Solution()
    s = "lee(t(c)o)de)"
    print(so.min_remove_to_make_valid(s))