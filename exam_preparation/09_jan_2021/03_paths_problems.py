from copy import copy


def dfs(node, graph, visited, result):
    if node in visited or node not in graph:
        return
    visited.add(node)
    result.append(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)
    if len(result) == len(graph):
        return result


nodes = int(input())
graph = {}
for node in range(nodes):
    children = [int(x) for x in input().split()]
    graph[node] = children

target = max(graph.keys())
# outer_graph = copy(graph)
result = []
for x in range(len(graph) - 1):
    dfs_result = dfs(x, graph, set(), [])
    if dfs_result:
        result.append(dfs_result)


    inner_graph = copy(graph)
    for y in range(x + 1, target):
        inner_graph.pop(y)
        visited = set()
        dfs_result = dfs(x, inner_graph, set(), [])
        if dfs_result:
            result.append(dfs_result)

    for y in range(x + 1, target):
        inner_graph = copy(graph)
        inner_graph.pop(y)
        visited = set()
        dfs_result = dfs(x, inner_graph, set(), [])
        if dfs_result:
            result.append(dfs_result)

    graph.pop(x)

unique_results = []
for r in result:
    if r not in unique_results:
        unique_results.append(r)

[print(*result, sep=' ') for result in sorted(unique_results, key=lambda x: (x[0], -len(x), x[1]))]
