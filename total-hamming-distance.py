from common import *


class SolutionA:
    def totalHammingDistance(self, nums: List[int]) -> int:
        def ones(x):
            x = x - ((x >> 1) & 0x55555555)
            x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
            x = (x + (x >> 4)) & 0x0F0F0F0F
            x = x + (x >> 8)
            x = x + (x >> 16)
            return x & 0x0000003F

        N = len(nums)
        ans = 0

        if N < 2:
            return 0

        for i in range(N - 1):
            for j in range(i + 1, N):
                ans += ones(nums[i] ^ nums[j])

        return ans


class SolutionB:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
