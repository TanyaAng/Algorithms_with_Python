from collections import deque


class Path:
    def __init__(self, start, destination, lenght):
        self.start = start
        self.destination = destination
        self.lenght = lenght

    def __gt__(self, other):
        return self.destination > other.destination


nodes = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    first, second = [int(x) for x in input().split()]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    graph[first].append(second)

# print(graph)

start_node = int(input())
forest = set()
forest_edges = []

unreacheble_spots = []
for node in graph:
    if node == start_node:
        continue
    destination = node
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}

    visited[start_node] = True
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    # print(f"{start_node} -> {destination} ({len(path)-1})")
    if len(path) - 1 == 0:
        unreacheble_spots.append(destination)

for node in sorted(unreacheble_spots):
    print(node)
