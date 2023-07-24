from common import *


class SolutionA:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]


class SolutionB:
    def minimumTotal(self, triangle: List[List[int]]) -> int | float:
        N = len(triangle)
        dp = [[inf] * (N + 1) for _ in range(N + 1)]
        dp[1][1] = triangle[0][0]
        for i in range(2, N + 1):
            for j in range(1, i + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i - 1][j - 1]

        return min(dp[N][i] for i in range(N + 1))

        # @cache
        # def dfs(n: int, idx: int) -> None:
        #     if n == 0 and idx == 0:
        #         return triangle[0][0]
        #     if idx < 0 or n < 0 or idx > n:
        #         return inf
        #     return min(dfs(n-1, idx), dfs(n-1, idx-1)) + triangle[n][idx]

        # return min(dfs(N-1, i) for i in range(N))
