from typing import List, Annotated, Optional
from bisect import bisect_left, bisect_right


class SolutionA:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        left = toBeRemoved[0]
        right = toBeRemoved[1]
        N = len(intervals)

        def nearestleft(intervals, target):
            lefts = [left for left, _ in intervals]
            i = bisect_left(lefts, target)
            return intervals[i - 1] if i else []

        def nearestright(intervals, target):
            rights = [right for _, right in intervals]
            i = bisect_right(rights, target)
            return intervals[i] if i < N else []

        def overlapleft(nl, tbr):
            if not nl:
                return []
            ans = []
            if nl[1] < tbr[0]:
                return [nl]
            if nl[1] > tbr[1]:
                ans = [[nl[0], tbr[0]], [tbr[1], nl[1]]]
            else:
                ans = [[nl[0], tbr[0]]]
            return [a for a in ans if a[0] != a[1]]

        def overlapright(nr, tbr):
            if not nr:
                return []
            ans = []
            if nr[0] > tbr[1]:
                return [nr]
            if nr[0] < tbr[0]:
                ans = [[tbr[1], nr[1]], [nr[0], tbr[0]]]
            else:
                ans = [[tbr[1], nr[1]]]
            return [a for a in ans if a[0] != a[1]]

        intervals.sort()
        nl = nearestleft(intervals, left)
        nr = nearestright(intervals, right)
        leftoverlap = overlapleft(nl, toBeRemoved)
        rightoverlap = overlapright(nr, toBeRemoved)
        if nl and nr:
            lrs = [itv for itv in intervals if itv < nl or itv[0] > nr[0]]
        elif nl:
            lrs = [itv for itv in intervals if itv < nl]
        elif nr:
            lrs = [itv for itv in intervals if itv[0] > nr[0]]
        else:
            lrs = []
        ans = lrs + leftoverlap + rightoverlap
        return sorted(list(set(tuple(sorted(a)) for a in ans)))


class SolutionB:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        left, right = toBeRemoved
        result = []

        for interval in intervals:
            if interval[1] <= left or interval[0] >= right:
                result.append(interval)
            elif interval[0] < left and interval[1] > right:
                result.append([interval[0], left])
                result.append([right, interval[1]])
            elif interval[0] < left:
                result.append([interval[0], left])
            elif interval[1] > right:
                result.append([right, interval[1]])

        return result
