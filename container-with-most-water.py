from common import *


class SolutionA:
    """
    Not working
    """

    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        i, j = 0, N - 1
        res = min(heights[i], heights[j]) * (j - i)
        while i < j:
            while heights[i] <= heights[j] and i < j:
                if heights[i + 1] <= heights[i]:
                    i += 1
                else:
                    if (newarea := heights[i + 1] * (j - i - 1)) > res:
                        res = newarea
                    else:
                        i += 1
            while heights[i] >= heights[j] and i < j:
                if heights[j - 1] <= heights[j]:
                    j -= 1
                else:
                    if (newarea := heights[j - 1] * (j - i - 1)) > res:
                        res = newarea
                    else:
                        j -= 1
        return res


class SolutionB:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        i, j = 0, N - 1
        res = 0

        while i < j:
            res = max(res, min(heights[i], heights[j]) * (j - i))

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return res
