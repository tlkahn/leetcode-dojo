from typing import List, Set, Tuple, Union, DefaultDict, Generator
import numpy as np
from collections import defaultdict
from dataclasses import dataclass
from collections import deque


@dataclass
class Empty:
    pass


@dataclass
class Wall:
    pass


@dataclass
class Start:
    pass


@dataclass
class End:
    pass


@dataclass
class Portal:
    letter: str


CellType = Union[Empty, Wall, Start, End, Portal]


class Cell:
    def __init__(self, y: int, x: int, content: str):
        self.y = y
        self.x = x
        self.content = content

    @property
    def cell_type(self) -> CellType:
        if self.content == ".":
            return Empty()
        elif self.content == "#":
            return Wall()
        elif self.content == "S":
            return Start()
        elif self.content == "E":
            return End()
        elif self.content.islower():
            return Portal(self.content)
        else:
            raise ValueError(f"Unknown cell type: {self.content}")

    def __repr__(self):
        return f"Cell({self.y}, {self.x}, {self.content})"


class Grid:
    def __init__(self, chars: List[List[str]]):
        self.grid: List[List[Cell]] = []
        self.portal_map: DefaultDict[str, List[Cell]] = defaultdict(list)
        self._parse(chars)
        self.build_portal_map()

    def build_portal_map(self):
        for row in self.grid:
            for cell in row:
                if isinstance(cell.cell_type, Portal):
                    self.portal_map[cell.content].append(cell)

    def _parse(self, chars: List[List[str]]):
        for y, line in enumerate(chars):
            self.grid.append([])
            for x, char in enumerate(line):
                cell = Cell(y, x, char)
                self.grid[y].append(cell)

    def __getitem__(self, key: Tuple[int, int]) -> Cell:
        return self.grid[key[0]][key[1]]

    def __setitem__(self, key: Tuple[int, int], value: Cell):
        self.grid[key[0]][key[1]] = value

    def __str__(self):
        return "\n".join(",".join(str(cell) for cell in row) for row in self.grid)

    def find_neighbors(self, cell: Cell) -> Set[Cell]:
        row = cell.y
        col = cell.x
        neighbors = set()
        if row > 0:
            neighbors.add(self.grid[row - 1][col])
        if row < len(self.grid) - 1:
            neighbors.add(self.grid[row + 1][col])
        if col > 0:
            neighbors.add(self.grid[row][col - 1])
        if col < len(self.grid[0]) - 1:
            neighbors.add(self.grid[row][col + 1])
        return neighbors

    def _next_cell(self, cell: Cell) -> Generator[Cell, None, None]:
        neighbors = self.find_neighbors(cell)
        for neighbor in neighbors:
            if not isinstance(neighbor.cell_type, Wall):
                yield neighbor
        if isinstance(cell.cell_type, Portal):
            for portal_cell in self.portal_map[cell.content]:
                if portal_cell != cell:
                    yield portal_cell

    def next_cells(self, cell: Cell) -> Set[Cell]:
        return set(self._next_cell(cell))

    def bfs(self) -> int:
        start = next(
            cell
            for row in self.grid
            for cell in row
            if isinstance(cell.cell_type, Start)
        )
        ends = list(
            cell for row in self.grid for cell in row if isinstance(cell.cell_type, End)
        )
        queue = deque([start])
        visited = set()
        distance = {start: 0}
        while queue:
            current = queue.popleft()
            visited.add(current)
            next_cells = self.next_cells(current)
            for cell in next_cells:
                if cell not in visited:
                    if cell in ends:
                        return distance[current] + 1
                    else:
                        if cell not in queue:
                            queue.append(cell)
                            distance[cell] = distance[current] + 1
        return -1


def test():
    G1 = [["x", "S", ".", ".", "x", ".", ".", "E", "x"]]
    print(np.array(G1))
    g1 = Grid(G1)
    print(g1.bfs())


import timeit
import itertools


# Define the first version using nested loops
def nested_loops():
    N = 10
    res = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            res += 1
    return res


# Define the second version using itertools.product
def cartesian_product():
    N = 10
    for i, j in itertools.product(range(N - 1), range(N)):
        if i < j:
            pass


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    N = len(nums)
    if N == 1:
        return 1 if nums[0] >= target else 0

    ps = self.prefixsum(nums)

    i = 0
    j = 0

    candidates = []
    while i <= j and j < N:
        if ps[j + 1] - ps[i] >= target:
            while ps[j + 1] - ps[i + 1] >= target:
                i += 1
            candidates.append(j - i + 2)
            i = j
        else:
            j += 1

    return min(candidates)

    # candidates = []
    # for i in range(N):
    #     for j in range(i, N):
    #         if ps[j+1] - ps[i] >= target:
    #             candidates.append(j-i+1)

    # return min(candidates) if candidates else 0


# def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#     if not nums:
#         return 0

#     n = len(nums)
#     ans = n + 1
#     sums = [0]
#     for i in range(n):
#         sums.append(sums[-1] + nums[i])

#     for i in range(1, n + 1):
#         target = s + sums[i - 1]
#         bound = bisect.bisect_left(sums, target)
#         if bound != len(sums):
#             ans = min(ans, bound - (i - 1))

#     return 0 if ans == n + 1 else ans

# import bisect


# def minSubArrayLen(s: int, nums: List[int]) -> int:
#     if not nums:
#         return 0

#     n = len(nums)
#     ans = n + 1
#     sums = [0]  # Initialize a list to store cumulative sums

#     # Calculate cumulative sums up to each index
#     for i in range(n):
#         sums.append(sums[-1] + nums[i])

#     # Check subarrays starting from each index
#     for i in range(1, n + 1):
#         target = s + sums[i - 1]  # Calculate the target sum for subarray
#         bound = bisect.bisect_left(
#             sums, target
#         )  # Find the leftmost index where cumulative sum is greater than or equal to the target
#         if bound != len(sums):
#             ans = min(
#                 ans, bound - (i - 1)
#             )  # Update the minimum subarray length if a valid subarray is found

#     return (
#         0 if ans == n + 1 else ans
#     )  # Return 0 if no valid subarray is found, otherwise return the minimum subarray length


# def rob(nums: List[int]) -> int:
#     N = len(nums)
#     F = [0] * (N + 1)
#     F[1] = nums[0]
#     for num in range(2, N + 1):
#         F[num] = max(F[num - 1], F[num - 2] + nums[num - 1])
#     return F[-1]


# print(rob([1, 2, 3, 1]))


# def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     if not s:
#         return True

#     return any(self.proc(s, d) for d in wordDict)


# def proc(self, s: str, word: str):
#     if not s:
#         return True

#     if s.startswith(word):
#         return self.proc(s[len(word) :], word)

#     return False
