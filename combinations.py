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


import collections

from itertools import islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)
