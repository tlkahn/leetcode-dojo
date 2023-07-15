from functools import cache


class SolutionA:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Calculates the length of the longest palindromic subsequence in a given string.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest palindromic subsequence.

        """
        N = len(s)

        @cache
        def dfs(i, j):
            if j < i:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + dfs(i + 1, j - 1)
            else:
                return max(dfs(i, j - 1), dfs(i + 1, j))

        return dfs(0, N - 1)


class SolutionB:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][N - 1]
