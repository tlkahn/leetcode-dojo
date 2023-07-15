class SolutionA:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        # same_color` represents the number of ways to paint the
        # current fence with the same color as the previous
        # fence. `diff_color` represents the number of ways to paint
        # the current fence with a different color than the previous
        # fence.
        same_color = k
        diff_color = k * (k - 1)
        for _ in range(3, n + 1):
            same_color, diff_color = diff_color, (same_color + diff_color) * (k - 1)
        return same_color + diff_color


class SolutionB:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[1] = k
        if n > 1:
            dp[2] = k * k
        for i in range(3, n + 1):
            # For the i-th fence (given any color from k-1 options
            # different from the previous fence), we have two options:

            # 1. We can paint it with the same color as the (i-1)-th
            # fence, which has `dp[i-2]` ways to choose the color.

            # 2. We can paint it with a different color than the
            # (i-1)-th fence, which has`dp[i-1]` ways to choose the
            # color.

            # So, the total number of ways to paint the i-th fence is
            # the sum of these two options: `dp[i] = dp[i - 1] + dp[i
            # - 2]`.

            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
        return dp[n]
