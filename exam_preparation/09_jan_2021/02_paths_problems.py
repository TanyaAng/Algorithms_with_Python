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
result = []
for x in range(len(graph) - 1):
    # ====== FIRST FIND IF THERE IS A PATH FROM EVERY START NODE TO THE END NODE
    dfs_result = dfs(x, graph, set(), [])
    if dfs_result and dfs_result not in result:
        result.append(dfs_result)

    # ======= THEN FIND IF IS THERE A PATH FROM START NODE, WHEN WE REMOVE NODE BY NODE TO THE END
    # WE NEED TO COPY THE ORIGINAL GRAPH, BECAUSE WE DON'T WANT TO CHANGE IT
    inner_graph = copy(graph)
    for y in range(x + 1, target):
        inner_graph.pop(y)
        visited = set()
        dfs_result = dfs(x, inner_graph, set(), [])
        if dfs_result and dfs_result not in result:
            result.append(dfs_result)

    # FINALLY WE TRY TO FIND PATH IF ANY OF ANOTHER NODE IS REMOVED ONE BY ONE
    # WE NEED TO COPY THE ORIGINAL GRAPH EVERY TIME BEFORE WE REMOVE NODE
    for y in range(x + 1, target):
        inner_graph = copy(graph)
        inner_graph.pop(y)
        visited = set()
        dfs_result = dfs(x, inner_graph, set(), [])
        if dfs_result and dfs_result not in result:
            result.append(dfs_result)
    graph.pop(x)


[print(*r, sep=' ') for r in sorted(result, key=lambda x: (x[0], -len(x), x[1]))]
