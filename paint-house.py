from common import *


class SolutionA:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        curr = prev = 0

        for i in range(n):
            curr = costs[i]
            mincost = min(curr)
            minindex = costs[i].index(mincost)
            altcost = min(costs[i][:minindex] + costs[i][minindex + 1 :])
            if curr != prev:
                curr = prev + mincost
            else:
                curr = prev + altcost
            prev = curr

        return curr


# This is a Python solution to the "Paint House" problem on LeetCode.
# The function `minCost` calculates the minimum cost of painting all
# houses based on the given color costs.


class SolutionB:
    def minCost(self, costs: List[List[int]]) -> int:
        # Check if there are no costs
        if len(costs) == 0:
            return 0

        # Variables to track the minimum cost for each color
        pre_red_min = 0
        pre_blue_min = 0
        pre_green_min = 0

        # Variable to store the overall minimum cost
        min_result = inf

        # Iterate over each house
        for i in range(len(costs)):
            min_result = inf

            # Calculate the minimum cost for painting the current house with red color
            temp_red_min = min(pre_blue_min, pre_green_min) + costs[i][0]

            # Calculate the minimum cost for painting the current house with blue color
            temp_blue_min = min(pre_red_min, pre_green_min) + costs[i][1]

            # Calculate the minimum cost for painting the current house with green color
            temp_green_min = min(pre_red_min, pre_blue_min) + costs[i][2]

            # Update the overall minimum cost
            min_result = min(
                min(min(temp_green_min, temp_red_min), temp_blue_min), min_result
            )

            # Update the minimum costs for each color for the next house
            pre_red_min = temp_red_min
            pre_blue_min = temp_blue_min
            pre_green_min = temp_green_min

        # Return the minimum cost of painting all houses
        return min_result


class SolutionC:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        prev_min_costs = costs[0]

        for i in range(1, len(costs)):
            curr_min_costs = [
                min(prev_min_costs[1], prev_min_costs[2]) + costs[i][0],
                min(prev_min_costs[0], prev_min_costs[2]) + costs[i][1],
                min(prev_min_costs[0], prev_min_costs[1]) + costs[i][2],
            ]
            prev_min_costs = curr_min_costs

        return min(prev_min_costs)


class SolutionD:
    def minCost(self, costs: List[List[int]]) -> int | float:
        """
        This does not make much difference from SolutionE. Only
        starting from the beginning side rather than the end side.
        """
        if not costs:
            return 0

        @cache
        def helper(i, color):
            if i == len(costs):
                return 0

            min_cost = inf

            for j in range(3):
                if j != color:
                    min_cost = min(min_cost, costs[i][j] + helper(i + 1, j))

            return min_cost

        return min(helper(0, 0), helper(0, 1), helper(0, 2))


class SolutionE:
    def minCost(self, costs: List[List[int]]) -> int | float:
        if not costs:
            return 0
        N = len(costs)

        @cache
        def helper(i, color):
            if i == -1:
                return 0

            min_cost = float("inf")

            for j in range(3):
                if j != color:
                    min_cost = min(min_cost, costs[i][j] + helper(i - 1, j))

            return min_cost

        return min(helper(N - 1, 0), helper(N - 1, 1), helper(N - 1, 2))
