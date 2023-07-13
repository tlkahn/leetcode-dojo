class Solution:
    def lengthOfLongestSubstringKDistinctA(self, s: str, k: int) -> int:
        # this fails the performance test
        N = len(s)
        if N <= k:
            return len(s)

        i, j = 0, 0
        res = 0
        while i < N:
            j = i + 1
            while len(set(s[i:j])) <= k and j < N + 1:
                if res < j - i:
                    res = j - i
                j += 1
            i += 1

        return res

    def lengthOfLongestSubstringKDistinctB(self, s: str, k: int) -> int:
        char_count = {}
        i, j = 0, 0
        max_length = 0

        while j < len(s):
            char_count[s[j]] = char_count.get(s[j], 0) + 1

            while len(char_count) > k:
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i += 1

            max_length = max(max_length, j - i + 1)
            j += 1

        return max_length

    def lengthOfLongestSubstringKDistinctC(self, s: str, k: int) -> int:
        char_count = {}
        i, max_length = 0, 0

        for j in range(len(s)):
            char_count[s[j]] = char_count.get(s[j], 0) + 1

            while len(char_count) > k:
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i += 1

            max_length = max(max_length, j - i + 1)

        return max_length

    def lengthOfLongestSubstringKDistinctD(self, s: str, k: int) -> int:
        """
        This code uses a sliding window approach to find the length of the
        longest substring with at most k distinct characters in a given
        string. It iterates over the string using pointers `i` and `j`, where
        `i` represents the start of the substring and `j` represents the end.

        The code maintains a dictionary `char_count` to keep track of the
        count of each character within the current window. Whenever the number
        of distinct characters exceeds `k`, the window is shrunk by moving `i`
        to the right and updating the character counts accordingly.

        The maximum length of the substring is continuously updated and
        returned at the end.
        """
        # Dictionary to keep track of character counts
        char_count = {}
        # Pointers for the sliding window
        i, max_length = 0, 0

        # Iterate over the string
        for j in range(len(s)):
            # Update the character count
            char_count[s[j]] = char_count.get(s[j], 0) + 1

            # Shrink the window if the distinct characters exceed k
            while len(char_count) > k:
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i += 1

            # Update the maximum length if necessary
            max_length = max(max_length, j - i + 1)

        # Return the maximum length of substring with at most k distinct characters
        return max_length

        def lengthOfLongestSubstringKDistinctE(self, s: str, k: int) -> int:
            N = len(s)
            if N <= k:
                return N

            i, maxlen = 0, 0
            char_count = {}
            for j in range(N):
                char_count[s[j]] = char_count.get(s[j], 0) + 1
                while len(char_count) > k:
                    char_count[s[i]] -= 1
                    if char_count[s[i]] == 0:
                        del char_count[s[i]]
                    i += 1
                maxlen = max(maxlen, j - i + 1)
            return maxlen

    def lengthOfLongestSubstringKDistinctF(self, s: str, k: int) -> int:
        char_count = {}
        i, maxlen = 0, 0

        for j in range(len(s)):
            char_count[s[j]] = char_count.get(s[j], 0) + 1

            while len(char_count) > k:
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i += 1

            maxlen = max(maxlen, j - i + 1)

        return maxlen
