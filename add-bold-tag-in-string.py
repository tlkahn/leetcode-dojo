from typing import List


class Limits:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class SolutionA:
    def get_next(self, s):
        next = [-1] * (len(s) + 1)
        j = 0
        k = -1
        while j < len(s):
            if k == -1 or s[j] == s[k]:
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]
        return next

    def index_kmp(self, s, t, begin, end, pos):
        next = self.get_next(t)
        i = pos
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j = next[j]
            if j < 0:
                i += 1
                j += 1
        if j == len(t):
            begin[0] = i - len(t)
            end[0] = i - 1
            return True
        return False

    def radix_sort(self, nums):
        count = [0] * 1000
        pos = [[] for _ in range(1000)]

        for num in nums:
            pos[num.left].append(num)
            count[num.left] += 1

        result = []
        for i in range(1000):
            for j in range(count[i]):
                result.append(pos[i][j])

        return result

    def merge_limits(self, bounds):
        bounds.sort(key=lambda x: x.left)
        merged = []
        i = 0
        while i < len(bounds):
            left = bounds[i].left
            right = bounds[i].right
            while i + 1 < len(bounds) and bounds[i + 1].left <= right + 1:
                right = max(right, bounds[i + 1].right)
                i += 1
            merged.append(Limits(left, right))
            i += 1
        return merged

    def add_bold_tag(self, s, dict):
        if not dict:
            return s
        bounds = []
        for word in dict:
            pos = 0
            while True:
                begin = [0]
                end = [0]
                if not self.index_kmp(s, word, begin, end, pos):
                    break
                bounds.append(Limits(begin[0], end[0]))
                pos = begin[0] + 1
                while pos < len(s) and s[pos] != s[begin[0]]:
                    pos += 1

        bounds = self.merge_limits(bounds)
        bounds.sort(key=lambda x: x.left)

        result = ""
        i = 0
        for j in range(len(s)):
            if i < len(bounds) and j == bounds[i].left:
                result += "<b>"
            result += s[j]
            if i < len(bounds) and j == bounds[i].right:
                result += "</b>"
                i += 1

        return result


class SolutionB:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        def merge(intervals: list[list[int]]):
            if len(intervals) < 2:
                return intervals

            intervals.sort()
            i = 1
            while i < len(intervals):
                if intervals[i][0] <= intervals[i - 1][1]:
                    if intervals[i][1] > intervals[i - 1][1]:
                        intervals[i - 1][1] = intervals[i][1]
                    intervals.pop(i)
                else:
                    i += 1

        def occurrences(pattern: str, s: str) -> list[list[int]]:
            N = len(pattern)
            M = len(s)
            ans = []
            for i in range(M - N + 1):
                if s[i : i + N] == pattern:
                    ans.append([i, i + N])
            return ans

        def highlight(s: str, intervals: list[list[int]], tag: list[str]) -> str:
            """
            Highligh the substring in intervals of s with tags
            """
            ans = ""
            j = 0
            starts = [itv[0] for itv in intervals]
            ends = [itv[1] for itv in intervals]
            while j < len(s):
                if j in starts:
                    ans += tag[0]
                if j in ends:
                    ans += tag[1]
                ans += s[j]
                j += 1
            if len(s) in ends:
                ans += tag[1]
            return ans

        intervals = []
        for word in words:
            intervals += occurrences(word, s)
            print(f"intervals: {intervals}")

        merge(intervals)
        print(f"merged intervals: {intervals}")
        return highlight(s, intervals, ["<b>", "</b>"])


class SolutionC:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        """
        This is pure art.
        """
        intervals = []
        for word in words:
            start = 0
            while start >= 0:
                start = s.find(word, start)
                if start >= 0:
                    intervals.append([start, start + len(word)])
                    start += 1

        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        result = ""
        i = 0
        for j in range(len(s)):
            if i < len(merged) and j == merged[i][0]:
                result += "<b>"
            result += s[j]
            if i < len(merged) and j == merged[i][1] - 1:
                result += "</b>"
                i += 1

        return result
