from common import *


class SolutionA:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        prev = 0
        cur = nums[0]
        for num in range(2, N + 1):
            old_cur = cur
            cur = max(cur, prev + nums[num - 1])
            prev = old_cur
        return cur


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        fst = 0
        snd = nums[0]

        for i in range(2, n + 1):
            cur = max(snd, nums[i - 1] + fst)
            fst = snd
            snd = cur

        return snd

        # N = len(nums)
        # dp = [0] * (N + 1)
        # dp[1] = nums[0]

        # for i in range(2, N + 1):
        #     dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        # return dp[-1]

        # @cache
        # def dfs(n):
        #     if n == -1:
        #         return 0
        #     if n == 0:
        #         return nums[0]
        #     return max(dfs(n-1), nums[n] + dfs(n-2))

        # return dfs(len(nums) - 1)
