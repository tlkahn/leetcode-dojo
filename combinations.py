def preamble():
    """
    # Table of Contents

    - **itertools.combinations(*iterable*, *r*):** Return *r* length
         subsequences of elements from the input *iterable*.

        The combination tuples are emitted in lexicographic ordering
        according to the order of the input *iterable*. So, if the input
        *iterable* is sorted, the output tuples will be produced in
        sorted order.

        Elements are treated as unique based on their position, not on
        their value. So if the input elements are unique, there will be
        no repeated values in each combination.

        Roughly equivalent to:

            def combinations(iterable, r):
                # combinations('ABCD', 2) --> AB AC AD BC BD CD
                # combinations(range(4), 3) --> 012 013 023 123
                pool = tuple(iterable)
                n = len(pool)
                if r > n:
                    return
                indices = list(range(r))
                yield tuple(pool[i] for i in indices)
                while True:
                    for i in reversed(range(r)):
                        if indices[i] != i + n - r:
                            break
                    else:
                        return
                    indices[i] += 1
                    for j in range(i+1, r):
                        indices[j] = indices[j-1] + 1
                    yield tuple(pool[i] for i in indices)

        The code for
        [`combinations()`](http://127.0.0.1:60483/Dash/yenlwfuv/doc/library/itertools.html#itertools.combinations)
        can be also expressed as a subsequence of
        [`permutations()`](http://127.0.0.1:60483/Dash/yenlwfuv/doc/library/itertools.html#itertools.permutations)
        after filtering entries where the elements are not in sorted
        order (according to their position in the input pool):

            def combinations(iterable, r):
                pool = tuple(iterable)
                n = len(pool)
                for indices in permutations(range(n), r):
                    if sorted(indices) == list(indices):
                        yield tuple(pool[i] for i in indices)

        The number of items returned is `n!=` `=/=` `=r!=` `=/=`
        `=(n-r)!` when `0=` `=<==` `=r=` `=<==` `=n` or zero when `r=`
        `=>=` `=n`.
    """
    pass


def mycombinations(iterable, r):
    """
    This code works as a way to find all combinations of size "r" in an
     iterable by utilizing a technique known as lexicographic ordering.
    Here's an elaboration of why this code works:
    1. The code starts by converting the iterable into a tuple called
    "pool" and determining the length of the pool.
    2. It checks if the desired combination size "r" is greater than the
    length of the pool. If so, it immediately returns, as there are no
    valid combinations to generate.
    3. It creates a list called "indices" containing the initial indices
    for the combination. These indices represent the positions of the
    elements in the pool that will be selected for each combination.
    4. It yields the first combination by selecting elements from the
    pool based on the initial indices.
    5. The code enters a loop that generates subsequent combinations:
       a. It iterates in reverse order through the indices.
       b. For each index, it checks if it can be incremented without
       exceeding the boundaries of the pool or violating the combination
       size.
       c. If an index can be incremented, it updates it and adjusts the
       following indices accordingly.
       d. It yields the new combination by selecting elements from the
       pool based on the updated indices.
    6. The loop continues until all combinations have been
    generated. The loop terminates when the indices cannot be further
    incremented without violating the combination size or exceeding the
    boundaries of the pool.
    7. Once the loop ends, the function returns, indicating that all
    combinations have been generated.
    By systematically incrementing and adjusting the indices, the code
    explores all possible combinations of elements from the given
    iterable. The lexicographic ordering ensures that all combinations
    are generated in a specific order, making it an efficient approach
    to finding all combinations of size "r" in an iterable.
    """
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
            yield tuple(pool[i] for i in indices)


print(list(mycombinations("ABCD", 2)))

from common import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, comb):
            nonlocal ans
            if len(comb) == K:
                ans.append(comb)
                return
            for j in range(i + 1, N):
                dfs(j, comb + [A[j]])

        N = n
        K = k
        A = range(1, n + 1)
        ans = []
        for i in range(n):
            dfs(i, [A[i]])
        return ans


class Solution:
    def combine(self, n, k):
        @cache
        def dfs(_n, _k):
            if _n == 0:
                return -inf
            if k == 0:
                return 1

            return dfs(_n, k - 1) + dfs(_n - 1, k)

        return dfs(n, k)


class SolutionA:
    def combine(self, n: int, k: int) -> List[List[int]]:
        @cache
        def dfs(_n, _k):
            if _n == 0:
                return []
            if _k == 0:
                return [[]]
            return [d + [_n] for d in dfs(_n, _k - 1) if _n not in d] + dfs(_n - 1, _k)

        return dfs(n, k)


class SolutionB:
    def combine(self, n: int, k: int) -> List[List[int]]:
        dp = [[[] for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(k + 1):
            dp[0][i] = []
        for i in range(n + 1):
            dp[i][0] = [[]]

        for _n in range(1, n + 1):
            for _k in range(1, k + 1):
                dp[_n][_k] = [d + [_n] for d in dp[_n][_k - 1] if _n not in d] + dp[
                    _n - 1
                ][_k]
        return dp[-1][-1]


class SolutionC:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k <= 0 or n < k:
            return res

        path = []
        self.dfs(n, k, 1, path, res)

        return res

    def dfs(self, n, k, begin, path, res):
        if len(path) == k:
            res.append(path[:])  # Add a copy of the current combination to the result
            return

        for i in range(begin, n + 1):
            path.append(i)  # Add a number to the path
            self.dfs(n, k, i + 1, path, res)  # Recursive call
            path.pop()  # Remove the last number added to the path (backtracking step)


class SolutionD:
    def combine(self, n: int, k: int) -> List[List[int]]:
        @cache
        def dfs(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n + 1):
                dfs(i + 1, path + (i,))

        res = []
        dfs(1, tuple())
        return [list(r) for r in res]
