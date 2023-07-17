from common import *


class SolutionA:
    def findShortestWay(
        self, maze: List[List[int]], ball: List[int], hole: List[int]
    ) -> str:
        directions = [(-1, 0, "u"), (0, 1, "r"), (0, -1, "l"), (1, 0, "d")]
        # Define the four directions: up, right, left, down, along with the corresponding characters

        m = len(maze)  # Get the size of the maze
        n = len(maze[0])
        queue = [(ball[0], ball[1])]  # Create a queue and include the starting position
        # distance stores the distance from the starting point to each point
        # string stores the corresponding string for each point
        distance = [[float("inf")] * n for _ in range(m)]
        string = [["impossible"] * n for _ in range(m)]
        distance[ball[0]][
            ball[1]
        ] = 0  # Initialize the distance and string for the starting point
        string[ball[0]][ball[1]] = ""

        while queue:
            i, j = queue.pop(0)  # Pop the coordinate values i, j

            for (
                dx,
                dy,
                letter,
            ) in (
                directions
            ):  # Iterate over the four directions, letter stores the corresponding character for the operation
                x, y, step, word = i + dx, j + dy, distance[i][j], string[i][j]
                while (
                    0 <= x < m
                    and 0 <= y < n
                    and maze[x][y] == 0
                    and (x - dx != hole[0] or y - dy != hole[1])
                ):
                    # While the x, y coordinates are valid, the corresponding value is 0, and it has not crossed the hole
                    x = (
                        x + dx
                    )  # Continue moving forward, simulating the rolling process of the ball
                    y = y + dy
                    step += 1  # Record the number of steps

                x = x - dx
                y = y - dy

                if distance[x][y] > step or (
                    distance[x][y] == step and word + letter < string[x][y]
                ):
                    # If the distance from the starting point to this point is greater than the current distance
                    # or if they are equal but the string is lexicographically smaller
                    # update the distance and string, and add the coordinates to the queue
                    distance[x][y] = step
                    string[x][y] = word + letter
                    # print(x,y,string[x][y])
                    if (
                        x != hole[0] or y != hole[1]
                    ):  # When the coordinates are not the hole coordinates
                        queue.append((x, y))  # Add them to the queue

        return string[hole[0]][hole[1]]
