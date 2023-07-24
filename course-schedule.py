from common import *


class SolutionA:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        [graph[p[0]].append(p[1]) for p in prerequisites]
        visited = []

        def dfs(node: int) -> bool:
            nonlocal visited
            if node in visited:
                return False
            visited.append(node)
            return all(dfs(nei) for nei in graph[node])

        return all(dfs(c) for c in range(numCourses))


class SolutionB:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        [graph[p[0]].append(p[1]) for p in prerequisites]
        visited = set()

        def dfs(node: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            return all(dfs(nei) for nei in graph[node])

        for c in range(numCourses):
            if not dfs(c):
                return False
            visited.clear()
        return True


class SolutionC:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        [graph[p[0]].append(p[1]) for p in prerequisites]
        visited = set()

        def dfs(node: int, origin: int) -> bool:
            nonlocal visited
            if node in visited:
                return node != origin
            visited.add(node)
            return all(dfs(nei, origin) for nei in graph[node])

        for c in range(numCourses):
            if not dfs(c, c):
                return False
            visited.clear()
        return True
