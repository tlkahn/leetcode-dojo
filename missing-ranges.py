from typing import List


class Solution:
    def findMissingRangesA(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        N = len(nums)
        itvs = []
        if nums[0] > lower:
            itvs.append([lower, nums[0] - 1])
        for i in range(N - 1):
            itvs.append([nums[i] + 1, nums[i + 1] - 1])
        if nums[-1] < upper:
            itvs.append([nums[-1] + 1, upper])

        return [itv for itv in itvs if itv[1] >= itv[0]]
