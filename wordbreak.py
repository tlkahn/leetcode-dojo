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
