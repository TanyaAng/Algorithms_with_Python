def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


buildings = int(input())
streets = int(input())

graph = []
edges = set()

[graph.append([]) for _ in range(buildings)]

for _ in range(streets):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.add((min(first, second), max(first, second)))

important_street = []
for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)
    visited = [False] * buildings
    dfs(0, graph, visited)

    if not all(visited):
        important_street.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

print("Important streets:")
for first, second in important_street:
    print(f"{first} {second}")
