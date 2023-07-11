class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Solution for:
        https://leetcode.cn/problems/interleaving-string/

        Check if s1 and s2 can be interleaved to form s3 using dynamic
        programming.

        Args:
            s1 (str): The first string.
            s2 (str): The second string.
            s3 (str): The target string to be formed from s1 and s2.

        Returns:
            bool: True if s1 and s2 can be interleaved to form s3,
            False otherwise.
        """
        m, n, l = len(s1), len(s2), len(s3)

        if m + n != l:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[m][n]
