from typing import List


class Solution:
    def maxProfitA(self, prices: List[int]) -> int:
        N = len(prices)

        if N < 2:
            return 0

        dp = [[0] * 2] * N
        dp[0][1] = -prices[0]

        for i in range(1, N):
            for _ in range(2):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit
