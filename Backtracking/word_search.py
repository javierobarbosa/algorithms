"""
Backtracking Time O(N * M * 4^N), Space O(N * M * 4^N) --> two power N recursive stacks as is binary tree.
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        if not board:
            return False

        def backtracking(x: int, y: int, i: int) -> bool:
            if i == len(word):
                return True

            # return condition
            if (x < 0 or x >= rows or
                    y < 0 or y >= cols or
                    word[i] != board[x][y] or
                    (x, y) in visited):
                return False

            visited.add((x, y))
            for idx in range(4):
                if backtracking(x + dx[idx], y + dy[idx], i + 1):
                    return True
            visited.remove((x, y))
            return False

        for i in range(rows):
            for j in range(cols):
                if backtracking(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    so = Solution()
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    w = "ABCCED"
    print(so.exist(b, w))
