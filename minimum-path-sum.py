from common import *


class SolutionA:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += (
                    min(grid[i - 1][j], grid[i][j - 1])
                    if i > 0 and j > 0
                    else (grid[i - 1][j] if i > 0 else grid[i][j - 1])
                )
        return grid[-1][-1]


class SolutionB:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[1][1] = grid[0][0]
                else:
                    dp[i][j] = grid[i - 1][j - 1] + min(dp[i][j - 1], dp[i - 1][j])

        return int(dp[-1][-1])


class SolutionC:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = dp[1][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]
