from common import *


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        water, land, area = 0, 1, 0

        def dfs(i, j, areacounter=False):
            nonlocal area, grid
            if i < 0 or j < 0 or i >= N or j >= M or grid[i][j] == water:
                return
            grid[i][j] = water
            if areacounter:
                area += 1
            for y_move, x_move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if areacounter:
                    dfs(i + y_move, j + x_move, True)
                else:
                    dfs(i + y_move, j + x_move)

        for i in range(N):
            dfs(i, 0)
            dfs(i, M - 1)

        for i in range(M):
            dfs(0, i)
            dfs(N - 1, i)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == land:
                    dfs(i, j, True)

        return area


class SolutionB:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        water, land, area = 0, 1, 0

        def dfs(i, j):
            nonlocal grid
            if i < 0 or j < 0 or i >= N or j >= M or grid[i][j] == water:
                return 0
            _area = 1
            grid[i][j] = water
            for y_move, x_move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                _area += dfs(i + y_move, j + x_move)
            return _area

        for i in range(N):
            dfs(i, 0)
            dfs(i, M - 1)

        for i in range(M):
            dfs(0, i)
            dfs(N - 1, i)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == land:
                    area += dfs(i, j)

        return area
