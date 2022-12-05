"""
BFS/DFS Implementation, Time O(V+E) Space O(V)
"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def set_node(self, n1: int, n2: int) -> None:
        self.graph[n1].append(n2)

    def bfs(self, start_node: int):
        visited = set()
        queue = [start_node]
        visited.add(start_node)
        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for v in self.graph[node]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)

    def dfs(self, start_node: int):
        visited = set()
        stack = [start_node]
        visited.add(start_node)
        while stack:
            node = stack.pop()
            print(node, end=" ")
            for v in self.graph[node]:
                if v not in visited:
                    stack.append(v)
                    visited.add(v)


if __name__ == "__main__":
    g = Graph()
    g.set_node(2, 1)
    g.set_node(2, 5)
    g.set_node(5, 6)
    g.set_node(5, 8)
    g.set_node(6, 9)
    print("")
    print("--BFS--")
    g.bfs(2)
    print("")
    print("--DFS--")
    g.dfs(2)
