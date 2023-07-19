from common import *


class SolutionA(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in xrange(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in xrange(1 << N)]
        parent = [[None] * N for _ in xrange(1 << N)]
        for mask in xrange(1, 1 << N):
            for bit in xrange(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0:
                        continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1 << N) - 1
        i = max(xrange(N), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            overlap = overlaps[perm[i - 1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)


class SolutionB:
    def shortestSuperstring(self, ws: List[str]) -> str:
        n, mask = len(ws), 1 << len(ws)
        g = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                a, b = ws[i], ws[j]
                l1, l2 = len(a), len(b)
                length = min(l1, l2)
                for k in range(length, 0, -1):
                    if a[l1 - k :] == b[:k]:
                        g[i][j] = k
                        break
        f = [[0 for _ in range(n)] for _ in range(mask)]
        p = [[0 for _ in range(n)] for _ in range(mask)]
        for s in range(mask):
            for i in range(n):
                if (s >> i) & 1 == 0:
                    continue
                for j in range(n):
                    if (s >> j) & 1 == 1:
                        continue
                    if f[s | (1 << j)][j] <= f[s][i] + g[i][j]:
                        f[s | (1 << j)][j] = f[s][i] + g[i][j]
                        p[s | (1 << j)][j] = i

        max_val = f[mask - 1][0]
        idx, last, status = 0, -1, mask - 1
        for i in range(1, n):
            if max_val < f[mask - 1][i]:
                max_val = f[mask - 1][i]
                idx = i
        ans = ""
        while status != 0:
            if last == -1:
                ans = ws[idx]
            else:
                ans = ws[idx][: len(ws[idx]) - g[idx][last]] + ans
            last = idx
            idx = p[status][idx]
            status ^= 1 << last
        return ans
