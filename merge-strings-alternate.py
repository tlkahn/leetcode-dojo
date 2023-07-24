class SolutionA:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1), len(word2))
        res = ""
        for c1, c2 in zip(word1, word2):
            res += c1 + c2

        res += word1[minlen:] + word2[minlen:]
        return res


class SolutionB:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res += word1[i] + word2[i]

        res += word1[min_len:] + word2[min_len:]
        return res
