def dfs(source, destination, graph, visited):
    if source in visited:
        return
    visited.add(source)
    if source == destination:
        return
    for child in graph[source]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination):
    visited = set()
    dfs(source, destination, graph, visited)
    return destination in visited


n = int(input())

graph = {}

edges = []
for _ in range(n):
    command = input()
    parent, children = command.split(' -> ')
    if parent not in graph:
        graph[parent] = []
    graph[parent] = children.split()
    for child in children:
        edges.append((parent, child))

removed_edges = []
for source, destination in sorted(edges, key=lambda item: (item[0], item[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(removed_edges)}")
for edge in removed_edges:
    print(f"{edge[0]} - {edge[1]}")
