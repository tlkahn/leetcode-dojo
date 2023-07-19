from common import *


class SolutionA:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def insertlex(ps: list[list[int]], n: int) -> list[list[int]]:
            res: list[list[int]] = []
            for p in ps:
                for i in range(len(p)):
                    _p = p.copy()
                    _p.insert(i, n)
                    res.append(_p)
                p.append(n)
                res.append(p)
            return res

        curr = [[]]
        for i in range(len(nums)):
            curr = insertlex(curr, nums[i])

        return curr


class SolutionB:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def insertlex(ps: List[List[int]], n: int) -> List[List[int]]:
            res = []
            for p in ps:
                res.extend([p[:i] + [n] + p[i:] for i in range(len(p) + 1)])
            return res

        curr = [[]]
        for num in nums:
            curr = insertlex(curr, num)

        return curr
