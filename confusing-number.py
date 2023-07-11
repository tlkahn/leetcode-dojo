class Solution:
    def confusingNumberA(self, n: int) -> bool:
        def topple(n):
            d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
            return int("".join([d[s] for s in str(n)[::-1]]))

        nset = set(str(n))
        if nset.issubset({"0", "1", "6", "8", "9"}):
            return topple(n) != n
        else:
            return False

    def confusingNumber(self, n: int) -> bool:
        d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        n_str = str(n)

        return any(ch not in d or d[ch] != n_str[-i - 1] for i, ch in enumerate(n_str))
