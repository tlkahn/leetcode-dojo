from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be obtained from buying
        and selling stocks.

        More similar questions:

        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/bao-li-mei-ju-dong-tai-gui-hua-chai-fen-si-xiang-b/
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/dong-tai-gui-hua-by-liweiwei1419-7/
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/dong-tai-gui-hua-by-liweiwei1419-4/
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/dong-tai-gui-hua-by-liweiwei1419-5/
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
        - https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/dong-tai-gui-hua-by-liweiwei1419-6/

        Args:
            prices (List[int]): A list of stock prices.

        Returns:
            int: The maximum profit that can be obtained.

        Example:
            Input: prices = [7,1,5,3,6,4]
            Output: 5
            Explanation: Buy on day 2 (price = 1) and sell on day 5
            (price = 6), profit = 6-1 = 5.
        """
        N = len(prices)

        if N == 1:
            return 0

        res = float("-inf")
        for i in range(N - 1):
            local_profit = max(prices[i + 1 :]) - prices[i]
            if local_profit > res:
                res = local_profit

        return int(res) if res > 0 else 0

    def maxProfit1A(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        return (
            max(max(prices[i + 1 :]) - prices[i] for i in range(len(prices) - 1)) or 0
        )

    def maxProfitB(self, prices: List[int]) -> int:
        N = len(prices)

        if N == 1:
            return 0

        res = float("-inf")
        for i in range(N - 1):
            local_profit = max(prices[i + 1 :]) - prices[i]
            if local_profit > res:
                res = local_profit

        return int(res) if res > 0 else 0

    def maxProfitC(self, prices):
        # not working
        N = len(prices)

        if N == 1:
            return 0

        dp = [[0] * 2 for _ in range(N)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        return dp[N][0]

    def maxProfitD(self, prices: List[int]) -> int:
        # kadane algorithm
        cash, hold = 0, float("-inf")

        for price in prices:
            cash = max(cash, hold + price)
            hold = max(hold, -price)

        return int(cash)

    def maxProfitE(self, prices: List[int]) -> int:
        length = len(prices)
        # Special case handling: if there are less than 2 elements, profit is 0
        if length < 2:
            return 0

        dp = [[0] * 2 for _ in range(length)]

        # dp[i][0] represents the cash amount when not holding stock at the end of day i
        # dp[i][1] represents the cash amount when holding stock at the end of day i

        # Initialization: cash amount when not holding stock is 0, when holding stock subtract the price of day 1 (index 0)
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # Start iterating from day 2
        for i in range(1, length):
            # Update the cash amount when not holding stock by taking the maximum of the previous day's cash amount when not holding stock
            # and the previous day's cash amount when holding stock plus the price of the current day
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # Update the cash amount when holding stock by taking the maximum of the previous day's cash amount when holding stock
            # and the negative price of the current day (buying the stock on this day)
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        # Return the cash amount when not holding stock at the end of the last day
        return dp[length - 1][0]

    def maxProfitF(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        cash_not_holding_stock = 0
        cash_holding_stock = -prices[0]

        for price in prices[1:]:
            cash_not_holding_stock = max(
                cash_not_holding_stock, cash_holding_stock + price
            )
            cash_holding_stock = max(cash_holding_stock, -price)

        return cash_not_holding_stock
