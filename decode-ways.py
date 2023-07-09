def numDecodings2(s):
    """
    Solution for [leetcode problem](
    https://leetcode.cn/problems/decode-ways/description)

    Calculates the number of ways to decode a given string.

    Args:
        s (str): The input string to be decoded.

    Returns:
        int: The number of ways to decode the input string.

    Example:
        s = "226"
        numDecodings(s)  # Returns 3

    Note:
        - The input string should only contain digits from '0' to '9'.
        - A '0' in the input string cannot be decoded by itself.
        - A '0' should be combined with the previous number if it
          forms a valid decoding.
        - Decoding can be done by combining one or two digits from the
          input string.

    """
    if s[0] == "0":
        return 0

    pre = curr = 1
    for i in range(1, len(s)):
        if s[i] == "0":
            if s[i - 1] not in ["1", "2"]:
                return 0
            curr = pre
        elif s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
            pre, curr = curr, curr + pre
        else:
            pre = curr

    return curr


# This is so beautiful that I wanna cry.
def numDecodings(s):
    if s[0] == "0":
        return 0

    pre = curr = 1
    for i in range(1, len(s)):
        pre, curr = curr, (curr if s[i] != "0" else 0) + (
            pre if "10" <= s[i - 1 : i + 1] <= "26" else 0
        )

    return curr
