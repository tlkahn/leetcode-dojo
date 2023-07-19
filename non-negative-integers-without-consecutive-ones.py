from common import *


class Solution:
    N = 50

    f = [[0] * 2 for _ in range(N)]
    f[1][0] = 1
    f[1][1] = 2
    for i in range(1, N - 1):
        f[i + 1][0] = f[i][1]
        f[i + 1][1] = f[i][0] + f[i][1]

    def getLen(self, n):
        for i in range(31, -1, -1):
            if (n >> i) & 1 == 1:
                return i
        return 0

    def findIntegers(self, n):
        length = self.getLen(n)
        ans = 0
        prev = 0
        for i in range(length, -1, -1):
            cur = (n >> i) & 1
            if cur == 1:
                ans += self.f[i + 1][0]
            if prev == 1 and cur == 1:
                break
            prev = cur
            if i == 0:
                ans += 1
        return ans
