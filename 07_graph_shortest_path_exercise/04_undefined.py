from collections import deque

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


# Bellman Ford Algorithm
nodes = int(input())
edges = int(input())

graph = []
nodes_list = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))
    if source not in nodes_list:
        nodes_list.append(source)
    if destination not in nodes_list:
        nodes_list.append(destination)

start = int(input())
destination = int(input())



distance = {node: float('inf') for node in nodes_list}
distance[start] = 0
parent = {node: None for node in nodes_list}


for _ in range(nodes - 1):
    update=False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            update=True
    if not update:
        break

for edge in graph:
    print(edge.__dict__)
print(distance)
print(parent)

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print("Undefined")
        break
else:
    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    print(distance[destination])
