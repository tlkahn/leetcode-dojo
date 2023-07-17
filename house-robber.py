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
