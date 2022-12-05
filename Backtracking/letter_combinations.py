"""
Iterative: Time O(N³), Space O(N³)
Recursive: Time O(N * 2^N), Space O(N * 2^N)

"""
from typing import List, Dict


class Solution:
    def letter_combinations_iterative(self, digits: str) -> List[str]:
        if not digits:
            return []
        lookup = {
            "2": "abc",
            "3": "dfe",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = [""]
        for d in digits:
            temp = []
            for v in lookup[d]:
                for r in result:
                    temp.append(r+v)
            result = temp
        return result

    def backtracking(self, digits: str, result: List[str], lookup: Dict, combinations: str, idx: int ):
        if idx > len(digits):
            return
        if len(combinations) == len(digits):
            # As combinations is string, copy using list() does not work use slicing instead -> [:]
            result.append(combinations[:])
            return
        current_digit = digits[idx]
        for s in lookup[current_digit]:
            self.backtracking(digits, result, lookup, combinations+s, idx+1)
        return

    def letter_combinations_backtracking(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        lookup = {
            "2": "abc",
            "3": "dfe",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.backtracking(digits, result, lookup, "", 0)
        return result


if __name__ == "__main__":
    so = Solution()
    nums = "23"
    # print(so.letter_combinations_iterative(nums))
    print(so.letter_combinations_backtracking(nums))
