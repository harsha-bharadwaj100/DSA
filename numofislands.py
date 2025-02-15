from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= rows
                or j >= cols
                or grid[i][j] == "0"
                or (i, j) in visited
            ):
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1

        return islands


sol = Solution()
# print(
#     sol.numIslands(
#         [
#             ["1", "1", "1", "1", "0"],
#             ["1", "1", "0", "1", "0"],
#             ["1", "1", "0", "0", "0"],
#             ["0", "0", "0", "0", "0"],
#         ]
#     )
# )
print(
    sol.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
