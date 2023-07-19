from common import *


class SolutionA:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        splust = S + target
        if (splust) % 2:
            return 0
        nums.sort()
        A = splust // 2
        M = bisect_left(nums, A + 1)
        curr = [[]]
        for i in range(M):
            curr = curr + [d + [nums[i]] for d in curr if nums[i] <= A]
        return sum(1 for subset in curr if sum(subset) == A)


class SolutionB:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        sum_diff = S - target
        if sum_diff < 0 or sum_diff % 2 != 0:
            return 0
        A = sum_diff // 2
        dp = [0] * (A + 1)
        dp[0] = 1
        for num in nums:
            for j in range(A, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[A]
