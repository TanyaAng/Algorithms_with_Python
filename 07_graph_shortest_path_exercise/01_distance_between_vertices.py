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

#print(graph)

target_nodes = []
for _ in range(pairs):
    first, second = [int(x) for x in input().split('-')]
    target_nodes.append((first, second))

# print(target_nodes)

# BUSINESS LOGIC
for node in target_nodes:
    start, destination = node
    visited = {node: False for node in graph.keys()}
    parent = {node: None for node in graph.keys()}
    visited[start] = True
    queue = deque([start])
    bfs(queue, destination, graph, visited, parent)

    if parent[destination] is None:
        print(f"{{{start}, {destination}}} -> -1")
        continue

    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    lenght = len(path) - 1
    print(f"{{{start}, {destination}}} -> {lenght}")
