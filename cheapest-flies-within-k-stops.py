from common import *


class SolutionA:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int | float:
        """Floyd"""
        g = [[0 if i == j else inf for j in range(n)] for i in range(n)]
        dist = [inf] * n
        for f in flights:
            g[f[0]][f[1]] = f[2]
        k += 1
        dist[src] = 0

        for _ in range(k):
            clone = dist.copy()
            for i in range(n):
                for j in range(n):
                    dist[j] = min(dist[j], clone[i] + g[i][j])

        return dist[dst] if dist[dst] < inf else -1


class SolutionB:
    def findShortestPathWithKEdges(
        self, n: int, edges: List[List[int]], src: int, dst: int, k: int
    ) -> int | float:
        """
        Dijkstra. Exceeds time limit
        """
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        pq = [(0, src, 0)]

        while pq:
            distance, node, edge_count = heapq.heappop(pq)
            if node == dst and edge_count <= k:
                return distance
            if edge_count > k:
                continue
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (distance + weight, neighbor, edge_count + 1))

        return -1


class SolutionC:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int | float:
        """
        Bellman Ford
        """
        graph = [[] for _ in range(n)]
        dist = [float("inf")] * n

        for f in flights:
            graph[f[0]].append((f[1], f[2]))

        k += 1
        dist[src] = 0

        for _ in range(k):
            clone = dist.copy()
            for i in range(n):
                for neighbor, weight in graph[i]:
                    dist[neighbor] = min(dist[neighbor], clone[i] + weight)

        return dist[dst] if dist[dst] < float("inf") else -1
