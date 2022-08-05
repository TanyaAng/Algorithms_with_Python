from collections import deque

nodes = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)
    graph[destination].append(source)

start = int(input())
target = int(input())

print(graph)

visited = {node: False for node in graph}
parent = {node: None for node in graph}
visited[start] = True
queue = deque([start])

while queue:
    current_node = queue.popleft()
    if current_node == target:
        break
    for child in graph[current_node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = current_node

# print(parent)

path = deque()
node = target
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=' ')
