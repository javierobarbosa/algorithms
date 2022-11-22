"""
Time O(N), Space O(N)
GIven an array of integers representing asteroids in a row. For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
"""
from typing import List


class Solution:
    def asteroid_collision_1(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if n > 0:
                stack.append(n)
            else:
                while stack and stack[-1] > 0 and -n > stack[-1]:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(n)
                elif -n == stack[-1]:
                    stack.pop()
        return stack

    def asteroid_collision_2(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and stack[-1] > 0 and n < 0:
                collision = stack[-1] + n
                if collision <= 0:
                    stack.pop()
                elif collision >= 0:
                    break
            else:
                stack.append(n)
        return stack


if __name__ == "__main__":
    so = Solution()
    arr = [5, 10, -5]
    print(so.asteroid_collision_1(arr))
    print(so.asteroid_collision_2(arr))