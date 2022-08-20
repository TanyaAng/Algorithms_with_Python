def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


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

start_node = int(input())
visited = {node: False for node in graph}
dfs(start_node, graph, visited)

unreacheble_spots = []
for node in visited:
    if not visited[node]:
        unreacheble_spots.append(node)

if unreacheble_spots:
    print(*sorted(unreacheble_spots), sep=' ')


