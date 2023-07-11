class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        NS = len(s)
        NT = len(t)

        def replaceable(s, t) -> bool:
            if s == t:
                return False
            cnt = 0
            for i in range(NS):
                if s[i] != t[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return True

        def deletable(s, t) -> bool:
            if len(s) - len(t) != 1:
                return False

            for i in range(len(t)):
                if s[i] != t[i]:
                    return s[i + 1 :] == t[i:]

            return True

        if NS == NT:
            return replaceable(s, t)

        if NS > NT:
            return deletable(s, t)

        if NT < NS:
            return deletable(t, s)
