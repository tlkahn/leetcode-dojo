from typing import List


class Solution:
    def reverseWordsA(self, s: List[str]) -> None:
        def reverse(s: list[str]):
            N = len(s)
            if N < 2:
                return

            left = 0
            right = N - 1

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        ss = "".join(s)
        words = ss.split(" ")
        reverse(words)
        res = []
        for w in words:
            res += list(w) + [" "]

    def reverseWords(self, s):
        s.reverse()  # Reverse the entire string
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[start:i] = s[start:i][::-1]  # Reverse each word
                start = i + 1
        s[start:] = s[start:][::-1]  # Reverse the last word
