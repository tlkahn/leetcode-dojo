from common import *


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key=lambda x: x[1])

        @cache
        def dfs(n: int):
            nonlocal intervals
            if n == 0:
                return 0
            if intervals[n - 1][1] > intervals[n][0]:
                intervals.pop(n)
                return dfs(n - 1) + 1
            return dfs(n - 1)

        return dfs(N - 1)


class SolutionB:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end, count = float("-inf"), 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                count += 1

        return count


class SolutionE:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = -inf
        res = 0
        for start, end in intervals:
            if start < prev_end:
                res += 1
            else:
                prev_end = end
        return res


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals based on their end times
        intervals.sort(key=lambda x: x[1])

        # Recursive helper function with memoization
        @lru_cache(None)
        def helper(index, prev_end):
            # If we've processed all intervals, return 0
            if index == len(intervals):
                return 0

            start, end = intervals[index]
            taken = not_taken = float("inf")

            # If the current interval doesn't overlap with previous, consider taking it
            if start >= prev_end:
                taken = helper(index + 1, end)

            # Consider not taking the current interval
            not_taken = helper(index + 1, prev_end)

            # Return the minimum of the two choices, adding 1 if we don't take the current interval
            return min(taken, not_taken + 1)

        # Start processing intervals from index 0 and initialize prev_end to negative infinity
        return helper(0, float("-inf"))
