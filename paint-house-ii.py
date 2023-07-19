from common import *


class SolutionA:
    def minCostII(self, costs):
        if len(costs) == 0:
            return 0
        elif len(costs[0]) == 1:
            return costs[0][0]

        min_colour = -1
        min_cost = 0
        second_min_cost = 0

        for cost in costs:
            tmp_min_colour = -1
            tmp_min_cost = float("inf")
            tmp_second_min_cost = float("inf")

            for i in range(len(cost)):
                this_min_cost = cost[i] + (
                    second_min_cost if i == min_colour else min_cost
                )

                if this_min_cost < tmp_min_cost:
                    tmp_second_min_cost = tmp_min_cost
                    tmp_min_cost = this_min_cost
                    tmp_min_colour = i
                elif this_min_cost < tmp_second_min_cost:
                    tmp_second_min_cost = this_min_cost

            min_cost = tmp_min_cost
            min_colour = tmp_min_colour
            second_min_cost = tmp_second_min_cost

        return min_cost


class SolutionB:
    def minCostII(self, costs):
        if not costs:
            return 0

        num_houses = len(costs)
        num_colors = len(costs[0])

        min_cost = 0
        min_color = -1
        second_min_cost = 0

        for i in range(num_houses):
            new_min_cost = float("inf")
            new_min_color = -1
            new_second_min_cost = float("inf")

            for j in range(num_colors):
                cost = costs[i][j] + (second_min_cost if j == min_color else min_cost)

                if cost < new_min_cost:
                    new_second_min_cost = new_min_cost
                    new_min_cost = cost
                    new_min_color = j
                elif cost < new_second_min_cost:
                    new_second_min_cost = cost

            min_cost = new_min_cost
            min_color = new_min_color
            second_min_cost = new_second_min_cost

        return min_cost


class SolutionC:
    def minCostII(self, costs):
        if not costs:
            return 0

        min_cost = min_color = second_min_cost = 0

        for cost in costs:
            new_min_cost = new_second_min_cost = inf

            for i, c in enumerate(cost):
                this_min_cost = c + (second_min_cost if i == min_color else min_cost)

                if this_min_cost < new_min_cost:
                    new_second_min_cost, new_min_cost = new_min_cost, this_min_cost
                    min_color = i
                elif this_min_cost < new_second_min_cost:
                    new_second_min_cost = this_min_cost

            min_cost, second_min_cost = new_min_cost, new_second_min_cost

        return min_cost


class SolutionD:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def _rob(_nums):
            @cache
            def dfs(cur):
                nonlocal _nums
                if cur == -1:
                    return 0
                if cur == 0:
                    return _nums[0]
                return max(dfs(cur - 1), _nums[cur] + dfs(cur - 2))

            return dfs(len(_nums) - 1)

        return max(_rob(nums[1:]), _rob(nums[:-1]))
