class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += (
                    min(grid[i - 1][j], grid[i][j - 1])
                    if i > 0 and j > 0
                    else (grid[i - 1][j] if i > 0 else grid[i][j - 1])
                )
        return grid[-1][-1]
