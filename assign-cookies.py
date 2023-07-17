class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(key=lambda i: -i)
        s.sort(key=lambda i: -i)
        ans = 0
        si = 0
        for gut in g:
            if si < len(s) and s[si] >= gut:
                ans += 1
                si += 1
        return ans
