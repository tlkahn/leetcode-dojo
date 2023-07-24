from common import *


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Fail some tests like:
        [0,0,1,0,1]
        1
        """

        def canplaceone(flowerbed) -> int:
            ones = [i for i, f in enumerate(flowerbed) if f == 1]
            dists = [(o2 - o1, o1 - 1) for o1, o2 in zip(ones, ones[1:])]
            for dist, start in dists:
                if dist > 3:
                    return start + 2
            return -1

        for _ in range(n):
            if (k := canplaceone(flowerbed)) == -1:
                return False
            flowerbed[k] = 1

        return True


class SolutionB:
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 1:
                i += 2
            elif i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                n -= 1
                i += 2
            else:
                i += 3
        return n <= 0


class SolutionC:
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        while i < len(flowerbed) and n > 0:
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                n -= 1
                i += 1
            i += 1
        return n <= 0
