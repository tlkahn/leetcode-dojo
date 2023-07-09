def longest_palindrome2(s):
    if len(s) < 2:
        return s

    max_len = 1
    start = 0

    for i in range(len(s)):
        # Check for odd-length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1

        # Check for even-length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1

    return s[start : start + max_len]


def longest_palindrome(s):
    if len(s) < 2:
        return s

    max_len = 1
    start = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > max_len:
                max_len = len(substring)
                start = i

    return s[start : start + max_len]
