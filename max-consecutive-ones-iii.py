class Solution:
    def longestOnes(self, A, K):
        """
        This Python code implements the same sliding window approach to solve
        the "Max Consecutive Ones III" problem. It iterates through the input
        list `A`, counts the number of zeros within the window, and shrinks
        the window until the count is less than or equal to `K`. The result is
        updated with the maximum length of consecutive ones encountered, and
        finally returned.

        - The goal is to find the maximum length of consecutive ones
          in the given list `A` by flipping at most `K` zeros.
        - The variables `res`, `zeros`, and `left` are initialized to
          keep track of the maximum length, the count of zeros in the
          window, and the left index of the window, respectively.
        - The loop iterates over each element in `A`, starting from
          the right.
        - If the current element is 0, we increment the `zeros` count.
        - The `while` loop is used to shrink the window from the left
          side until the count of zeros within the window is less than
          or equal to `K`.
        - If the left element is 0, we decrement the `zeros` count and
          move the left index to the right.
        - At each iteration, we update the `res` variable with the
          maximum length of consecutive ones seen so far.
        - Finally, we return the maximum length of consecutive ones
          stored in `res`.

        This program uses a sliding window approach to find the
        maximum length of consecutive ones, allowing at most `K` zeros
        within the window. By updating the `res` variable whenever a
        longer consecutive sequence is found, the program efficiently
        finds and returns the desired result
        """
        res = 0  # Variable to store the maximum length of consecutive ones
        zeros = 0  # Count of zeros within the window
        left = 0  # Left index of the window

        for right in range(len(A)):
            if A[right] == 0:
                zeros += 1  # Increment zeros count if current element is 0

            while zeros > K:
                if A[left] == 0:
                    zeros -= 1  # Decrement zeros count if left element is 0
                left += 1  # Move the left index to shrink the window

            res = max(
                res, right - left + 1
            )  # Update the maximum length of consecutive ones

        return res  # Return the maximum length of consecutive ones


def test_longestOnes():
    test_cases = [
        ([1, 1, 0, 1, 1, 0, 0, 1, 1], 1, 5),
        ([1, 1, 1, 1, 1], 2, 5),
        ([0, 0, 0, 0, 0, 0], 3, 3),
        ([], 2, 0),
    ]

    for i, (A, K, expected) in enumerate(test_cases):
        result = Solution().longestOnes(A, K)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases pass")


# Run the test function
test_longestOnes()
