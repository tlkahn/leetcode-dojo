import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    heap = [(0, start)]
    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Traveling Salesman Problem (Held-Karp Algorithm):
import itertools

def tsp(graph, start):
    num_nodes = len(graph)
    all_sets = [set(range(num_nodes)) - {start}]
    memo = {}

    def tsp_helper(curr_node, curr_set):
        if (curr_node, curr_set) in memo:
            return memo[(curr_node, curr_set)]

        if not curr_set:
            return graph[curr_node][start]

        min_dist = float('inf')
        for next_node in curr_set:
            new_set = tuple(sorted(curr_set - {next_node}))
            dist = graph[curr_node][next_node] + tsp_helper(next_node, new_set)
            min_dist = min(min_dist, dist)

        memo[(curr_node, curr_set)] = min_dist
        return min_dist

    return tsp_helper(start, all_sets[0])

# Maximum Flow Problem (Ford-Fulkerson Algorithm):
def ford_fulkerson(graph, source, sink):
    def bfs(graph, source, sink, parent):
        visited = [False] * len(graph)
        queue = [source]
        visited[source] = True

        while queue:
            curr_node = queue.pop(0)
            for next_node, capacity in enumerate(graph[curr_node]):
                if not visited[next_node] and capacity > 0:
                    queue.append(next_node)
                    visited[next_node] = True
                    parent[next_node] = curr_node
                    if next_node == sink:
                        return True

        return False

    n = len(graph)
    parent = [-1] * n
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        curr_node = sink

        while curr_node != source:
            prev_node = parent[curr_node]
            path_flow = min(path_flow, graph[prev_node][curr_node])
            curr_node = prev_node

        max_flow += path_flow
        curr_node = sink

        while curr_node != source:
            prev_node = parent[curr_node]
            graph[prev_node][curr_node] -= path_flow
            graph[curr_node][prev_node] += path_flow
            curr_node = prev_node

    return max_flow

# Longest Common Subsequence Problem:
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Knapsack Problem:
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]
