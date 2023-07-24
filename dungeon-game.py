from common import *


class SolutionA:
    def calculateMinimumHP(self, dungeon):
        N = len(dungeon)
        M = len(dungeon[0])

        @cache
        def dfs(i, j):
            nonlocal dungeon, N, M
            if i == N - 1 and j == M - 1:
                return max(1 - dungeon[i][j], 1)
            if i == N - 1:
                return max(dfs(i, j + 1) - dungeon[i][j], 1)
            if j == M - 1:
                return max(dfs(i + 1, j) - dungeon[i][j], 1)
            return max(
                min(dfs(i + 1, j), dfs(i, j + 1)) - dungeon[i][j],
                1,
            )

        return dfs(dungeon, N, M, 0, 0)


class SlutionB:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int | float:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[inf] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]
