from common import *


class SolutionA:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        return self.dfs(maze, start, destination, visited)

    def dfs(
        self,
        maze: List[List[int]],
        start: List[int],
        destination: List[int],
        visited: List[List[bool]],
    ) -> bool:
        if visited[start[0]][start[1]]:
            return False
        if start[0] == destination[0] and start[1] == destination[1]:
            return True
        visited[start[0]][start[1]] = True
        r, l, u, d = start[1] + 1, start[1] - 1, start[0] - 1, start[0] + 1

        while r < len(maze[0]) and maze[start[0]][r] == 0:  # right
            r += 1
        if self.dfs(maze, [start[0], r - 1], destination, visited):
            return True

        while l >= 0 and maze[start[0]][l] == 0:  # left
            l -= 1
        if self.dfs(maze, [start[0], l + 1], destination, visited):
            return True

        while u >= 0 and maze[u][start[1]] == 0:  # up
            u -= 1
        if self.dfs(maze, [u + 1, start[1]], destination, visited):
            return True

        while d < len(maze) and maze[d][start[1]] == 0:  # down
            d += 1
        if self.dfs(maze, [d - 1, start[1]], destination, visited):
            return True

        return False


class SolutionB:
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up, right, down, left

    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        n, m = len(maze), len(maze[0])
        visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
        queue = deque()

        for i in range(4):
            visited[start[0]][start[1]][i] = True
            queue.append([i, start[0], start[1]])

        while queue:
            d, x, y = queue.popleft()
            row, col = x + self.directions[d][0], y + self.directions[d][1]

            if 0 <= row < n and 0 <= col < m and maze[row][col] == 0:
                if not visited[row][col][d]:
                    visited[row][col][d] = True
                    queue.append([d, row, col])
            else:
                if x == destination[0] and y == destination[1]:
                    return True

                for i in range(4):
                    if i != d and not visited[x][y][i]:
                        visited[x][y][i] = True
                        queue.append([i, x, y])

        return False
