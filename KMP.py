class Solution:
    def strStr(self, s: str, p: str) -> int:
        """
        The code assumes that the pattern `p` is not empty and returns 0 if it is. It then
        adds a sentinel character at the beginning of both the string `s` and the pattern
        `p` to simplify the algorithm.

        The `next` list is initialized and preprocessed using a two-pointer approach,
        comparing characters in the pattern to determine the longest proper suffix that is
        also a proper prefix. The `next` list stores the length of this suffix.

        The matching process iterates over the characters of the string `s` and pattern `p`,
        comparing them and updating the `j` pointer based on the `next` list. If a match is
        found (`j` reaches the end of the pattern), the function returns the index of the
        first occurrence. If no match is found, it returns -1.
        """
        n, m = len(s), len(p)
        if m == 0:
            return 0
        # Set sentinel
        s = " " + s
        p = " " + p
        next = [0] * (m + 1)
        # Preprocess the next array
        j = 0
        for i in range(2, m + 1):
            while j and p[i] != p[j + 1]:
                j = next[j]
            if p[i] == p[j + 1]:
                j += 1
            next[i] = j
        # Matching process
        j = 0
        for i in range(1, n + 1):
            while j and s[i] != p[j + 1]:
                j = next[j]
            if s[i] == p[j + 1]:
                j += 1
            if j == m:
                return i - m
        return -1


def strStr2(s, p):
    n, m = len(s), len(p)
    if m == 0:
        return 0

    next = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = next[j - 1]
        if p[i] == p[j]:
            j += 1
        next[i] = j

    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = next[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == m:
            return i - m + 1

    return -1


def strStr3(s, p):
    n, m = len(s), len(p)
    if m == 0:
        return 0

    next = [0] * m
    j = 0

    for i in range(1, m):
        while j and p[i] != p[j]:
            j = next[j - 1]
        j += p[i] == p[j]
        next[i] = j

    j = 0
    for i in range(n):
        while j and s[i] != p[j]:
            j = next[j - 1]
        j += s[i] == p[j]
        if j == m:
            return i - m + 1

    return -1


# #include <stdio.h>
# #include <string.h>

# int strStr(char* s, char* p) {
#     int n = strlen(s);
#     int m = strlen(p);

#     if (m == 0) {
#         return 0;
#     }

#     int next[m];
#     int j = 0;

#     next[0] = 0;
#     for (int i = 1; i < m; i++) {
#         while (j > 0 && p[i] != p[j]) {
#             j = next[j - 1];
#         }
#         if (p[i] == p[j]) {
#             j++;
#         }
#         next[i] = j;
#     }

#     j = 0;
#     for (int i = 0; i < n; i++) {
#         while (j > 0 && s[i] != p[j]) {
#             j = next[j - 1];
#         }
#         if (s[i] == p[j]) {
#             j++;
#         }
#         if (j == m) {
#             return i - m + 1;
#         }
#     }

#     return -1;
# }

# int main() {
#     char s[] = "text";
#     char p[] = "pattern";

#     int index = strStr(s, p);
#     printf("Pattern found at index: %d\n", index);

#     return 0;
# }


def computeNext(pattern):
    m = len(pattern)
    next = [0] * m
    i, j = 1, 0
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            next[i] = j
            i += 1
        else:
            if j != 0:
                j = next[j - 1]
            else:
                next[i] = 0
                i += 1

    return next


# basic example
pattern = "ababaca"
next = computeNext(pattern)
print(f"next: {next}")
assert next == [0, 0, 1, 2, 3, 0, 1]


def test_computeNext():
    # Test case 1: pattern = "ABCDABD"
    pattern1 = "ABCDABD"
    expected1 = [0, 0, 0, 0, 1, 2, 0]
    result1 = computeNext(pattern1)
    assert (
        result1 == expected1
    ), f"Test case 1 failed. Expected: {expected1}, Got: {result1}"

    # Test case 2: pattern = "AAAAAA"
    pattern2 = "AAAAAA"
    expected2 = [0, 1, 2, 3, 4, 5]
    result2 = computeNext(pattern2)
    assert (
        result2 == expected2
    ), f"Test case 2 failed. Expected: {expected2}, Got: {result2}"

    # Test case 3: pattern = "ABCDEF"
    pattern3 = "ABCDEF"
    expected3 = [0, 0, 0, 0, 0, 0]
    result3 = computeNext(pattern3)
    assert (
        result3 == expected3
    ), f"Test case 3 failed. Expected: {expected3}, Got: {result3}"

    # Test case 4: pattern = "AABAABAAA"
    pattern4 = "AABAABAAA"
    expected4 = [0, 1, 0, 1, 2, 3, 4, 5, 2]
    result4 = computeNext(pattern4)
    assert (
        result4 == expected4
    ), f"Test case 4 failed. Expected: {expected4}, Got: {result4}"

    print("All test cases passed!")


# Run the test cases
test_computeNext()


# def KMP(text, pattern):
#     m = len(pattern)
#     n = len(text)

#     # Step 1: Compute the next array using the computeNext function
#     next_array = computeNext(pattern)

#     # Step 2: Perform pattern matching
#     i = 0  # Index for text
#     j = 0  # Index for pattern

#     while i < n:
#         if j < m and pattern[j] == text[i]:
#             i += 1
#             j += 1

#             if j == m:
#                 print("Pattern found at index", i - j)
#                 j = next_array[j - 1]
#         else:
#             if j != 0:
#                 j = next_array[j - 1]
#             else:
#                 i += 1


def KMP(text, pattern):
    m = len(pattern)
    n = len(text)

    # Step 1: Compute the next array using the computeNext function
    next_array = computeNext(pattern)

    # Step 2: Perform pattern matching
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if j < m:
            if pattern[j] == text[i]:
                i += 1
                j += 1

                if j == m:
                    return i - j
            else:
                if j != 0:
                    j = next_array[j - 1]
                else:
                    i += 1
        else:
            i += 1

    return -1


def test_KMP():
    # Test case 1: Basic test case
    text = "CDABCDABDABCDABCDABD"
    pattern = "ABCDABD"
    result = KMP(text, pattern)
    print("Pattern found at index", result) if result != -1 else print(
        "Pattern not found"
    )

    # Test case 2: Pattern not present in the text
    text = "ABCDABDABCDABCDABD"
    pattern = "XYZ"
    result = KMP(text, pattern)
    print("Pattern found at index", result) if result != -1 else print(
        "Pattern not found"
    )

    # Test case 3: Pattern occurs multiple times in the text
    text = "ABABABAB"
    pattern = "AB"
    result = KMP(text, pattern)
    print("Pattern found at index", result) if result != -1 else print(
        "Pattern not found"
    )

    # Test case 4: Pattern is empty
    text = "ABCDABDABCDABCDABD"
    pattern = ""
    result = KMP(text, pattern)
    print("Pattern found at index", result) if result != -1 else print(
        "Pattern not found"
    )

    # Test case 5: Text is empty
    text = ""
    pattern = "ABCDABD"
    result = KMP(text, pattern)
    print("Pattern found at index", result) if result != -1 else print(
        "Pattern not found"
    )


test_KMP()
