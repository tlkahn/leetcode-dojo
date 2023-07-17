from common import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        prev = curr = [[]]

        # Solution 1:
        for i in range(N):
            curr = prev + [p + [nums[i]] for p in prev]
            prev = curr

        return prev

        # Solution 2:
        # dp = [[[]] for _ in range(N+1)]

        # for i in range(N):
        #     dp[i+1] = dp[i] + [d + [nums[i]] for d in dp[i]]

        # return dp[N]

        # Solution: 3
        # @cache
        # def dfs(i):
        #     if i == -1:
        #         return [[]]
        #     ds = dfs(i-1)
        #     return ds + [d + [nums[i]] for d in ds]

        # return dfs(N-1)
