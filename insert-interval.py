from common import *

from bisect import bisect_left


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Not working for some cases
        """
        if not intervals:
            return [newInterval]

        N = len(intervals)

        new_start, new_end = newInterval
        starts, ends = zip(*intervals)
        loc = bisect_left(starts, new_start)

        if N == 1:
            itv = intervals[0]
            left, right = sorted([newInterval, itv])
            if left[0] <= right[0] <= left[1]:
                return [[left[0], max(left[1], right[1])]]
            else:
                return [left, right]

        # case 1:
        if new_end <= ends[loc - 1]:
            pass

        # case 2:
        elif ends[loc - 1] < new_end < starts[loc]:
            intervals[loc - 1][1] = new_end

        # case 3:
        elif starts[loc] <= new_end <= ends[loc]:
            intervals[loc - 1][1] = ends[loc]
            intervals.pop(loc)

        else:
            # case 4:
            for i in range(loc, N):
                if ends[i] > new_end:
                    if starts[i] > new_end:
                        intervals[loc - 1][1] = new_end
                        intervals = intervals[:loc] + intervals[i:]
                    else:
                        intervals[loc - 1][1] = ends[i]
                        intervals = intervals[:loc] + intervals[i + 1 :]
                    return intervals

            # case 5:
            intervals[loc - 1][1] = new_end
            intervals = intervals[:loc]

        return intervals


class SolutionB:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        new_start, new_end = newInterval
        starts, ends = zip(*intervals)
        loc = bisect_left(starts, new_start)

        # case 1, 2, 3:
        if loc > 0 and ends[loc - 1] >= new_start:
            loc -= 1
            intervals[loc][1] = max(new_end, ends[loc])
        else:
            intervals.insert(loc, newInterval)

        # case 4, 5:
        while loc + 1 < len(intervals):
            if intervals[loc + 1][0] <= intervals[loc][1]:
                intervals[loc][1] = max(intervals[loc][1], intervals[loc + 1][1])
                intervals.pop(loc + 1)
            else:
                break

        return intervals
