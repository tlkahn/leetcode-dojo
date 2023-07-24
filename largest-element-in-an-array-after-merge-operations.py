from common import *


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dfs(n: int):
            if n == 0:
                return nums[0]
            if nums[n - 1] > nums[n]:
                tmp = nums[n]
                nums.pop()
                return max(tmp, dfs(n - 1))
            nums[n - 1] += nums[n]
            nums.pop()
            return dfs(n - 1)

        return dfs(N - 1)
