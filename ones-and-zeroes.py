from common import *


class SolutionA:
    def findMaxForm(self, strs, m, n):
        def countZeroAndOne(string):
            cnt = [0, 0]
            for c in string:
                cnt[int(c)] += 1
            return cnt

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]

        for i in range(1, len(strs) + 1):
            count = countZeroAndOne(strs[i - 1])
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    zeros = count[0]
                    ones = count[1]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(
                            dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1
                        )

        return dp[len(strs)][m][n]


class SolutionB:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        ans = 0

        def digits(s: str) -> tuple[int, int]:
            if not s:
                return 0, 0

            ones = sum(1 for es in list(s) if es == "1")
            zeros = len(s) - ones
            return (ones, zeros)

        @cache
        def dfs(i):
            nonlocal m, n, strs, ans
            if not i:
                return 0, 0
            s = strs[i]
            ones, zeros = digits(s)
            d = dfs(i - 1)
            new_ones = d[0] + ones
            new_zeros = d[1] + zeros
            if new_ones <= n and new_zeros <= m:
                ans += 1
                return new_ones, new_zeros
            return ones, zeros

        dfs(N - 1)
        return ans
