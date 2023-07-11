from typing import List


class Solution:
    def maxProfit4(self, K: int, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # Adjust K if it's greater than half of the total days
        K = min(K, n // 2)

        # Create dp array
        dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(n)]

        # Initialize dp array for the first day
        for k in range(1, K + 1):
            dp[0][0][k] = 0  # Not holding stock
            dp[0][1][k] = -prices[0]  # Holding stock

        # Calculate the maximum profit for each day and transaction count
        for i in range(1, n):
            for k in range(1, K + 1):
                # When not holding stock on the current day, compare the maximum profit of
                # not holding stock on the previous day and holding stock on the previous day
                dp[i][0][k] = max(dp[i - 1][0][k], dp[i - 1][1][k] + prices[i])

                # When holding stock on the current day, compare the maximum profit of
                # holding stock on the previous day and not holding stock on the previous day (with k-1 transactions)
                dp[i][1][k] = max(dp[i - 1][1][k], dp[i - 1][0][k - 1] - prices[i])

        return dp[n - 1][0][
            K
        ]  # Return the maximum profit on the last day with K transactions
t-time-to-buy-and-sell-stock-ii.py
