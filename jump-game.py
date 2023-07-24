from common import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 0:
            return False
        if N == 1:
            return True
        item_index = N - 2
        if nums[item_index] == 0:
            lst = [i + num >= N - 1 for i, num in enumerate(nums[:item_index])]
            return self.canJump(nums[:-1]) if any(lst) else False
        return self.canJump(nums[: N - 1])
