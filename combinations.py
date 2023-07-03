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


def wordBreak(s, wordDict):
    """
    1. The function takes two parameters: "s" (the input string) and
    "wordDict" (a list of words).
    2. It creates a set called "wordSet" using the "wordDict" list for
    efficient word lookup.
    3. It initializes a list called "dp" of length "n+1" (where "n" is
    the length of the string) and fills it with False values. The "dp"
    list will track if a substring of "s" can be segmented into words
    from "wordDict".
    4. The first element of "dp", "dp[0]", is set to True to indicate
    that an empty string can be segmented.
    5. It starts a nested loop to iterate over the positions "i" in "s"
    from 1 to "n".
    6. Inside the nested loop, it iterates over the positions "j" from
    "i-1" down to 0, representing the potential starting position of a
    word.
    7. If "dp[i]" is already True (indicating that substring "s[0:i]"
    can be segmented), it breaks out of the inner loop since there is no
    need to check further.
    8. If "dp[j]" is False, it continues to the next iteration of the
    inner loop since the substring "s[j:i]" cannot be segmented.
    9. It extracts the substring "suffix" using "s[j:i]".
    10. If "suffix" is found in "wordSet" and "dp[j]" is True
    (indicating that substring "s[0:j]" can be segmented), it updates
    "dp[i]" to True and breaks out of the inner loop.
    11. After the nested loops complete, it returns "dp[n]", which
    represents whether the entire string "s" can be segmented into words
    from "wordDict".

    """
    wordSet = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if dp[i]:
                break
            if not dp[j]:
                continue
            suffix = s[j:i]
            if suffix in wordSet and dp[j]:
                dp[i] = True
                break

    return dp[n]


# // This function checks if a given string can be broken into words from a given word dictionary

# const wordBreak = (s, wordDict) => {
#   const len = s.length;
#   const wordSet = new Set(wordDict);
#   const memo = new Array(len); // memoization array to store previous results

#   const canBreak = (start) => {
#     if (start == len) return true; // base case: the string has been fully processed and can be broken
#     if (memo[start] !== undefined) return memo[start]; // if the result is already memoized, return it

#     // Iterate through all possible prefixes of the string
#     for (let i = start + 1; i <= len; i++) {
#       const prefix = s.slice(start, i);
#       if (wordSet.has(prefix) && canBreak(i)) { // if the current prefix is in the word dictionary and the remaining string can be broken, return true
#         memo[start] = true; // memoize the result for the current start index
#         return true;
#       }
#     }
#     memo[start] = false; // memoize the result as false for the current start index
#     return false;
#   };

#   return canBreak(0); // start the recursive function call from index 0
# };


# def wordBreak(s, wordDict):
#     memo = {}

#     def canBreak(start):
#         if start == len(s):
#             return True
#         if start in memo:
#             return memo[start]

#         for i in range(start + 1, len(s) + 1):
#             prefix = s[start:i]
#             if prefix in wordDict and canBreak(i):
#                 memo[start] = True
#                 return True

#         memo[start] = False
#         return False

#     return canBreak(0)

from collections import deque


def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    visited = [False] * len(s)

    queue = deque()
    queue.append(0)

    while queue:
        start = queue.popleft()  # Dequeue the pointer for examination
        if visited[start]:
            continue  # If already visited, skip

        visited[start] = True  # Mark the index as visited

        for i in range(
            start + 1, len(s) + 1
        ):  # Iterate to split the string into two parts using pointer i
            prefix = s[start:i]  # Extract the prefix part
            if prefix in wordSet:  # If the prefix part is a word
                if i < len(
                    s
                ):  # If i is within the bounds of the string, enqueue it as a node to be examined in the next level of BFS
                    queue.append(i)
                else:  # If i reaches the end of the string, it means the string has been split into words without any remaining substring, return True
                    return True

    return False  # If all nodes have been examined (all possible splits have been considered) and no True result has been returned, return False


def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    length = len(s)
    dp = [False] * (length + 1)
    dp[0] = True

    for i in range(1, length + 1):
        for j in range(i - 1, -1, -1):
            if dp[i]:
                break
            if not dp[j]:
                continue

            suffix = s[j:i]
            if suffix in wordSet and dp[j]:
                dp[i] = True
                break

    return dp[length]


class Trie:
    def __init__(self):
        self.isEnd = False
        self.next = [None] * 26

    def insert(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if not node.next[index]:
                node.next[index] = Trie()
            node = node.next[index]
        node.isEnd = True

    def search(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if not node.next[index]:
                return False
            node = node.next[index]
        return node.isEnd

    def startsWith(self, prefix):
        node = self
        for c in prefix:
            index = ord(c) - ord("a")
            if not node.next[index]:
                return False
            node = node.next[index]
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        count = 0

        def dfs(i, j):
            visited[i][j] = True

            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]

                if (
                    0 <= new_i < rows
                    and 0 <= new_j < cols
                    and grid[new_i][new_j] == "1"
                    and not visited[new_i][new_j]
                ):
                    dfs(new_i, new_j)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count


# M = 5
# N = 4
# visited1 = [[False] * M] * N
# visited2 = [[False] * M for _ in range(N)]
# visited1[0][0] = True
# visited2[0][0] = True

# print(visited1)
# print(visited2)
