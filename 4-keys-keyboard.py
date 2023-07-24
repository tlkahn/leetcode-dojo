class Solution:
    def maxA(self, N: int) -> int:
        if N <= 5:
            return N
        arr = [0] * (N + 1)
        for i in range(1, N + 1):
            arr[i] = arr[i - 1] + 1
            for j in range(2, i):
                arr[i] = max(arr[i], arr[j] * (i - (j + 1)))
        return arr[N]


class SolutionB:
    def maxA(self, N: int) -> int:
        if N <= 5:
            return N

        dp = [i for i in range(N + 1)]

        for i in range(7, N + 1):
            dp[i] = max(dp[i - 4] * 3, dp[i - 5] * 4)

        return dp[N]
