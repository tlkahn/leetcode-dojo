class Solution:
    def lengthOfLongestSubstringTwoDistinctA(self, s: str) -> int:
        N = len(s)
        if N < 3:
            return N
        i, j = 0, 0
        res = ""
        new_begin = False
        while i < N:
            for j in range(i + 1, N + 1):
                curr = s[i]
                win = set(s[i:j])
                if len(win) > 2:
                    while s[i] == curr:
                        i += 1
                        new_begin = True
                    break
                else:
                    if j - i > len(res):
                        res = s[i:j]
            if not new_begin:
                i += 1
            new_begin = False

        return len(res)

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        N = len(s)
        if N < 3:
            return N
        i, j = 0, 0
        res = ""
        while i < N:
            j = i + 1
            while j < N + 1 and len(set(s[i:j])) <= 2:
                if j - i > len(res):
                    res = s[i:j]
                j += 1
            i += 1
        return len(res)
