def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        if child not in graph:
            return
        dfs(child, graph, visited)

    print(node, end=' ')


def dfs2(node, graph, visited, result):
    if node in visited or node not in graph:
        return
    visited.add(node)
    result.append(node)
    for child in graph[node]:
        dfs2(child, graph, visited, result)
    if len(result) == len(graph):
        return result


# graph = {
#     1: [19, 21, 14],
#     19: [7, 12, 31, 21],
#     7: [1],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [6, 23],
#     23: [21],
#     6: [],
# }

# graph = {0: [1], 2: [3], 3: [4], 4: []}
graph = {0: [1], 1: [2, 3], 2: [3], 3: [4], 4: []}
# graph = {0: [1], 3: [4], 4: []}
visited = set()
start_node = 0
# for node in graph:
print(dfs2(start_node, graph, visited, []))
