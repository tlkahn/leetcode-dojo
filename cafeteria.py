from typing import List

# Write any import statements here


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    intervals = [(s - K - 1, s + K + 1) for s in sorted(S)]
    candidates_ranges = [
        (i1[1], i2[0]) for i1, i2 in zip(intervals[:-1], intervals[1:])
    ]
    candidates_ranges = (
        [
            (1, intervals[0][0]),
        ]
        + candidates_ranges
        + [
            (intervals[-1][1], N),
        ]
    )
    available_ranges = list(filter(lambda t: t[0] <= t[1], candidates_ranges))
    slots = set()
    for r in available_ranges:
        slots |= set(range(r[0], r[1] + 1))
    res = 0
    while slots:
        print(f"slots: {slots}")
        s = slots.pop()
        res += 1
        for i in range(s - K, s + K + 1):
            if i in slots:
                slots.remove(i)
    return res


def test1():
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    print(getMaxAdditionalDinersCount(N, K, M, S))


def test2():
    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]
    print(getMaxAdditionalDinersCount(N, K, M, S))


tests = [test2]

for t in tests:
    t()


# https://leetcode.cn/problems/maximize-distance-to-closest-person
# /Users/toeinriver/Documents/org/clips/849-到最近的人的最大距离-力扣（Leetcode）.org
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seats_index = [i for i, s in enumerate(seats) if s == 1]
        start = -1
        end = len(seats)
        if start not in seats_index:
            seats_index.insert(0, -1)
        if end not in seats_index:
            seats_index.append(end)

        intervals = [
            (i, j) for i, j in zip(seats_index[:-1], seats_index[1:]) if j - i > 1
        ]
        maxi, maxj = max(intervals, key=lambda t: t[1] - t[0])
        mid = (maxj + maxi) // 2
        return max(mid - maxi, maxj - mid)
