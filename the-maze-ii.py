from common import *


class SolutionA:
    """
    Exceeds time limit
    """

    def shortestDistance(self, maze, start, dest):
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        self.dfs(maze, start, distance)
        return (
            -1
            if distance[dest[0]][dest[1]] == float("inf")
            else distance[dest[0]][dest[1]]
        )

    def dfs(self, maze, start, distance):
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dir in dirs:
            x, y = start[0] + dir[0], start[1] + dir[1]
            count = 0
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                x += dir[0]
                y += dir[1]
                count += 1
            if distance[start[0]][start[1]] + count < distance[x - dir[0]][y - dir[1]]:
                distance[x - dir[0]][y - dir[1]] = distance[start[0]][start[1]] + count
                self.dfs(maze, (x - dir[0], y - dir[1]), distance)


class SolutionB:
    def shortestDistance(self, maze, start, dest):
        distance = [[inf] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        queue = deque([start])

        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                count = 0

                while (
                    0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0
                ):
                    nx += dx
                    ny += dy
                    count += 1

                if distance[x][y] + count < distance[nx - dx][ny - dy]:
                    distance[nx - dx][ny - dy] = distance[x][y] + count
                    queue.append((nx - dx, ny - dy))

        return -1 if distance[dest[0]][dest[1]] == inf else distance[dest[0]][dest[1]]


class SolutionC:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], dest: List[int]
    ) -> int:
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        heap = [(0, start[0], start[1])]

        while heap:
            dist, x, y = heappop(heap)

            if visited[x][y]:
                continue

            visited[x][y] = True

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                count = 0

                while (
                    0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0
                ):
                    nx += dx
                    ny += dy
                    count += 1

                if dist + count < distance[nx - dx][ny - dy]:
                    distance[nx - dx][ny - dy] = dist + count
                    heappush(heap, (dist + count, nx - dx, ny - dy))

        return -1 if distance[dest[0]][dest[1]] == inf else distance[dest[0]][dest[1]]


import heapq


class Solution:
    def shortestDistanceD(
        self, maze: List[List[int]], start: List[int], dest: List[int]
    ) -> int:
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        heap = [(0, start[0], start[1])]

        while heap:
            dist, x, y = heapq.heappop(heap)

            if dist > distance[x][y]:
                continue

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                count = 0

                while (
                    0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0
                ):
                    nx += dx
                    ny += dy
                    count += 1

                if dist + count < distance[nx - dx][ny - dy]:
                    distance[nx - dx][ny - dy] = dist + count
                    heapq.heappush(heap, (dist + count, nx - dx, ny - dy))

        return (
            -1
            if distance[dest[0]][dest[1]] == float("inf")
            else distance[dest[0]][dest[1]]
        )
