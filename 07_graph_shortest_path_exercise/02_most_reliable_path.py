from queue import PriorityQueue
from collections import deque


def convert_from_percent(value):
    return value / 100


# Djiikstra Algorithm
class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))
    graph[destination].append(Edge(destination, source, weight))

start = int(input())
destination = int(input())

# for node, edges in graph.items():
#     for edge in edges:
#         print(f"{node} -> {edge.__dict__}")

reliability = {node: float('-inf') for node in graph}
parent = {node: None for node in graph}
visited = {node: False for node in graph}
visited[start] = True
pq = PriorityQueue()
pq.put((1, start))

# BFS with priority queue
max_reliability = 0
while not pq.empty():
    max_reliability, node = pq.get()
    if max_reliability != 1:
        max_reliability = 1 - max_reliability
    if node == destination:
        break
    max_destination = None
    for edge in graph[node]:
        # child = edge.destination if edge.source == node else edge.source
        new_reliability = max_reliability * convert_from_percent(edge.weight)
        if new_reliability > reliability[node] and not visited[edge.destination]:
            reliability[node] = new_reliability
            parent[edge.destination] = node
            pq.put([1 - new_reliability, edge.destination])
            max_destination = edge.destination
    visited[max_destination] = True

print(f"Most reliable path reliability: {max_reliability * 100:.2f}%")


path = deque()
node = destination
while node is not None:
    path.appendleft(node)
    node = parent[node]
print(*path, sep=' -> ')
