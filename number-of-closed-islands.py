from common import *


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        N = len(grid)
        M = len(grid[0])
        land = 0
        water = 1

        def dfs(i, j):
            if i < 0 or j < 0 or i >= N or j >= M or grid[i][j] == water:
                return
            grid[i][j] = water
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        for i in range(M):
            dfs(0, i)
            dfs(N - 1, i)

        for i in range(N):
            dfs(i, 0)
            dfs(i, M - 1)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == land:
                    dfs(i, j)
                    res += 1

        return res
