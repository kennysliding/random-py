import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Graph:
    def __init__(self, n: int, edges: List[List[int]]) -> None:
        self.adjacency_list: defaultdict = defaultdict(list)
        self.n = n

        for edge in edges:
            from_node, to_node, cost = edge
            self.adjacency_list[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.adjacency_list[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = {vertex: float("inf") for vertex in range(self.n)}
        distances[node1] = 0

        # sort by the first element
        priority_queue = [(0, node1)]

        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)

            # if we reach the goal
            if current_node == node2:
                return current_cost

            # don't run the check again if the node is stale
            if current_cost > distances[current_node]:
                continue

            # check neighbor
            for neighbor, edge_cost in self.adjacency_list[current_node]:
                new_cost = current_cost + edge_cost

                # if the neighbor has a new cost, we can "refresh" from this node again
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
