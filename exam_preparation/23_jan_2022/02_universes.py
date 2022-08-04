def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


lines = int(input())

graph = {}
edges = []

for _ in range(lines):
    first, second = input().split()
    edge = (first, second)
    edges.append(edge)
    if first not in graph:
        graph[first] = []
    graph[first].append(second)
    if second not in graph:
        graph[second] = []
    graph[second].append(first)

print(edges)
parent = {node: node for node in graph}
print(parent)
for edge in edges:
    first = find_root(parent, edge[0])
    second = find_root(parent, edge[1])
    if first != second:
        parent[first] = second

print(parent)
counter = 0
for key, value in parent.items():
    if key == value:
        counter += 1

print(counter)
