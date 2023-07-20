class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            c = columnNumber % 26
            if c == 0:
                c = 26
                columnNumber -= 1
            res += chr(ord("A") + c - 1)
            columnNumber //= 26

        return res[::-1]
