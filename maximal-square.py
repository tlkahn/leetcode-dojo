def maximalSquare(matrix):
    """
    Solution for: https://leetcode.cn/problems/maximal-square

    Calculates the size of the largest square formed by '1's in a given matrix.

    Args:
        matrix (list[list[str]]): A 2D matrix consisting of '0's and '1's.

    Returns:
        int: The area of the largest square formed by '1's in the matrix.

    Example:
        matrix = [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0']
        ]
        maximalSquare(matrix) => 4

    """
    if not matrix or not matrix[0]:
        return 0

    height, width = len(matrix), len(matrix[0])
    maxSide = 0
    dp = [[0] * (width + 1) for _ in range(height + 1)]

    for row in range(height):
        for col in range(width):
            if matrix[row][col] == "1":
                dp[row + 1][col + 1] = (
                    min(dp[row][col], dp[row][col + 1], dp[row + 1][col]) + 1
                )
                maxSide = max(maxSide, dp[row + 1][col + 1])

    return maxSide * maxSide
