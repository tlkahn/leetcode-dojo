from common import *


class SolutionA:
    def networkDelayTime(self, ts: List[List[int]], n: int, k: int) -> int | float:
        # Initialize the adjacency matrix
        w = [[0 if i == j else inf for i in range(n + 1)] for j in range(n + 1)]

        # Build the adjacency matrix
        for u, v, c in ts:
            w[u][v] = c

        # Find the shortest paths using Floyd-Warshall algorithm
        for p in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    w[i][j] = min(w[i][j], w[i][p] + w[p][j])

        ans = max(w[k][i] for i in range(1, n + 1))

        return -1 if ans == inf else ans


class SolutionB:
    def networkDelayTime(self, ts: List[List[int]], n: int, k: int) -> int | float:
        # Build the adjacency matrix
        w = [[inf] * (n + 1) for _ in range(n + 1)]
        for u, v, c in ts:
            w[u][v] = c

        # Dijkstra's algorithm
        dist = [inf] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            # edge relaxation
            for nei in range(1, n + 1):
                if dist[node] + w[node][nei] < dist[nei]:
                    dist[nei] = dist[node] + w[node][nei]
                    heapq.heappush(pq, (dist[nei], nei))

        # Traverse the answer
        ans = max(dist[1:]) if max(dist[1:]) != inf else -1
        return ans
