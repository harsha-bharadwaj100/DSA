from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
                if board[j][i].isnumeric():
                    if board[j][i] in col:
                        return False
                    else:
                        col.add(board[j][i])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = set()
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l].isnumeric():
                            if board[i + k][j + l] in square:
                                return False
                            else:
                                square.add(board[i + k][j + l])
        return True


sol = Solution()
print(
    sol.isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
