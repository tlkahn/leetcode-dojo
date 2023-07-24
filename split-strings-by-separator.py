from common import *


class SolutionA:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for w in words:
            res += [w for w in w.split(separator) if w]  # separated words
        return res


class SolutionB:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [w for word in words for w in word.split(separator) if w]
