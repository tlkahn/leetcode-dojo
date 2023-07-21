from common import *


class SolutionA:
    """
    DFS floodfill variant
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(_i, _j):
            nonlocal grid
            if _i < 0 or _j < 0 or _i >= m or _j >= n:
                return
            if grid[_i][_j] == 0:
                return
            grid[_i][_j] = 0
            dfs(_i + 1, _j)
            dfs(_i, _j + 1)
            dfs(_i - 1, _j)
            dfs(_i, _j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
                    dfs(i, j)

        return res


class SolutionA1:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0

        def dfs(i, j):
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            grid[i][j] = "#"
            for d in directions:
                dfs(i + d[0], j + d[1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count


class SolutionB:
    """
    Standard DFS
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * M for _ in range(N)]

        count = 0

        def dfs(i, j):
            visited[i][j] = True
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if (
                    0 <= new_i < N
                    and 0 <= new_j < M
                    and not visited[new_i][new_j]
                    and grid[new_i][new_j] == "1"
                ):
                    dfs(new_i, new_j)

        # Main
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
