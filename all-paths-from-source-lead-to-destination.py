from collections import defaultdict, deque
from typing import List


class SolutionA:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], so: int, de: int
    ) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            graph[v].append(u)
            in_degree[u] += 1

        if in_degree[de]:
            return False

        queue = deque([de])

        while queue:
            node = queue.popleft()
            if node == so:
                return True

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return False


from collections import defaultdict, deque


class SolutionAA:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], so: int, de: int
    ) -> bool:
        # Create a defaultdict to store the adjacency list
        # representation of the graph
        graph = defaultdict(list)
        # Create a list to store the in-degree of each node
        in_degree = [0] * n

        # Build the graph and calculate the in-degree for each node
        for u, v in edges:
            graph[v].append(u)
            in_degree[u] += 1

        # If the destination node has a non-zero in-degree, there is a
        # cycle, so return False
        if in_degree[de]:
            return False

        # Create a deque to serve as a queue for the topological sorting algorithm
        queue = deque([de])

        # Kahn's algorithm: perform topological sorting using the queue
        while queue:
            # Remove a node from the front of the queue
            node = queue.popleft()
            # If the node is the source node, there is a path from
            # source to destination, so return True
            if node == so:
                return True

            # Decrease the in-degree of each neighbor of the current node
            #
            # In this specific section of the code:
            # - It iterates over each neighbor of the current node `node` in the graph.
            # - For each neighbor, it decreases the in-degree of that neighbor by 1.
            # - If the in-degree of the neighbor becomes zero, it
            # - means that all of its prerequisite nodes (neighbors)
            # - have been visited or processed. Hence, it is safe to
            # - add the neighbor to the queue for further processing.
            # Adding a node to the queue when its in-degree becomes
            # zero is a crucial step in topological sorting. It
            # ensures that we process the nodes in an order that
            # respects the dependencies between them. By adding a node
            # with an in-degree of zero to the queue, we indicate that
            # it has no remaining prerequisites and can be visited or
            # processed next. This helps in ensuring that all the
            # nodes are processed in the correct order, satisfying the
            # dependencies and avoiding cycles in directed graphs.

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                # If the neighbor's in-degree becomes zero, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If the function reaches this point without finding a path, return False
        return False


from collections import defaultdict


class SolutionB:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        visited = [False] * n
        onPath = [False] * n
        return self.dfs(graph, source, destination, visited, onPath)

    def dfs(self, adj, v, d, visited, onPath):
        if len(adj[v]) == 0:
            return v == d
        visited[v] = True
        onPath[v] = True
        for next_node in adj[v]:
            if (visited[next_node] and onPath[next_node]) or (
                not visited[next_node]
                and not self.dfs(adj, next_node, d, visited, onPath)
            ):
                return False
        onPath[v] = False
        return True


from collections import defaultdict


class SolutionC:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        Exceeds time limit
        """
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * n
        return self.dfs(adj, source, destination, visited)

    def dfs(self, adj, v, d, visited):
        if v == d:
            return len(adj[v]) == 0

        if visited[v]:
            return False

        visited[v] = True
        if len(adj[v]) == 0:
            visited[v] = False
            return False

        for next_node in adj[v]:
            if not self.dfs(adj, next_node, d, visited):
                visited[v] = False
                return False

        visited[v] = False
        return True
