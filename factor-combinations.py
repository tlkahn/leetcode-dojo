from typing import List


class Solution:
    def getFactorsA(self, n: int) -> List[List[int]]:
        return self.dfs(2, n)

    def dfs(self, start: int, num: int) -> List[List[int]]:
        if num == 1:
            return []

        qNum = int(num**0.5)
        result = []
        for mulNum in range(start, qNum + 1):
            if num % mulNum == 0:
                simpleList = [mulNum, num // mulNum]
                result.append(simpleList)
                nextLists = self.dfs(mulNum, num // mulNum)
                for lst in nextLists:
                    lst.append(mulNum)
                    result.append(lst)

        return result

    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(m, n):
            res = []
            for i in range(m, int(n**0.5) + 1):
                if n % i == 0:
                    res.append([i, n // i])
                    xs = dfs(i, n // i)
                    for x in xs:
                        res.append([i] + x)
            return res

        return dfs(2, n)
