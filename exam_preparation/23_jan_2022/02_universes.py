# VARIANT I
# def find_root(parent, node):
#     while node != parent[node]:
#         node = parent[node]
#     return node
#
#
# lines = int(input())
#
# nodes = set()
# edges = []
#
# for _ in range(lines):
#     first, second = input().split(' - ')
#     edge = (first, second)
#     edges.append((first,second))
#     nodes.add(first)
#     nodes.add(second)
#
# # print(edges)
# parent = {node: node for node in nodes}
# # print(parent)
# for edge in edges:
#     first = find_root(parent, edge[0])
#     second = find_root(parent, edge[1])
#     if first != second:
#         parent[first] = second
#
# # print(parent)
# counter = 0
# for key, value in parent.items():
#     if key == value:
#         counter += 1
#
# print(counter)


# VARIANT II
'''For every node in graph start DFS,
every time you start another DFS it means
that it is found another unconnected graph'''


def dfs(node, graph, visited, universe):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, universe)
    universe.append(node)


lines = int(input())
graph = {}
for _ in range(lines):
    first, second = input().split(' - ')
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    graph[first].append(second)
    graph[second].append(first)

# print(graph)
universe_counter = 0
visited = {node: False for node in graph}
for node in graph:
    if visited[node]:
        continue
    current_universe = []
    dfs(node, graph, visited, current_universe)
    print(*current_universe, sep=' ')
    universe_counter += 1

print(universe_counter)
