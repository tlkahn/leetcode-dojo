from common import *


class SolutionA:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # 1.初始化队列及标记数组，存入起点
        q = deque(
            (i, 1 << i, 0) for i in range(n)
        )  # 三个属性分别为 idx, mask, dist；存入起点，起始距离0，标记
        vis = {(i, 1 << i) for i in range(n)}  # 节点编号及当前状态

        # 开始搜索
        while q:
            u, mask, dist = q.popleft()  # 弹出队头元素
            if mask == (1 << n) - 1:  # 找到答案，返回结果
                return dist
            # 扩展
            for x in graph[u]:
                nextmask = mask | (1 << x)
                if (x, nextmask) not in vis:
                    q.append((x, nextmask, dist + 1))
                    vis.add((x, nextmask))

        return 0


class SolutionB:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        vis = {(i, 1 << i) for i in range(n)}

        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                return dist

            for x in graph[u]:
                nextmask = mask | (1 << x)
                if (x, nextmask) not in vis:
                    q.append((x, nextmask, dist + 1))
                    vis.add((x, nextmask))

        return 0


class SolutionC:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque(
            (i, 1 << i, 0) for i in range(n)
        )  # Initialize the queue with tuples (idx, mask, dist) for each node
        visited = {
            (i, 1 << i) for i in range(n)
        }  # Initialize the visited set with tuples (idx, mask) for each visited node

        while q:
            idx, mask, dist = q.popleft()  # Pop the front element from the queue
            if (
                mask == (1 << n) - 1
            ):  # If all nodes have been visited, return the distance
                return dist

            for x in graph[idx]:  # Iterate through the neighbors of the current node
                nextmask = mask | (
                    1 << x
                )  # Update the mask by setting the bit corresponding to the neighbor
                if (
                    x,
                    nextmask,
                ) not in visited:  # If the neighbor has not been visited with the new mask
                    q.append(
                        (x, nextmask, dist + 1)
                    )  # Add the neighbor to the queue with updated mask and distance
                    visited.add(
                        (x, nextmask)
                    )  # Mark the neighbor as visited with the new mask

        return 0  # If no path is found, return 0


class SolutionC:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        visited = {(i, 1 << i) for i in range(n)}

        while q:
            idx, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                return dist

            for x in graph[idx]:
                nextmask = mask | (1 << x)
                if (x, nextmask) not in visited:
                    q.append((x, nextmask, dist + 1))
                    visited.add((x, nextmask))

        return 0
