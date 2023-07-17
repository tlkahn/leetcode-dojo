from common import *


class SolutionA:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N < 2:
            return 0
        K = 3

        dp = [[[0] * 2 for _ in range(K)] for _ in range(N)]
        dp[0][0][1] = -inf
        dp[0][1][1] = -prices[0]
        dp[0][2][1] = -prices[0]
        ans = -inf

        for i in range(1, N):
            for k in range(K):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                ans = max(ans, dp[i][k][0], dp[i][k][1])

        return ans


class SolutionB:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N < 2:
            return 0
        K = 3

        @cache
        def dfs(day, trades, hold):
            if day == 0:
                if not trades:
                    return -inf if hold else 0
                else:
                    return -prices[0] if hold else 0
            if not hold:
                return max(
                    dfs(day - 1, trades, hold), dfs(day - 1, trades, 1) + prices[day]
                )
            return max(
                dfs(day - 1, trades, hold), dfs(day - 1, trades - 1, 0) - prices[day]
            )

        return dfs(N - 1, K - 1, 0)
