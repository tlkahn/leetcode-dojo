from common import *

# Binary Tree Traversal Framework
# def traverse(root):
#     if root is None:
#         return
#     traverse(root.left)
#     traverse(root.right)

#  2D Matrix Traversal Framework
# def dfs(grid, i, j, visited):
#     m, n = len(grid), len(grid[0])
#     if i < 0 or j < 0 or i >= m or j >= n:
#         return
#     if visited[i][j]:
#         return
#     visited[i][j] = True
#     dfs(grid, i - 1, j, visited) # 上
#     dfs(grid, i + 1, j, visited) # 下
#     dfs(grid, i, j - 1, visited) # 左
#     dfs(grid, i, j + 1, visited) # 右

# 2D Matrix Traversal Framework
# This code defines a framework for traversing a 2D matrix. It
# performs depth-first search (DFS) on the given grid.  The visited
# array is used to keep track of visited cells.  If the indices i and
# j are out of bounds or the cell (i, j) has already been visited, the
# function returns. Otherwise, it marks the cell (i, j) as visited
# and recursively calls the dfs function to traverse its neighboring
# cells.

# A two-dimensional matrix can be considered as a graph because each
# cell in the matrix can be seen as a node, and the connections
# between adjacent cells represent the edges in the graph. In this
# representation, each cell has up to four neighboring cells (top,
# bottom, left, and right), which can be considered as the adjacent
# nodes in the graph.


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        traces = set()
        N = len(grid)
        M = len(grid[0])
        land = 1
        water = 0

        def dfs(i, j, dir):
            nonlocal grid, M, N, land, water
            if i < 0 or j < 0 or i >= N or j >= M:
                return ""
            if grid[i][j] == water:
                return ""
            grid[i][j] = water
            return (
                f"{dir},"
                + dfs(i + 1, j, "1")
                + ","
                + dfs(i, j + 1, "2")
                + ","
                + dfs(i - 1, j, "3")
                + ","
                + dfs(i, j - 1, "4")
                + ","
                + f"-{dir},"
            )

        for i in range(N):
            for j in range(M):
                if grid[i][j] == land:
                    traces.add(dfs(i, j, "0"))

        return len(traces)
