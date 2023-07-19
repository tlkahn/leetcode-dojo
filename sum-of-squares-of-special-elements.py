import math
from common import *


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        def get_factors(n: int) -> list[int]:
            factors = []
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    factors.extend([i, n // i]) if i != n // i else factors.append(i)
            return factors

        return sum(nums[f - 1] * nums[f - 1] for f in get_factors(len(nums)))
