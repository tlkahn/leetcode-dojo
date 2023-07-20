from common import *


class SolutionA:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones)
        stone_map = {stone: index for index, stone in enumerate(stones)}
        speeds = [-1, 0, 1]

        @cache
        def dfs(u: int, k: int) -> bool:
            nonlocal N, stone_map, stones, speeds
            if u == N - 1:
                return True

            for i in speeds:
                if (
                    k + i > 0
                    and (next_stone := stones[u] + k + i) in stone_map
                    and dfs(stone_map[next_stone], k + i)
                ):
                    return True

            return False

        return False if 1 not in stone_map else dfs(1, 1)


class SolutionB:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if stones[1] != 1:
            return False

        f = [[False] * n for _ in range(n)]
        f[1][1] = True

        for i in range(2, n):
            for j in range(1, i):
                if (k := stones[i] - stones[j]) <= j + 1:
                    f[i][k] = f[j][k - 1] or f[j][k] or f[j][k + 1]

        return any(f[n - 1])
