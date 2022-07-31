from collections import deque


# BFS
def bfs(queue, destination, graph, visited, parent):
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


def find_path_size(parent, destination):
    node = destination
    size = 0
    while node is not None:
        node = parent[node]
        size += 1
    return size - 1


# INPUTS
vertices = int(input())
pairs = int(input())

# READ GRAPH
graph = {}
for _ in range(vertices):
    p, ch = input().split(':')
    parent = int(p)
    children = [int(child) for child in ch.split()]
    if parent not in graph:
        graph[parent] = []
    for child in children:
        graph[parent].append(child)

# print(graph)

for _ in range(pairs):
    start, destination = [int(x) for x in input().split('-')]
    visited = {node: False for node in graph.keys()}
    parent = {node: None for node in graph.keys()}
    visited[start] = True
    queue = deque([start])
    bfs(queue, destination, graph, visited, parent)
    if parent[destination] is None:
        print(f"{{{start}, {destination}}} -> -1")
        continue
    size = find_path_size(parent, destination)
    print(f"{{{start}, {destination}}} -> {size}")
