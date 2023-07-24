from common import *


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        clonemap = {}

        def dfs(node: Node) -> Node:
            if nurse-
                nc = Node(node.val, [])
                clonemap[node] = nc
                nc.neighbors = [dfs(n) for n in node.neighbors]
                return nc
            return clonemap[node]

        if not node:
            return
        dfs(node)
