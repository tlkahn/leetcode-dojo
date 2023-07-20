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
            zeros, ones = countZeroAndOne(strs[i - 1])
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(
                            dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1
                        )
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[len(strs)][m][n]


class SolutionB:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        def countZeroAndOne(s: str) -> list[int]:
            return [s.count("0"), s.count("1")]

        @cache
        def dfs(idx, m, n):
            if idx < 0 or m < 0 or n < 0:
                return 0
            zeros, ones = countZeroAndOne(strs[idx])
            if m >= zeros and n >= ones:
                return max(dfs(idx - 1, m, n), 1 + dfs(idx - 1, m - zeros, n - ones))
            return dfs(idx - 1, m, n)

        return dfs(len(strs) - 1, M, N)
