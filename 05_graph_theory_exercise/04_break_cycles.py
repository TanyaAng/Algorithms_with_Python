from collections import deque


def dfs(source, destination, graph, visited, path):
    if source in visited:
        return
    visited.add(source)
    if source == destination:
        # path.appendleft(source)
        return
    for child in graph[source]:
        dfs(child, destination, graph, visited, path)
    # path.appendleft(source)


def path_exists(source, destination):
    visited = set()
    current_path = deque()
    dfs(source, destination, graph, visited, current_path)
    return destination in visited


n = int(input())

graph = {}
edges = []
for _ in range(n):
    command = input()
    parent, children = command.split(' -> ')
    if parent not in graph:
        graph[parent] = []
    children = children.split()
    graph[parent] = children
    for child in children:
        edges.append((parent, child))

print(graph)
print(edges)

edges_to_remove = []
for source, destination in sorted(edges, key=lambda item: (item[0], item[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)
    is_path_exists= path_exists(source, destination)
    if is_path_exists:
        # print(f"From {source} to {destination} there is another path: {path}")
        edges_to_remove.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(edges_to_remove)}")
for edge in edges_to_remove:
    print(f"{edge[0]} - {edge[1]}")
