from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, 0
        res = []
        if m == 1:
            while c < n:
                res.append(matrix[r][c])
                c += 1
            return res
        if n == 1:
            while r < m:
                res.append(matrix[r][c])
                r += 1
            return res
        while c < n:
            res.append(matrix[r][c])
            c += 1
        r, c = 1, n - 1
        while r < m:
            res.append(matrix[r][c])
            r += 1
        r, c = m - 1, n - 2
        while c >= 0:
            res.append(matrix[r][c])
            c -= 1
        r, c = m - 2, 0
        while r >= 1:
            res.append(matrix[r][c])
            r -= 1
        inner_matrix = [row[1:-1] for row in matrix[1:-1]]
        return res + self.spiralOrder(inner_matrix)


sol = Solution()
print(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
