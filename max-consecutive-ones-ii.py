from typing import List


class Solution:
    def findMaxConsecutiveOnesA(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            if nums[i - 1] == 1:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i - 1][0] + 1
            res = max(res, dp[i][0], dp[i][1])
        return res

    def findMaxConsecutiveOnesB(self, nums):
        res = 0
        prev_zeros = 0
        prev_ones = 0

        for num in nums:
            if num == 1:
                prev_zeros += 1
                prev_ones += 1
            else:
                prev_zeros = prev_ones + 1
                prev_ones = 0

            res = max(res, prev_zeros, prev_ones)

        return res


class SolutionB:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Not working yet.
        """
        N = len(nums)
        if N < 2:
            return N

        i, j = 0, 0
        k = 2
        ans = float("-inf")

        while i < N:
            ones = 0
            while j < N:
                if nums[j] == 0:
                    k -= 1
                    if not k:
                        break
                j += 1
                ones += 1
            ans = max(ans, ones)
            i = j + 1

        return int(ans)


class SolutionC:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Sliding window
        """
        res = 0
        count = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
                while count > 1:
                    count -= 1 if nums[l] == 0 else 0
                    l += 1
            res = max(res, r - l + 1)

        return res
