class Solution:
    def canAttendMeetingsA(self, intervals: List[List[int]]) -> bool:
        N = len(intervals)
        if N < 2:
            return True

        itvs = sorted(intervals, key=lambda itv: itv[0])
        for i in range(1, N):
            if itvs[i][0] < itvs[i - 1][1]:
                return False

        return True

    def canAttendMeetingsB(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda itv: itv[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
