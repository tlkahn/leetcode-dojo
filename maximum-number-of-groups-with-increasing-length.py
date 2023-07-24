from common import *


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        if len(usageLimits) == 1:
            return 1
        uwi = sorted(
            [[usagelimit, idx] for idx, usagelimit in enumerate(usageLimits)],
            reverse=True,
        )  # usagelimits with index
        group_size = 1
        groups = []
        while group_size <= len(uwi):
            fii = uwi[:group_size]  # first i items
            items = [idx for usagelimit, idx in fii]
            if items not in groups:
                groups.append(items)
            for el in fii:
                if el[0] > 0:
                    el[0] -= 1
            uwi[:group_size] = sorted([[u, i] for u, i in fii if u > 0], reverse=True)
            group_size += 1

        return len(groups)


class SolutionB:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        if len(usageLimits) == 1:
            return 1

        uwi = sorted(
            [[idx, u] for idx, u in enumerate(usageLimits)],
            key=lambda x: x[1],
            reverse=True,
        )

        groups = []
        group_size = 1
        while group_size <= len(uwi):
            fii = [idx for idx, _ in uwi[:group_size]]

            if fii not in groups:
                groups.append(fii)

            for i in range(group_size):
                if uwi[i][1] > 0:
                    uwi[i][1] -= 1
            uwi = [
                [u, v]
                for u, v in sorted(uwi, key=lambda el: el[1], reverse=True)
                if v > 0
            ]
            group_size += 1

        return len(groups)
