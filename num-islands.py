class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        count = 0

        def dfs(i, j):
            visited[i][j] = True

            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]

                if (
                    0 <= new_i < rows
                    and 0 <= new_j < cols
                    and grid[new_i][new_j] == "1"
                    and not visited[new_i][new_j]
                ):
                    dfs(new_i, new_j)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count


# M = 5
# N = 4
# visited1 = [[False] * M] * N
# visited2 = [[False] * M for _ in range(N)]
# visited1[0][0] = True
# visited2[0][0] = True

# print(visited1)
# print(visited2)
