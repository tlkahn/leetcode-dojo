from common import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda itv: itv[0])
        if len(sorted_intervals) == 1:
            return sorted_intervals
        res = [sorted_intervals[0]]
        for i2 in sorted_intervals[1:]:
            i1 = res[-1]
            if i2[0] <= i1[1]:
                if i2[1] <= i1[1]:
                    pass
                else:
                    res[-1] = [i1[0], i2[1]]
            else:
                res.append(i2)
        return res


class SolutionB:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for start, end in intervals:
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res
