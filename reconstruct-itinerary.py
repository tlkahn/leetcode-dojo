from common import *


class Solution:
    def findItinerary(self, tickets):
        # Use defaultdict and sorted list for efficient graph creation
        graph = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)

        # Perform DFS traversal to find itinerary
        itinerary = []
        self.visit(graph, "JFK", itinerary)
        return itinerary[::-1]  # Reverse the itinerary list

    def visit(self, graph, src, itinerary):
        while graph[src]:
            dest = graph[src].pop()
            self.visit(graph, dest, itinerary)
        itinerary.append(src)


# Example usage:
# s = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# result = s.findItinerary(tickets)
# print(result)


class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dest in sorted(tickets)[::-1]:
            graph[src].append(dest)

        itinerary = []
        stack = ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())

        return itinerary[::-1]
