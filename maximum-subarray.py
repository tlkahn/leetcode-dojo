class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        for i in range(1, N):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] >= 0 else nums[i]
        return max(dp)


def kadanes_algorithm(arr):
    max_sum = float("-inf")  # Initialize max_sum as negative infinity
    curr_sum = 0  # Initialize current sum as 0

    for num in arr:
        curr_sum = max(num, curr_sum + num)  # Update current sum
        max_sum = max(max_sum, curr_sum)  # Update max sum

    return max_sum


def test_kadanes_algorithm():
    # Test case 1: Basic case
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert kadanes_algorithm(arr1) == 6

    # Test case 2: All negative numbers
    arr2 = [-1, -2, -3, -4, -5]
    assert kadanes_algorithm(arr2) == -1

    # Test case 3: All positive numbers
    arr3 = [1, 2, 3, 4, 5]
    assert kadanes_algorithm(arr3) == 15

    # Test case 4: Empty array
    arr4 = []
    assert kadanes_algorithm(arr4) == float("-inf")

    # Test case 5: Array with only one element
    arr5 = [10]
    assert kadanes_algorithm(arr5) == 10

    # Test case 6: Array with all zeros
    arr6 = [0, 0, 0, 0, 0]
    assert kadanes_algorithm(arr6) == 0

    print("All test cases passed.")


test_kadanes_algorithm()
