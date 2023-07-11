class Solution:
    def maxDistance(self, lst: List[List[int]]) -> int:
        res = 0  # maximum distance
        min_val, max_val = float("inf"), float("-inf")  # initialize min_val and max_val

        # Iterate through the list of lists
        for inner_lst in lst:
            res = max(res, max(inner_lst[-1] - min_val, max_val - inner_lst[0]))
            min_val = min(min_val, inner_lst[0])
            max_val = max(max_val, inner_lst[-1])

        return res  # return the maximum distance
