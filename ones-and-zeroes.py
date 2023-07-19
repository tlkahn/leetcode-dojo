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
