class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        N = len(s)
        if k > N:
            return 0
        res = 0
        for i in range(N - k + 1):
            ss = s[i : i + k]
            if len(set(ss)) == k:
                res += 1

        return res

    def numKLenSubstrNoRepeatsA(self, s: str, k: int) -> int:
        return sum(1 for i in range(len(s) - k + 1) if len(set(s[i : i + k])) == k)
