from common import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)

        def find_exact_match(sorted_list, target):
            index = bisect_left(sorted_list, target)
            return (
                index
                if index != len(sorted_list) and sorted_list[index] == target
                else -1
            )

        @cache
        def dfs(i, j):
            if i > j:
                return -1
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[i] <= target < nums[mid]:
                if (res := find_exact_match(nums[i:mid], target)) > -1:
                    return i + res
                else:
                    return -1
            elif nums[mid] < target <= nums[j]:
                if (res := find_exact_match(nums[mid + 1 : j + 1], target)) > -1:
                    return mid + 1 + res
                else:
                    return -1
            elif nums[mid] > nums[j]:
                return dfs(mid + 1, j)
            else:
                return dfs(i, mid - 1)

        return dfs(0, N - 1)


from typing import List


class SolutionB:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
