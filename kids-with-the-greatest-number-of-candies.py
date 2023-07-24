class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # sorted_candies_with_index
        sc = sorted(((c, i) for i, c in enumerate(candies)), reverse=True)
        # max candies
        mc = sc[0][0]
        res = []
        for candies, idx in sc:
            cando = True if candies + extraCandies >= mc else False
            res.append((cando, idx))

        res.sort(key=lambda cdi: cdi[1])
        return [r[0] for r in res]


class SolutionB:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [(c + extraCandies >= max_candies) for c in candies]
